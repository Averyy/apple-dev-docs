# startAccelerometerUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Starts accelerometer updates on an operation queue and with a specified handler.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startAccelerometerUpdates(to queue: OperationQueue, withHandler handler: @escaping CMAccelerometerHandler)
```

```objc
- (void) startAccelerometerUpdatesToQueue:(NSOperationQueue *) queue withHandler:(CMAccelerometerHandler) handler;
```

## Mentions

- [Getting raw accelerometer events](../getting-raw-accelerometer-events.md)

## Discussion

You must call [`stopAccelerometerUpdates()`](./stopaccelerometerupdates%28%29.md) when you no longer want your app to process accelerometer updates.

## Parameters

- `queue`: An operation queue provided by the caller. Because the processed events might arrive at a high rate, using the main operation queue is not recommended.
- `handler`: A block that is invoked with each update to handle new accelerometer data. The block must conform to the [`CMAccelerometerHandler`](../cmaccelerometerhandler.md) type.

## See Also

### Managing Accelerometer Updates
- [var accelerometerUpdateInterval: TimeInterval](./accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates()](./startaccelerometerupdates%28%29.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](./stopaccelerometerupdates%28%29.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](./accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](../cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))*