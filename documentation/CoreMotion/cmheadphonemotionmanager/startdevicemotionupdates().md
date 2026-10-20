# startDeviceMotionUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) startDeviceMotionUpdates;
```

#### Discussion

To receive the latest device-motion data, examine the [`deviceMotion`](./devicemotion.md) property.

## See Also

### Starting and Stopping Updates
- [func startDeviceMotionUpdates(to: OperationQueue, withHandler: CMHeadphoneMotionManager.DeviceMotionHandler)](./startdevicemotionupdates%28to,withhandler%29.md)
  Starts device-motion updates with a handler.
- [func startConnectionStatusUpdates()](./startconnectionstatusupdates%28%29.md)
- [func stopDeviceMotionUpdates()](./stopdevicemotionupdates%28%29.md)
  Stops device-motion updates.
- [func stopConnectionStatusUpdates()](./stopconnectionstatusupdates%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/startdevicemotionupdates())*