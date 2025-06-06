# startDeviceMotionUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

Starts device-motion updates on an operation queue and using a specified block handler.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startDeviceMotionUpdates(to queue: OperationQueue, withHandler handler: @escaping CMDeviceMotionHandler)
```

#### Discussion

This method reports motion relative to the reference frame in the [`attitudeReferenceFrame`](cmmotionmanager/attitudereferenceframe.md) property. You must call [`stopDeviceMotionUpdates()`](cmmotionmanager/stopdevicemotionupdates().md) when you no longer want your app to process device-motion updates.

## Parameters

- `queue`: An operation queue provided by the caller. Because the processed events might arrive at a high rate, using the main operation queue is not recommended.
- `handler`: A block that is invoked with each update to handle new device-motion data. The block must conform to the   type.

## See Also

- [var showsDeviceMovementDisplay: Bool](cmmotionmanager/showsdevicemovementdisplay.md)
  Controls whether the device-movement display is shown.
- [var deviceMotionUpdateInterval: TimeInterval](cmmotionmanager/devicemotionupdateinterval.md)
  The interval, in seconds, for providing device-motion updates to the block handler.
- [func startDeviceMotionUpdates(using: CMAttitudeReferenceFrame, to: OperationQueue, withHandler: CMDeviceMotionHandler)](cmmotionmanager/startdevicemotionupdates(using:to:withhandler:).md)
  Starts device-motion updates on an operation queue and using a specified reference frame and block handler.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(to:withhandler:))*