# UnitConverter

**Framework**: Foundation  
**Kind**: class

An abstract class that provides a description of how to convert a unit to and from the base unit of its dimension.

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
class UnitConverter
```

#### Overview

For units that can be converted by a scale factor or linear equation, use the concrete subclass [`UnitConverterLinear`](unitconverterlinear.md).

##### Subclassing Notes

[`UnitConverter`](unitconverter.md) is an abstract class that is intended for subclassing. You can implement your own subclass of [`UnitConverter`](unitconverter.md) to convert between units according to any desired mapping function. For example, units may be converted using a logarithmic, exponential, or quantile scale.

###### Methods to Override

All subclasses must fully implement the following methods:

- [`baseUnitValue(fromValue:)`](unitconverter/baseunitvalue(fromvalue:).md)
- [`value(fromBaseUnitValue:)`](unitconverter/value(frombaseunitvalue:).md)

###### Alternatives to Subclassing

As stated above, most physical units can be converted using a linear equation with [`UnitConverterLinear`](unitconverterlinear.md). You should only create a custom subclass of [`UnitConverter`](unitconverter.md) for units that cannot be converted in this way.

## Topics

### Converting Between Units
- [func baseUnitValue(fromValue: Double) -> Double](unitconverter/baseunitvalue(fromvalue:).md)
  For a given unit, returns the specified value of that unit in terms of the base unit of its dimension.
- [func value(fromBaseUnitValue: Double) -> Double](unitconverter/value(frombaseunitvalue:).md)
  For a given unit, returns the specified value of the base unit in terms of that unit.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UnitConverterLinear](unitconverterlinear.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UnitConverterLinear](unitconverterlinear.md)
  A description of how to convert between units using a linear equation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitconverter)*