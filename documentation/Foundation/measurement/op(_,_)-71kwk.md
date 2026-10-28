# /(_:_:)

**Framework**: Foundation  
**Kind**: op  
**Role**: Operator

Divide a measurement by a scalar value.

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
static func / (lhs: Measurement<UnitType>, rhs: Double) -> Measurement<UnitType>
```

Available when `UnitType` inherits `Unit`.

## Return Value

A measurement of value `lhs.value / rhs` with the same unit as `lhs`.

## Parameters

- `lhs`: A measurement to divide.
- `rhs`: A double-precision floating-point number to divide by.

## See Also

### Operating on a Measurement
- [static func * (Double, Measurement<UnitType>) -> Measurement<UnitType>](./star%28_,_%29-1d26c.md)
  Multiply a scalar value by a measurement.
- [static func * (Measurement<UnitType>, Double) -> Measurement<UnitType>](./star%28_,_%29-5tv8a.md)
  Multiply a measurement by a scalar value.
- [static func + (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](./plus%28_,_%29-9lejn.md)
  Add two measurements.
- [static func + (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](./plus%28_,_%29-4fsbl.md)
  Adds two measurements of the same dimension.
- [static func - (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](./minus%28_,_%29-2nnoy.md)
  Subtract two measurements of the same Unit.
- [static func - (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](./minus%28_,_%29-1a47h.md)
  Subtract two measurements of the same Dimension.
- [static func / (Double, Measurement<UnitType>) -> Measurement<UnitType>](./op%28_,_%29-98s40.md)
  Divide a scalar value by a measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/_(_:_:)-71kwk)*