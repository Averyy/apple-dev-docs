# CMMagneticField

**Framework**: Core Motion  
**Kind**: struct

A structure containing 3-axis magnetometer data

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CMMagneticField
```

## Topics

### Getting the Field Values
- [var x: Double](cmmagneticfield/x.md)
  X-axis magnetic field in microteslas.
- [var y: Double](cmmagneticfield/y.md)
  Y-axis magnetic field in microteslas.
- [var z: Double](cmmagneticfield/z.md)
  Z-axis magnetic field in microteslas.
### Initializers
- [init()](cmmagneticfield/init.md)
- [init(x: Double, y: Double, z: Double)](cmmagneticfield/init(x:y:z:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var magneticField: CMMagneticField](cmmagnetometerdata/magneticfield.md)
  Returns the magnetic field measured by the magnetometer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmagneticfield)*