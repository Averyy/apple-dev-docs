# *(_:_:)

**Framework**: Foundation  
**Kind**: op

Multiply a measurement by a scalar value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
static func * (lhs: Measurement<UnitType>, rhs: Double) -> Measurement<UnitType>
```

#### Return Value

A measurement of value `lhs.value * rhs` with the same unit as `lhs`.

## Parameters

- `lhs`: A measurement to multiply.
- `rhs`: A double-precision floating-point number to multiply.

## See Also

- [static func * (Double, Measurement<UnitType>) -> Measurement<UnitType>](measurement/*(_:_:)-1d26c.md)
  Multiply a scalar value by a measurement.
- [static func + (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](measurement/+(_:_:)-9lejn.md)
  Add two measurements.
- [static func + (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](measurement/+(_:_:)-4fsbl.md)
  Adds two measurements of the same dimension.
- [static func - (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](measurement/-(_:_:)-2nnoy.md)
  Subtract two measurements of the same Unit.
- [static func - (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](measurement/-(_:_:)-1a47h.md)
  Subtract two measurements of the same Dimension.
- [static func / (Double, Measurement<UnitType>) -> Measurement<UnitType>](measurement/_(_:_:)-98s40.md)
  Divide a scalar value by a measurement.
- [static func / (Measurement<UnitType>, Double) -> Measurement<UnitType>](measurement/_(_:_:)-71kwk.md)
  Divide a measurement by a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/*(_:_:)-5tv8a)*