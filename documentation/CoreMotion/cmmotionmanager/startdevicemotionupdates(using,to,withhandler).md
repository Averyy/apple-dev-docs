# startDeviceMotionUpdates(using:to:withHandler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Starts device-motion updates on an operation queue and using a specified reference frame and block handler.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startDeviceMotionUpdates(using referenceFrame: CMAttitudeReferenceFrame, to queue: OperationQueue, withHandler handler: @escaping CMDeviceMotionHandler)
```

```objc
- (void) startDeviceMotionUpdatesUsingReferenceFrame:(CMAttitudeReferenceFrame) referenceFrame toQueue:(NSOperationQueue *) queue withHandler:(CMDeviceMotionHandler) handler;
```

## Discussion

You must call [`stopDeviceMotionUpdates()`](./stopdevicemotionupdates%28%29.md) when you no longer want your app to process device-motion updates.

## Parameters

- `referenceFrame`: A constant identifying the reference frame to use for device-motion updates. It’s your responsibility to specify a reference frame that’s available on the current device. Call [`availableAttitudeReferenceFrames()`](./availableattitudereferenceframes%28%29.md) to determine which reference frames are currently available.
- `queue`: An operation queue provided by the caller. Because the processed events might arrive at a high rate, using the main operation queue is not recommended.
- `handler`: A block that is invoked with each update to handle new device-motion data. The block must conform to the [`CMDeviceMotionHandler`](../cmdevicemotionhandler.md) type.

## See Also

### Managing device motion updates
- [var deviceMotionBody: (any CMBodyIdentifiable)?](./devicemotionbody.md)
  A physical body or view that defines the coordinate system for device-motion data.
- [var showsDeviceMovementDisplay: Bool](./showsdevicemovementdisplay.md)
  Controls whether the device-movement display is shown.
- [var deviceMotionUpdateInterval: TimeInterval](./devicemotionupdateinterval.md)
  The interval, in seconds, for providing device-motion updates to the block handler.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startdevicemotionupdates(using:to:withhandler:))*