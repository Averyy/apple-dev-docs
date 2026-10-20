# startDeviceMotionUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Starts device-motion updates with a handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
func startDeviceMotionUpdates(to queue: OperationQueue, withHandler handler: @escaping CMHeadphoneMotionManager.DeviceMotionHandler)
```

```objc
- (void) startDeviceMotionUpdatesToQueue:(NSOperationQueue *) queue withHandler:(CMHeadphoneDeviceMotionHandler) handler;
```

## Parameters

- `queue`: The queue for handling updates.
- `handler`: The handler that receives the updates.

## See Also

### Starting and Stopping Updates
- [func startDeviceMotionUpdates()](./startdevicemotionupdates%28%29.md)
  Starts device-motion updates.
- [func startConnectionStatusUpdates()](./startconnectionstatusupdates%28%29.md)
- [func stopDeviceMotionUpdates()](./stopdevicemotionupdates%28%29.md)
  Stops device-motion updates.
- [func stopConnectionStatusUpdates()](./stopconnectionstatusupdates%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/startdevicemotionupdates(to:withhandler:))*