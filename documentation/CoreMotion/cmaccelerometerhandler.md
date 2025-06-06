# CMAccelerometerHandler

**Framework**: Core Motion  
**Kind**: typealias

The type of block callback for handling accelerometer data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias CMAccelerometerHandler = (CMAccelerometerData?, (any Error)?) -> Void
```

#### Discussion

Blocks of type `CMAccelerometerHandler` are called when there is accelerometer data to process. You pass the block into [`startAccelerometerUpdates(to:withHandler:)`](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md) as the second argument. Blocks of this type return no value but take two arguments:

## See Also

- [var accelerometerUpdateInterval: TimeInterval](cmmotionmanager/accelerometerupdateinterval.md)
  The interval, in seconds, for providing accelerometer updates to the block handler.
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](cmmotionmanager/startaccelerometerupdates.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](cmmotionmanager/stopaccelerometerupdates.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](cmmotionmanager/accelerometerdata.md)
  The latest sample of accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)*