# startAccelerometerUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method

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

## Mentions

- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)

#### Discussion

You must call [`stopAccelerometerUpdates()`](cmmotionmanager/stopaccelerometerupdates().md) when you no longer want your app to process accelerometer updates.

## Parameters

- `queue`: An operation queue provided by the caller. Because the processed events might arrive at a high rate, using the main operation queue is not recommended.
- `handler`: A block that is invoked with each update to handle new accelerometer data. The block must conform to the   type.

## See Also

- [var accelerometerUpdateInterval: TimeInterval](cmmotionmanager/accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates()](cmmotionmanager/startaccelerometerupdates.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](cmmotionmanager/stopaccelerometerupdates.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](cmmotionmanager/accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startaccelerometerupdates(to:withhandler:))*