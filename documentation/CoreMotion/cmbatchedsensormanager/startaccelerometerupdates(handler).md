# startAccelerometerUpdates(handler:)

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
func startAccelerometerUpdates(handler: @escaping ([CMAccelerometerData]?, (any Error)?) -> Void)
```

```objc
- (void) startAccelerometerUpdatesWithHandler:(void (^)(NSArray<CMAccelerometerData *> *data, NSError *error)) handler;
```

## See Also

### Collecting accelerometer data
- [func startAccelerometerUpdates()](./startaccelerometerupdates%28%29.md)
- [func stopAccelerometerUpdates()](./stopaccelerometerupdates%28%29.md)
- [var accelerometerBatch: [CMAccelerometerData]?](./accelerometerbatch.md)
- [func accelerometerUpdates() -> CMBatchedSensorManager.AccelerometerUpdates](./accelerometerupdates%28%29.md)
- [CMBatchedSensorManager.AccelerometerUpdates](./accelerometerupdates.md)
- [var isAccelerometerActive: Bool](./isaccelerometeractive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmbatchedsensormanager/startaccelerometerupdates(handler:))*