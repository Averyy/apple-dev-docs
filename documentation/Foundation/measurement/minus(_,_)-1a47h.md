# -(_:_:)

**Framework**: Foundation  
**Kind**: op  
**Role**: Operator

Subtract two measurements of the same Dimension.

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
static func - (lhs: Measurement<UnitType>, rhs: Measurement<UnitType>) -> Measurement<UnitType>
```

Available when `UnitType` inherits `Dimension`.

#### Return Value

The result of adding the two measurements.

#### Discussion

If the `unit` of the `lhs` and `rhs` are `==`, then this returns the result of subtracting the `value` of each `Measurement`. If they are not equal, then this will convert both to the base unit of the `Dimension` and return the result as a `Measurement` of that base unit.

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
- [static func / (Double, Measurement<UnitType>) -> Measurement<UnitType>](./op%28_,_%29-98s40.md)
  Divide a scalar value by a measurement.
- [static func / (Measurement<UnitType>, Double) -> Measurement<UnitType>](./op%28_,_%29-71kwk.md)
  Divide a measurement by a scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/-(_:_:)-1a47h)*