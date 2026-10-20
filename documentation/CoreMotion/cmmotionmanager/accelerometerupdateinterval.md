# accelerometerUpdateInterval

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) NSTimeInterval accelerometerUpdateInterval;
```

## Mentions

- [Getting raw accelerometer events](../getting-raw-accelerometer-events.md)

#### Discussion

The system supplies accelerometer updates to the block handler specified in [`startAccelerometerUpdates(to:withHandler:)`](./startaccelerometerupdates%28to,withhandler%29.md) at regular intervals determined by the value of this property. The interval units are in seconds. The value of this property is capped to minimum and maximum values; the maximum value is determined by the maximum frequency supported by the hardware. If your app is sensitive to the intervals of acceleration data, it should always check the timestamps of the delivered [`CMAccelerometerData`](../cmaccelerometerdata.md) instances to determine the true update interval.

## See Also

### Related Documentation
- [Event Handling Guide for UIKit Apps](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html?language=swift#//apple_ref/doc/uid/TP40009541)
### Managing Accelerometer Updates
- [func startAccelerometerUpdates(to: OperationQueue, withHandler: CMAccelerometerHandler)](./startaccelerometerupdates%28to,withhandler%29.md)
  Starts accelerometer updates on an operation queue and with a specified handler.
- [func startAccelerometerUpdates()](./startaccelerometerupdates%28%29.md)
  Starts accelerometer updates without a handler.
- [func stopAccelerometerUpdates()](./stopaccelerometerupdates%28%29.md)
  Stops accelerometer updates.
- [var accelerometerData: CMAccelerometerData?](./accelerometerdata.md)
  The latest sample of accelerometer data.
- [typealias CMAccelerometerHandler](../cmaccelerometerhandler.md)
  The type of block callback for handling accelerometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/accelerometerupdateinterval)*