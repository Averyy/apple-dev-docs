# Measurement

**Framework**: Foundation  
**Kind**: struct

A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.

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
struct Measurement<UnitType> where UnitType : Unit
```

#### Overview

A [`Measurement`](measurement.md) object represents a quantity and unit of measure. The [`Measurement`](measurement.md) type provides a programmatic interface to converting measurements into different units, as well as calculating the sum or difference between two measurements.

[`Measurement`](measurement.md) objects are initialized with a [`Unit`](unit.md) object and double value. [`Measurement`](measurement.md) objects are immutable, and cannot be changed after being created.

Measurements support a large set of operators, including `+`, `-`, `*`, `/`, and a full set of comparison operators.

## Topics

### Creating a Measurement
- [init(value: Double, unit: UnitType)](measurement/init(value:unit:).md)
  Create a `Measurement` given a specified value and unit.
### Accessing the Value and Units
- [let unit: UnitType](measurement/unit.md)
  The unit component of the measurement.
- [var value: Double](measurement/value.md)
  The value component of the measurement.
### Converting to Other Units
- [func convert(to: UnitType)](measurement/convert(to:).md)
  Converts the measurement to the specified unit.
- [func converted(to: UnitType) -> Measurement<UnitType>](measurement/converted(to:).md)
  Returns a new measurement created by converting to the specified unit.
### Operating on a Measurement
- [static func * (Double, Measurement<UnitType>) -> Measurement<UnitType>](measurement/*(_:_:)-1d26c.md)
  Multiply a scalar value by a measurement.
- [static func * (Measurement<UnitType>, Double) -> Measurement<UnitType>](measurement/*(_:_:)-5tv8a.md)
  Multiply a measurement by a scalar value.
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
### Formatting a Measurement
- [func formatted() -> String](measurement/formatted.md)
  Generates a locale-aware string representation of a measurement using the default measurement format style.
- [func formatted<S>(S) -> S.FormatOutput](measurement/formatted(_:).md)
  Generates a locale-aware string representation of a measurement using the provided measurement format style.
- [Measurement.FormatStyle](measurement/formatstyle.md)
  A type that provides localized representations of measurements.
- [Measurement.AttributedStyle](measurement/attributedstyle.md)
  A type that provides localized representations of measurements with an attributed string.
### Comparing Measurements
- [static func > (Self, Self) -> Bool](measurement/_(_:_:)-648pf.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func >= (Self, Self) -> Bool](measurement/_=(_:_:)-lnsg.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func < <LeftHandSideType, RightHandSideType>(Measurement<LeftHandSideType>, Measurement<RightHandSideType>) -> Bool](measurement/_(_:_:)-7pou4.md)
  Compare two measurements of the same `Unit`.
- [static func <= (Self, Self) -> Bool](measurement/_=(_:_:)-12fhs.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
### Creating Ranges of Measurements
- [static func ... (Self) -> PartialRangeFrom<Self>](measurement/'...(_:)-378b4.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](measurement/'...(_:)-2o5x1.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](measurement/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func ..< (Self, Self) -> Range<Self>](measurement/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.
- [static func ..< (Self) -> PartialRangeUpTo<Self>](measurement/'.._(_:).md)
  Returns a partial range up to, but not including, its upper bound.
### Using Reference Types
- [class NSMeasurement](nsmeasurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
### Type Aliases
- [Measurement.Specification](measurement/specification.md)
- [Measurement.UnwrappedType](measurement/unwrappedtype.md)
- [Measurement.ValueType](measurement/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](measurement/defaultresolverspecification.md)
### Default Implementations
- [Comparable Implementations](measurement/comparable-implementations.md)
- [Equatable Implementations](measurement/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSMeasurement](nsmeasurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class Unit](unit.md)
  An abstract class representing a unit of measure.
- [class Dimension](dimension.md)
  An abstract class representing a dimensional unit of measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement)*