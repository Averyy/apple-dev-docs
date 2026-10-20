# magnetometerUpdateInterval

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The interval, in seconds, at which the system delivers magnetometer data to the block handler.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
var magnetometerUpdateInterval: TimeInterval { get set }
```

```objc
@property (nonatomic, assign) NSTimeInterval magnetometerUpdateInterval;
```

#### Discussion

The supplies magnetometer data to the block handler specified in [`startMagnetometerUpdates(to:withHandler:)`](./startmagnetometerupdates%28to,withhandler%29.md) at regular intervals determined by the value of this property. The interval unit are in seconds. The value of this property is capped to minimum and maximum values; the maximum value is determined by the maximum frequency supported by the hardware. If your app is sensitive to the intervals of magnetometer data, it should always check the timestamps of the delivered [`CMMagnetometerData`](../cmmagnetometerdata.md) instances to determine the true update interval.

## See Also

### Managing Magnetometer Updates
- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](./startmagnetometerupdates%28to,withhandler%29.md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func startMagnetometerUpdates()](./startmagnetometerupdates%28%29.md)
  Starts magnetometer updates without a block handler.
- [func stopMagnetometerUpdates()](./stopmagnetometerupdates%28%29.md)
  Stops magnetometer updates.
- [var magnetometerData: CMMagnetometerData?](./magnetometerdata.md)
  The latest sample of magnetometer data.
- [typealias CMMagnetometerHandler](../cmmagnetometerhandler.md)
  The type of block callback for handling magnetometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval)*