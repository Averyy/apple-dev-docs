# gyroData

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The latest sample of gyroscope data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var gyroData: CMGyroData? { get }
```

```objc
@property (readonly, nullable) CMGyroData * gyroData;
```

## Mentions

- [Getting raw gyroscope events](../getting-raw-gyroscope-events.md)

## Discussion

If no gyroscope data is available, the value of this property is `nil`. An app that is receiving gyroscope data after calling [`startGyroUpdates()`](./startgyroupdates%28%29.md) periodically checks the value of this property and processes the gyroscope data.

## See Also

### Managing Gyroscope Updates
- [var gyroUpdateInterval: TimeInterval](./gyroupdateinterval.md)
  The interval, in seconds, for providing gyroscope updates to the block handler.
- [func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)](./startgyroupdates%28to,withhandler%29.md)
  Starts gyroscope updates on an operation queue and with a specified handler.
- [func startGyroUpdates()](./startgyroupdates%28%29.md)
  Starts gyroscope updates without a handler.
- [func stopGyroUpdates()](./stopgyroupdates%28%29.md)
  Stops gyroscope updates.
- [typealias CMGyroHandler](../cmgyrohandler.md)
  The type of block callback for handling gyroscope data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/gyrodata)*