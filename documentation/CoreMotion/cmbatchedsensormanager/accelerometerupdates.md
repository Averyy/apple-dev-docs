# CMBatchedSensorManager.AccelerometerUpdates

**Framework**: Core Motion  
**Kind**: struct  
**Role**: Structure

**Availability**:
- watchOS 10.0+

## Declaration

```swift
struct AccelerometerUpdates
```

## Topics

### Structures
- [CMBatchedSensorManager.AccelerometerUpdates.Iterator](./accelerometerupdates/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Collecting accelerometer data
- [func startAccelerometerUpdates()](./startaccelerometerupdates%28%29.md)
- [func startAccelerometerUpdates(handler: ([CMAccelerometerData]?, (any Error)?) -> Void)](./startaccelerometerupdates%28handler%29.md)
- [func stopAccelerometerUpdates()](./stopaccelerometerupdates%28%29.md)
- [var accelerometerBatch: [CMAccelerometerData]?](./accelerometerbatch.md)
- [func accelerometerUpdates() -> CMBatchedSensorManager.AccelerometerUpdates](./accelerometerupdates%28%29.md)
- [var isAccelerometerActive: Bool](./isaccelerometeractive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerupdates)*