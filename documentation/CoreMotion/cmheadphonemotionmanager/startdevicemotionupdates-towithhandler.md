# startDeviceMotionUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

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

## Parameters

- `queue`: The queue for handling updates.
- `handler`: The handler that receives the updates.

## See Also

- [func startDeviceMotionUpdates()](cmheadphonemotionmanager/startdevicemotionupdates.md)
  Starts device-motion updates.
- [func startConnectionStatusUpdates()](cmheadphonemotionmanager/startconnectionstatusupdates.md)
- [func stopDeviceMotionUpdates()](cmheadphonemotionmanager/stopdevicemotionupdates.md)
  Stops device-motion updates.
- [func stopConnectionStatusUpdates()](cmheadphonemotionmanager/stopconnectionstatusupdates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/startdevicemotionupdates(to:withhandler:))*