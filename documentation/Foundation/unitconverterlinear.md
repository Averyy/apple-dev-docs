# UnitConverterLinear

**Framework**: Foundation  
**Kind**: class

A description of how to convert between units using a linear equation.

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
class UnitConverterLinear
```

#### Overview

A linear equation for unit conversion takes the form `y = mx + b`, such that the following is true:

- `y` is the value in terms of the base unit of the dimension.
- `m` is the known coefficient to use for this unit’s conversion.
- `x` is the value in terms of the unit on which you call this method.
- `b` is the known constant to use for this unit’s conversion.

The `baseUnitValueFromValue:` method performs the conversion in the form of `y = mx + b`, where `x` represents the value passed in and `y` represents the value returned. The `valueFromBaseUnitValue:` method performs the inverse conversion in the form of `x = (y - b) / m`, where `y` represents the value passed in and `x` represents the value returned.

For example, consider the [`fahrenheit`](unittemperature/fahrenheit.md) unit that [`UnitTemperature`](unittemperature.md) defines. The [`baseUnitValue(fromValue:)`](unitconverter/baseunitvalue(fromvalue:).md) method calculates the value in the base unit, [`kelvin`](unittemperature/kelvin.md), using the formula `K = (0.55555555555556) × °F + 255.37222222222427`. The [`value(fromBaseUnitValue:)`](unitconverter/value(frombaseunitvalue:).md) method calculates the value in [`fahrenheit`](unittemperature/fahrenheit.md) using the formula `°F = (K — 255.37222222222427) / (0.55555555555556)`, where the [`coefficient`](unitconverterlinear/coefficient.md) is `(0.55555555555556)` and the [`constant`](unitconverterlinear/constant.md) is `255.37222222222427`.

**Swift**:

```swift
let kelvinToFahrenheit = UnitConverterLinear(coefficient: 0.55555555555556, constant: 255.37222222222427)
```

**Objective-C**:

```objc
NSUnitConverter *kelvinToFahrenheit = [[NSUnitConverterLinear alloc] initWithCoefficient:0.55555555555556 constant:255.37222222222427];
```

Units that perform conversion using only a scale factor have a [`coefficient`](unitconverterlinear/coefficient.md) equal to the scale factor and a [`constant`](unitconverterlinear/constant.md) equal to `0`. For example, consider the [`kilometers`](unitlength/kilometers.md) unit [`UnitLength`](unitlength.md) defines. The [`baseUnitValue(fromValue:)`](unitconverter/baseunitvalue(fromvalue:).md) method calculates the value in meters using the formula `valueInMeters = 1000 * valueInKilometers + 0`. The [`value(fromBaseUnitValue:)`](unitconverter/value(frombaseunitvalue:).md) calculates the value in kilometers using the formula `valueInKilometers = (valueInMeters - 0) / 1000`, where the coefficient is `1000` and the constant is `0`.

**Swift**:

```swift
let kilometersToMeters = UnitConverterLinear(coefficient: 1000.0, constant: 0.0)
```

**Objective-C**:

```objc
NSUnitConverterLinear *kilometersToMeters = [[NSUnitConverterLinear alloc] initWithCoefficient:1000.0 constant:0.0];
```

## Topics

### Accessing Linear Parameters
- [var coefficient: Double](unitconverterlinear/coefficient.md)
  The coefficient to use in the linear unit conversion calculation.
- [var constant: Double](unitconverterlinear/constant.md)
  The constant to use in the linear unit conversion calculation.
### Creating Unit Converters
- [convenience init(coefficient: Double)](unitconverterlinear/init(coefficient:).md)
  Initializes the unit converter with the coefficient you specify.
- [init(coefficient: Double, constant: Double)](unitconverterlinear/init(coefficient:constant:).md)
  Creates a unit converter with the coefficient and constant you specify.
### Initializers
- [init?(coder: NSCoder)](unitconverterlinear/init(coder:).md)

## Relationships

### Inherits From
- [UnitConverter](unitconverter.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class UnitConverter](unitconverter.md)
  An abstract class that provides a description of how to convert a unit to and from the base unit of its dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/unitconverterlinear)*