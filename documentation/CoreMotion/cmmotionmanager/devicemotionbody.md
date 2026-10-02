# deviceMotionBody

**Framework**: Core Motion  
**Kind**: property

A physical body or view that defines the coordinate system for device-motion data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var deviceMotionBody: (any CMBodyIdentifiable)? { get set }
```

#### Discussion

Set this property to associate device-motion calculations with a specific body or view, such as a [`UIKit`](https://developer.apple.com/documentation/uikit) [`UIView`](https://developer.apple.com/documentation/uikit/uiview) that conforms to [`CMBodyIdentifiable`](cmbodyidentifiable.md).

When this property is `nil`, Core Motion calculates motion updates using the device’s hardware coordinate frame. When you set this property to an identifiable body, Core Motion transforms motion data, including 3D orientation, rotation rate, gravity, and user acceleration to match the current orientation of that view. The system updates this transformation automatically whenever the view rotates or changes position.

On iPhone Duo, setting this property also identifies which display your app occupies. For example, when iPhone Duo is seated with the camera-side down on a surface, setting `deviceMotionBody` to your view allows your app to receive motion data relative to that active display and detect which face is up.

Because coordinate transformations apply directly to each specified view rather than across the entire app, you can create separate motion manager instances for different views. For example, an app can display two distinct bubble levels side by side across separate views to check surface tilt, with one level tracking horizontal alignment and the other tracking vertical alignment. Each motion manager tracks its own view orientation independently.

```swift
let motionManager = CMMotionManager()

override func viewDidLoad() {
    super.viewDidLoad()
    
    // Align device motion with this view's orientation.
    motionManager.deviceMotionBody = view
    
    motionManager.startDeviceMotionUpdates(using: .xTrueNorthZVertical, to: .main) { motion, error in
        guard let motion else { return }
        // Motion data automatically aligns with the view's current orientation.
    }
}
```

> **Note**: On platforms where body-relative motion calculation isn’t supported, Core Motion reports motion data using the default device coordinate frame.

## Topics

### Motion configuration
- [protocol CMBodyIdentifiable](cmbodyidentifiable.md)
  A type that identifies a physical body or view for device-motion calculations.

## See Also

- [var showsDeviceMovementDisplay: Bool](cmmotionmanager/showsdevicemovementdisplay.md)
  Controls whether the device-movement display is shown.
- [var deviceMotionUpdateInterval: TimeInterval](cmmotionmanager/devicemotionupdateinterval.md)
  The interval, in seconds, for providing device-motion updates to the block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)](cmmotionmanager/startdevicemotionupdates(using:to:withhandler:).md)
  Starts device-motion updates on an operation queue and using a specified reference frame and block handler.
- [func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)](cmmotionmanager/startdevicemotionupdates(to:withhandler:).md)
  Starts device-motion updates on an operation queue and using a specified block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)](cmmotionmanager/startdevicemotionupdates(using:).md)
  Starts device-motion updates using a reference frame but without a block handler.
- [func startDeviceMotionUpdates()](cmmotionmanager/startdevicemotionupdates.md)
  Starts device-motion updates without a block handler.
- [func stopDeviceMotionUpdates()](cmmotionmanager/stopdevicemotionupdates.md)
  Stops device-motion updates.
- [var deviceMotion: CMDeviceMotion?](cmmotionmanager/devicemotion.md)
  The latest sample of device-motion data.
- [typealias CMDeviceMotionHandler](cmdevicemotionhandler.md)
  The type of block callback for handling device-motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionbody)*