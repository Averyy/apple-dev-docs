# stopGyroUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Stops gyroscope updates.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stopGyroUpdates()
```

```objc
- (void) stopGyroUpdates;
```

## See Also

### Managing Gyroscope Updates
- [var gyroUpdateInterval: TimeInterval](./gyroupdateinterval.md)
  The interval, in seconds, for providing gyroscope updates to the block handler.
- [func startGyroUpdates(to: OperationQueue, withHandler: CMGyroHandler)](./startgyroupdates%28to,withhandler%29.md)
  Starts gyroscope updates on an operation queue and with a specified handler.
- [func startGyroUpdates()](./startgyroupdates%28%29.md)
  Starts gyroscope updates without a handler.
- [var gyroData: CMGyroData?](./gyrodata.md)
  The latest sample of gyroscope data.
- [typealias CMGyroHandler](../cmgyrohandler.md)
  The type of block callback for handling gyroscope data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopgyroupdates())*