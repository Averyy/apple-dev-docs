# rotationRate

**Framework**: Core Motion  
**Kind**: property

The rotation rate of the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var rotationRate: CMRotationRate { get }
```

#### Discussion

A [`CMRotationRate`](cmrotationrate.md) structure contains data specifying the device’s rate of rotation around three axes. The value of this property contains a measurement of gyroscope data whose bias has been removed by Core Motion algorithms. The identically name property of [`CMGyroData`](cmgyrodata.md), on the other hand, gives the raw data from the gyroscope. The structure type is declared in `CMGyroData.h`.

## See Also

- [var attitude: CMAttitude](cmdevicemotion/attitude.md)
  The attitude of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotion/rotationrate)*