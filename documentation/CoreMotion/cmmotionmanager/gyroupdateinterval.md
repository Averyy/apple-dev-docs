# gyroUpdateInterval

**Framework**: Core Motion  
**Kind**: property

The interval, in seconds, for providing gyroscope updates to the block handler.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var gyroUpdateInterval: TimeInterval { get set }
```

## Mentions

- [Getting raw gyroscope events](getting-raw-gyroscope-events.md)

#### Discussion

The system supplies gyroscope (that is, rotation rate) updates to the block handler specified in [`startGyroUpdates(to:withHandler:)`](cmmotionmanager/startgyroupdates(to:withhandler:).md) at regular intervals determined by the value of this property. The interval units are in seconds. The value of this property is capped to minimum and maximum values; the maximum value is determined by the maximum frequency supported by the hardware. If your app is sensitive to the intervals of gyroscope data, it should always check the timestamps of the delivered [`CMGyroData`](cmgyrodata.md) instances to determine the true update interval.

## See Also

- [func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)](cmmotionmanager/startgyroupdates(to:withhandler:).md)
  Starts gyroscope updates on an operation queue and with a specified handler.
- [func startGyroUpdates()](cmmotionmanager/startgyroupdates.md)
  Starts gyroscope updates without a handler.
- [func stopGyroUpdates()](cmmotionmanager/stopgyroupdates.md)
  Stops gyroscope updates.
- [var gyroData: CMGyroData?](cmmotionmanager/gyrodata.md)
  The latest sample of gyroscope data.
- [typealias CMGyroHandler](cmgyrohandler.md)
  The type of block callback for handling gyroscope data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyroupdateinterval)*