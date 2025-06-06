# stopAccelerometerUpdates()

**Framework**: Core Motion  
**Kind**: method

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

## See Also

- [var accelerometerUpdateInterval: TimeInterval](cmmotionmanager/accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](cmmotionmanager/startaccelerometerupdates.md)
  Starts accelerometer updates without a handler.
- [var accelerometerData: CMAccelerometerData?](cmmotionmanager/accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/stopaccelerometerupdates())*