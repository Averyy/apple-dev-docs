# startDeviceMotionUpdates()

**Framework**: Core Motion  
**Kind**: method

Starts device-motion updates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
func startDeviceMotionUpdates()
```

#### Discussion

To receive the latest device-motion data, examine the [`deviceMotion`](cmheadphonemotionmanager/devicemotion.md) property.

## See Also

- [func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMHeadphoneMotionManager.DeviceMotionHandler)](cmheadphonemotionmanager/startdevicemotionupdates(to:withhandler:).md)
  Starts device-motion updates with a handler.
- [func startConnectionStatusUpdates()](cmheadphonemotionmanager/startconnectionstatusupdates.md)
- [func stopDeviceMotionUpdates()](cmheadphonemotionmanager/stopdevicemotionupdates.md)
  Stops device-motion updates.
- [func stopConnectionStatusUpdates()](cmheadphonemotionmanager/stopconnectionstatusupdates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/startdevicemotionupdates())*