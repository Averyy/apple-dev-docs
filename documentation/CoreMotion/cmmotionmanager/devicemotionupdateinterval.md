# deviceMotionUpdateInterval

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The interval, in seconds, for providing device-motion updates to the block handler.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var deviceMotionUpdateInterval: TimeInterval { get set }
```

```objc
@property (nonatomic, assign) NSTimeInterval deviceMotionUpdateInterval;
```

## Mentions

- [Getting processed device-motion data](../getting-processed-device-motion-data.md)

#### Discussion

The system supplies device-motion updates to the block handler specified in [`startDeviceMotionUpdates(to:withHandler:)`](./startdevicemotionupdates%28to,withhandler%29.md) at regular intervals determined by the value of this property. The interval units are in seconds. The value of this property is capped to minimum and maximum values; the maximum value is determined by the maximum frequency supported by the hardware. If your app is sensitive to the intervals of device-motion data, it should always check the timestamps of the delivered [`CMDeviceMotion`](../cmdevicemotion.md) instances to determine the true update interval.

## See Also

### Managing device motion updates
- [var deviceMotionBody: (any CMBodyIdentifiable)?](./devicemotionbody.md)
  A physical body or view that defines the coordinate system for device-motion data.
- [var showsDeviceMovementDisplay: Bool](./showsdevicemovementdisplay.md)
  Controls whether the device-movement display is shown.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotionupdateinterval)*