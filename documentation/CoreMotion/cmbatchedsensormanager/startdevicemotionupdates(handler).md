# startDeviceMotionUpdates(handler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func startDeviceMotionUpdates(handler: @escaping ([CMDeviceMotion]?, (any Error)?) -> Void)
```

```objc
- (void) startDeviceMotionUpdatesWithHandler:(void (^)(NSArray<CMDeviceMotion *> *data, NSError *error)) handler;
```

## See Also

### Collecting device-motion data
- [func startDeviceMotionUpdates()](./startdevicemotionupdates%28%29.md)
- [func stopDeviceMotionUpdates()](./stopdevicemotionupdates%28%29.md)
- [var deviceMotionBatch: [CMDeviceMotion]?](./devicemotionbatch.md)
- [func deviceMotionUpdates() -> CMBatchedSensorManager.DeviceMotionUpdates](./devicemotionupdates%28%29.md)
- [CMBatchedSensorManager.DeviceMotionUpdates](./devicemotionupdates.md)
- [var isDeviceMotionActive: Bool](./isdevicemotionactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startdevicemotionupdates(handler:))*