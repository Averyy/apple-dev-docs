# stopAccelerometerUpdates()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Stops accelerometer updates.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stopAccelerometerUpdates()
```

```objc
- (void) stopAccelerometerUpdates;
```

## See Also

### Managing Accelerometer Updates
- [var accelerometerUpdateInterval: TimeInterval](./accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](./startaccelerometerupdates%28to,withhandler%29.md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](./startaccelerometerupdates%28%29.md)
  Starts accelerometer updates without a handler.
- [var accelerometerData: CMAccelerometerData?](./accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](../cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())*