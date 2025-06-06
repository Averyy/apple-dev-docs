# accelerometerData

**Framework**: Core Motion  
**Kind**: property

The latest sample of accelerometer data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var accelerometerData: CMAccelerometerData? { get }
```

## Mentions

- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)

#### Discussion

If no accelerometer data is available, the value of this property is `nil`. An app that is receiving accelerometer data after calling [`startAccelerometerUpdates()`](cmmotionmanager/startaccelerometerupdates().md) periodically checks the value of this property and processes the acceleration data.

## See Also

- [var accelerometerUpdateInterval: TimeInterval](cmmotionmanager/accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](cmmotionmanager/startaccelerometerupdates.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](cmmotionmanager/stopaccelerometerupdates.md)
  Stops accelerometer updates.
- [typealias CMAccelerometerHandler](cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)*