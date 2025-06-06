# magnetometerUpdateInterval

**Framework**: Core Motion  
**Kind**: property

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

#### Discussion

The supplies magnetometer data to the block handler specified in [`startMagnetometerUpdates(to:withHandler:)`](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md) at regular intervals determined by the value of this property. The interval unit are in seconds. The value of this property is capped to minimum and maximum values; the maximum value is determined by the maximum frequency supported by the hardware. If your app is sensitive to the intervals of magnetometer data, it should always check the timestamps of the delivered [`CMMagnetometerData`](cmmagnetometerdata.md) instances to determine the true update interval.

## See Also

- [func startMagnetometerUpdates(to: OperationQueue, withHandler: CMMagnetometerHandler)](cmmotionmanager/startmagnetometerupdates(to:withhandler:).md)
  Starts magnetometer updates on an operation queue and with a specified handler.
- [func startMagnetometerUpdates()](cmmotionmanager/startmagnetometerupdates.md)
  Starts magnetometer updates without a block handler.
- [func stopMagnetometerUpdates()](cmmotionmanager/stopmagnetometerupdates.md)
  Stops magnetometer updates.
- [var magnetometerData: CMMagnetometerData?](cmmotionmanager/magnetometerdata.md)
  The latest sample of magnetometer data.
- [typealias CMMagnetometerHandler](cmmagnetometerhandler.md)
  The type of block callback for handling magnetometer data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/magnetometerupdateinterval)*