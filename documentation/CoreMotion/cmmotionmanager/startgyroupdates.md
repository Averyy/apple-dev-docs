# startGyroUpdates()

**Framework**: Core Motion  
**Kind**: method

Starts gyroscope updates without a handler.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startGyroUpdates()
```

## Mentions

- [Getting raw gyroscope events](getting-raw-gyroscope-events.md)

#### Discussion

You can get the latest gyroscope data through the [`gyroData`](cmmotionmanager/gyrodata.md) property. You must call [`stopGyroUpdates()`](cmmotionmanager/stopgyroupdates().md) when you no longer want your app to process gyroscope updates.

## See Also

- [var gyroUpdateInterval: TimeInterval](cmmotionmanager/gyroupdateinterval.md)
  The interval, in seconds, for providing gyroscope updates to the block handler.
- [func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)](cmmotionmanager/startgyroupdates(to:withhandler:).md)
  Starts gyroscope updates on an operation queue and with a specified handler.
- [func stopGyroUpdates()](cmmotionmanager/stopgyroupdates.md)
  Stops gyroscope updates.
- [var gyroData: CMGyroData?](cmmotionmanager/gyrodata.md)
  The latest sample of gyroscope data.
- [typealias CMGyroHandler](cmgyrohandler.md)
  The type of block callback for handling gyroscope data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/startgyroupdates())*