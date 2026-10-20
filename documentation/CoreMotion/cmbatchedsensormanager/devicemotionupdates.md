# CMBatchedSensorManager.DeviceMotionUpdates

**Framework**: Core Motion  
**Kind**: struct  
**Role**: Structure

**Availability**:
- watchOS 10.0+

## Declaration

```swift
struct DeviceMotionUpdates
```

## Topics

### Structures
- [CMBatchedSensorManager.DeviceMotionUpdates.Iterator](./devicemotionupdates/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Collecting device-motion data
- [func startDeviceMotionUpdates()](./startdevicemotionupdates%28%29.md)
- [func startDeviceMotionUpdates(handler: ([CMDeviceMotion]?, (any Error)?) -> Void)](./startdevicemotionupdates%28handler%29.md)
- [func stopDeviceMotionUpdates()](./stopdevicemotionupdates%28%29.md)
- [var deviceMotionBatch: [CMDeviceMotion]?](./devicemotionbatch.md)
- [func deviceMotionUpdates() -> CMBatchedSensorManager.DeviceMotionUpdates](./devicemotionupdates%28%29.md)
- [var isDeviceMotionActive: Bool](./isdevicemotionactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/devicemotionupdates)*