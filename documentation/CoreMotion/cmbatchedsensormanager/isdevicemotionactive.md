# isDeviceMotionActive

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var isDeviceMotionActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isDeviceMotionActive) BOOL deviceMotionActive;
```

## See Also

### Collecting device-motion data
- [func startDeviceMotionUpdates()](./startdevicemotionupdates%28%29.md)
- [func startDeviceMotionUpdates(handler: ([CMDeviceMotion]?, (any Error)?) -> Void)](./startdevicemotionupdates%28handler%29.md)
- [func stopDeviceMotionUpdates()](./stopdevicemotionupdates%28%29.md)
- [var deviceMotionBatch: [CMDeviceMotion]?](./devicemotionbatch.md)
- [func deviceMotionUpdates() -> CMBatchedSensorManager.DeviceMotionUpdates](./devicemotionupdates%28%29.md)
- [CMBatchedSensorManager.DeviceMotionUpdates](./devicemotionupdates.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/isdevicemotionactive)*