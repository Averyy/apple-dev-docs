# showsDeviceMovementDisplay

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

Controls whether the device-movement display is shown.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var showsDeviceMovementDisplay: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL showsDeviceMovementDisplay;
```

#### Discussion

When a device requires movement (for example, to calibrate the compass), the value of this property indicates if the system’s device-movement display should be shown. When a device requires movement, the block handler of type [`CMDeviceMotionHandler`](../cmdevicemotionhandler.md) reports the [`CMErrorDeviceRequiresMovement`](../cmerrordevicerequiresmovement.md) error once. By default, this property is [`false`](../../Swift/false.md).

## See Also

### Managing device motion updates
- [var deviceMotionBody: (any CMBodyIdentifiable)?](./devicemotionbody.md)
  A physical body or view that defines the coordinate system for device-motion data.
- [var deviceMotionUpdateInterval: TimeInterval](./devicemotionupdateinterval.md)
  The interval, in seconds, for providing device-motion updates to the block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)](./startdevicemotionupdates%28using,to,withhandler%29.md)
  Starts device-motion updates on an operation queue and using a specified reference frame and block handler.
- [func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMDeviceMotionHandler)](./startdevicemotionupdates%28to,withhandler%29.md)
  Starts device-motion updates on an operation queue and using a specified block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame)](./startdevicemotionupdates%28using%29.md)
  Starts device-motion updates using a reference frame but without a block handler.
- [func startDeviceMotionUpdates()](./startdevicemotionupdates%28%29.md)
  Starts device-motion updates without a block handler.
- [func stopDeviceMotionUpdates()](./stopdevicemotionupdates%28%29.md)
  Stops device-motion updates.
- [var deviceMotion: CMDeviceMotion?](./devicemotion.md)
  The latest sample of device-motion data.
- [typealias CMDeviceMotionHandler](../cmdevicemotionhandler.md)
  The type of block callback for handling device-motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/showsdevicemovementdisplay)*