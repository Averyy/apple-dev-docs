# startGyroUpdates(to:withHandler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Starts gyroscope updates on an operation queue and with a specified handler.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startGyroUpdates(to queue: OperationQueue, withHandler handler: @escaping CMGyroHandler)
```

```objc
- (void) startGyroUpdatesToQueue:(NSOperationQueue *) queue withHandler:(CMGyroHandler) handler;
```

## Mentions

- [Getting raw gyroscope events](../getting-raw-gyroscope-events.md)

## Discussion

You must call [`stopGyroUpdates()`](./stopgyroupdates%28%29.md) when you no longer want your app to process gyroscope updates.

## Parameters

- `queue`: An operation queue provided by the caller. Because the processed events might arrive at a high rate, using the main operation queue is not recommended.
- `handler`: A block that is invoked with each update to handle new gyroscope data. The block must conform to the [`CMGyroHandler`](../cmgyrohandler.md) type.

## See Also

### Managing Gyroscope Updates
- [var gyroUpdateInterval: TimeInterval](./gyroupdateinterval.md)
  The interval, in seconds, for providing gyroscope updates to the block handler.
- [func startGyroUpdates()](./startgyroupdates%28%29.md)
  Starts gyroscope updates without a handler.
- [func stopGyroUpdates()](./stopgyroupdates%28%29.md)
  Stops gyroscope updates.
- [var gyroData: CMGyroData?](./gyrodata.md)
  The latest sample of gyroscope data.
- [typealias CMGyroHandler](../cmgyrohandler.md)
  The type of block callback for handling gyroscope data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates(to:withhandler:))*