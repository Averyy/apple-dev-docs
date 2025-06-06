# deviceMotion

**Framework**: Core Motion  
**Kind**: property

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

## Mentions

- [Getting processed device-motion data](getting-processed-device-motion-data.md)

#### Discussion

If no device-motion data is available, the value of this property is `nil`. An app that is receiving device-motion data after calling [`startDeviceMotionUpdates()`](cmmotionmanager/startdevicemotionupdates().md) periodically checks the value of this property and processes the device-motion data.

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
- [typealias CMDeviceMotionHandler](cmdevicemotionhandler.md)
  The type of block callback for handling device-motion data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/devicemotion)*