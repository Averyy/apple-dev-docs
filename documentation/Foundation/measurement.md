# Measurement

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

A [`Measurement`](./measurement.md) object represents a quantity and unit of measure. The [`Measurement`](./measurement.md) type provides a programmatic interface to converting measurements into different units, as well as calculating the sum or difference between two measurements.

[`Measurement`](./measurement.md) objects are initialized with a [`Unit`](./unit.md) object and double value. [`Measurement`](./measurement.md) objects are immutable, and cannot be changed after being created.

Measurements support a large set of operators, including `+`, `-`, `*`, `/`, and a full set of comparison operators.

## Topics

### Creating a Measurement
- [init(value: Double, unit: UnitType)](./measurement/init%28value,unit%29.md)
  Create a `Measurement` given a specified value and unit.
### Accessing the Value and Units
- [let unit: UnitType](./measurement/unit.md)
  The unit component of the measurement.
- [var value: Double](./measurement/value.md)
  The value component of the measurement.
### Converting to Other Units
- [func convert(to: UnitType)](./measurement/convert%28to%29.md)
  Converts the measurement to the specified unit.
- [func converted(to: UnitType) -> Measurement<UnitType>](./measurement/converted%28to%29.md)
  Returns a new measurement created by converting to the specified unit.
### Operating on a Measurement
- [static func * (Double, Measurement<UnitType>) -> Measurement<UnitType>](./measurement/star%28_,_%29-1d26c.md)
  Multiply a scalar value by a measurement.
- [static func * (Measurement<UnitType>, Double) -> Measurement<UnitType>](./measurement/star%28_,_%29-5tv8a.md)
  Multiply a measurement by a scalar value.
- [static func + (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](./measurement/plus%28_,_%29-9lejn.md)
  Add two measurements.
- [static func + (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](./measurement/plus%28_,_%29-4fsbl.md)
  Adds two measurements of the same dimension.
- [static func - (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](./measurement/minus%28_,_%29-2nnoy.md)
  Subtract two measurements of the same Unit.
- [static func - (Measurement<UnitType>, Measurement<UnitType>) -> Measurement<UnitType>](./measurement/minus%28_,_%29-1a47h.md)
  Subtract two measurements of the same Dimension.
- [static func / (Double, Measurement<UnitType>) -> Measurement<UnitType>](./measurement/op%28_,_%29-98s40.md)
  Divide a scalar value by a measurement.
- [static func / (Measurement<UnitType>, Double) -> Measurement<UnitType>](./measurement/op%28_,_%29-71kwk.md)
  Divide a measurement by a scalar value.
### Formatting a Measurement
- [func formatted() -> String](./measurement/formatted%28%29.md)
  Generates a locale-aware string representation of a measurement using the default measurement format style.
- [func formatted<S>(S) -> S.FormatOutput](./measurement/formatted%28_%29.md)
  Generates a locale-aware string representation of a measurement using the provided measurement format style.
- [Measurement.FormatStyle](./measurement/formatstyle.md)
  A type that provides localized representations of measurements.
- [Measurement.AttributedStyle](./measurement/attributedstyle.md)
  A type that provides localized representations of measurements with an attributed string.
### Comparing Measurements
- [static func < <LeftHandSideType, RightHandSideType>(Measurement<LeftHandSideType>, Measurement<RightHandSideType>) -> Bool](./measurement/op%28_,_%29-7pou4.md)
  Compare two measurements of the same `Unit`.
### Using Reference Types
- [class NSMeasurement](./nsmeasurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
### Type Aliases
- [Measurement.Specification](./measurement/specification.md)
- [Measurement.UnwrappedType](./measurement/unwrappedtype.md)
- [Measurement.ValueType](./measurement/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](./measurement/defaultresolverspecification.md)
### Default Implementations
- [Comparable Implementations](./measurement/comparable-implementations.md)
- [Equatable Implementations](./measurement/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [ElectricityInsightMeasure](../EnergyKit/electricityinsightmeasure.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [ReferenceConvertible](./referenceconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [class NSMeasurement](./nsmeasurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class Unit](./unit.md)
  An abstract class representing a unit of measure.
- [class Dimension](./dimension.md)
  An abstract class representing a dimensional unit of measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement)*