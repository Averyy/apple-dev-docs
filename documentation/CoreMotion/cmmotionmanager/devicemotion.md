# deviceMotion

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The latest sample of device-motion data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var deviceMotion: CMDeviceMotion? { get }
```

```objc
@property (readonly, nullable) CMDeviceMotion * deviceMotion;
```

## Mentions

- [Getting processed device-motion data](../getting-processed-device-motion-data.md)

#### Discussion

If no device-motion data is available, the value of this property is `nil`. An app that is receiving device-motion data after calling [`startDeviceMotionUpdates()`](./startdevicemotionupdates%28%29.md) periodically checks the value of this property and processes the device-motion data.

## See Also

### Managing device motion updates
- [var deviceMotionBody: (any CMBodyIdentifiable)?](./devicemotionbody.md)
  A physical body or view that defines the coordinate system for device-motion data.
- [var showsDeviceMovementDisplay: Bool](./showsdevicemovementdisplay.md)
  Controls whether the device-movement display is shown.
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
- [typealias CMDeviceMotionHandler](../cmdevicemotionhandler.md)
  The type of block callback for handling device-motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)*