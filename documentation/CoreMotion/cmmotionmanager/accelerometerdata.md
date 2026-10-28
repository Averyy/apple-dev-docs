# accelerometerData

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) CMAccelerometerData * accelerometerData;
```

## Mentions

- [Getting raw accelerometer events](../getting-raw-accelerometer-events.md)

## Discussion

If no accelerometer data is available, the value of this property is `nil`. An app that is receiving accelerometer data after calling [`startAccelerometerUpdates()`](./startaccelerometerupdates%28%29.md) periodically checks the value of this property and processes the acceleration data.

## See Also

### Managing Accelerometer Updates
- [var accelerometerUpdateInterval: TimeInterval](./accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](./startaccelerometerupdates%28to,withhandler%29.md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](./startaccelerometerupdates%28%29.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](./stopaccelerometerupdates%28%29.md)
  Stops accelerometer updates.
- [typealias CMAccelerometerHandler](../cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerdata)*