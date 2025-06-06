# accelerometerUpdateInterval

**Framework**: Core Motion  
**Kind**: property

The interval, in seconds, for providing accelerometer updates to the block handler.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var accelerometerUpdateInterval: TimeInterval { get set }
```

## Mentions

- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)

#### Discussion

The system supplies accelerometer updates to the block handler specified in [`startAccelerometerUpdates(to:withHandler:)`](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md) at regular intervals determined by the value of this property. The interval units are in seconds. The value of this property is capped to minimum and maximum values; the maximum value is determined by the maximum frequency supported by the hardware. If your app is sensitive to the intervals of acceleration data, it should always check the timestamps of the delivered [`CMAccelerometerData`](cmaccelerometerdata.md) instances to determine the true update interval.

## See Also

- [Event Handling Guide for UIKit Apps](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html?language=swift#//apple_ref/doc/uid/TP40009541)
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](cmmotionmanager/startaccelerometerupdates(to:withhandler:).md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](cmmotionmanager/startaccelerometerupdates.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](cmmotionmanager/stopaccelerometerupdates.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](cmmotionmanager/accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)*