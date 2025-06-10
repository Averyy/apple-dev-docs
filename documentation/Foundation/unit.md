# Unit

**Framework**: Foundation  
**Kind**: class

An abstract class representing a unit of measure.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class Unit
```

#### Overview

Each instance of an [`Unit`](unit.md) subclass consists of a [`symbol`](unit/symbol.md), which can be used to create string representations of [`NSMeasurement`](nsmeasurement.md) objects with the [`MeasurementFormatter`](measurementformatter.md) class.

The [`Dimension`](dimension.md) subclass is an abstract class that represents a dimensional unit, which can be converted into different units of the same type. The Foundation framework provides several concrete [`Dimension`](dimension.md) subclasses to represent the most common physical quantities, including mass, length, duration, and speed.

##### Subclassing Notes

[`Unit`](unit.md) is intended for subclassing. For dimensional units, you should use one of the Apple provided [`Dimension`](dimension.md) subclasses listed in Table 1 of [`Dimension`](dimension.md), or create a custom subclass of [`Dimension`](dimension.md). You can create a direct subclass of [`Unit`](unit.md) to represent a custom dimensionless unit, such as a count, score, or ratio.

## Topics

### Accessing Properties
- [var symbol: String](unit/symbol.md)
  The symbolic representation of the unit.
### Creating Units
- [init(symbol: String)](unit/init(symbol:).md)
  Initializes a new unit with the specified symbol.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [Dimension](dimension.md)
- [UnitEnergy.EnergyKit](unitenergy/energykit.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Measurement](measurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class NSMeasurement](nsmeasurement.md)
  A numeric quantity labeled with a unit of measure, with support for unit conversion and unit-aware calculations.
- [class Dimension](dimension.md)
  An abstract class representing a dimensional unit of measure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unit)*