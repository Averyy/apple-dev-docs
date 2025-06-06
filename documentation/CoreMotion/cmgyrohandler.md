# CMGyroHandler

**Framework**: Core Motion  
**Kind**: typealias

The type of block callback for handling gyroscope data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias CMGyroHandler = (CMGyroData?, (any Error)?) -> Void
```

#### Discussion

Blocks of type `CMGyroHandler` are called when there is gyroscope data to process. You pass the block into [`startGyroUpdates(to:withHandler:)`](cmmotionmanager/startgyroupdates(to:withhandler:).md) as the second argument. Blocks of this type return no value but take two arguments:

## See Also

- [var gyroUpdateInterval: TimeInterval](cmmotionmanager/gyroupdateinterval.md)
  The interval, in seconds, for providing gyroscope updates to the block handler.
- [func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)](cmmotionmanager/startgyroupdates(to:withhandler:).md)
  Starts gyroscope updates on an operation queue and with a specified handler.
- [func startGyroUpdates()](cmmotionmanager/startgyroupdates.md)
  Starts gyroscope updates without a handler.
- [func stopGyroUpdates()](cmmotionmanager/stopgyroupdates.md)
  Stops gyroscope updates.
- [var gyroData: CMGyroData?](cmmotionmanager/gyrodata.md)
  The latest sample of gyroscope data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmgyrohandler)*