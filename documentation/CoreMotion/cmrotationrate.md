# CMRotationRate

**Framework**: Core Motion  
**Kind**: struct

The type of structures representing a measurement of rotation rate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CMRotationRate
```

## Topics

### Getting the Rotation Rates
- [var x: Double](cmrotationrate/x.md)
  The value for the X-axis.
- [var y: Double](cmrotationrate/y.md)
  The value for the Y-axis.
- [var z: Double](cmrotationrate/z.md)
  The value for the Z-axis.
### Initializers
- [init()](cmrotationrate/init.md)
- [init(x: Double, y: Double, z: Double)](cmrotationrate/init(x:y:z:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var rotationRate: CMRotationRate](cmgyrodata/rotationrate.md)
  The rotation rate as measured by the device’s gyroscope.
- [class CMRotationRateData](cmrotationratedata.md)
  A data object that contains a single rotation-rate measurement.
- [class CMRecordedRotationRateData](cmrecordedrotationratedata.md)
  A data object that contains a single rotation-rate measurement at a specific time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrotationrate)*