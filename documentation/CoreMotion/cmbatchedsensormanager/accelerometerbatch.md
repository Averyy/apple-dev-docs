# accelerometerBatch

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
var accelerometerBatch: [CMAccelerometerData]? { get }
```

```objc
@property (readonly, nullable) NSArray<CMAccelerometerData *> * accelerometerBatch;
```

## See Also

### Collecting accelerometer data
- [func startAccelerometerUpdates()](./startaccelerometerupdates%28%29.md)
- [func startAccelerometerUpdates(handler: ([CMAccelerometerData]?, (any Error)?) -> Void)](./startaccelerometerupdates%28handler%29.md)
- [func stopAccelerometerUpdates()](./stopaccelerometerupdates%28%29.md)
- [func accelerometerUpdates() -> CMBatchedSensorManager.AccelerometerUpdates](./accelerometerupdates%28%29.md)
- [CMBatchedSensorManager.AccelerometerUpdates](./accelerometerupdates.md)
- [var isAccelerometerActive: Bool](./isaccelerometeractive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/accelerometerbatch)*