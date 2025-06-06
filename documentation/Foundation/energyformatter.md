# EnergyFormatter

**Framework**: Foundation  
**Kind**: class

A formatter that provides localized descriptions of energy values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EnergyFormatter
```

#### Overview

> **Note**:  As of iOS 10, macOS 10.12, tvOS 10, and watchOS 3, Foundation provides the [`MeasurementFormatter`](measurementformatter.md) class, which can be used to represent quantities of [`UnitEnergy`](unitenergy.md) to provide equivalent functionality to [`EnergyFormatter`](energyformatter.md). You are encouraged to transition to these new Foundation Units and Measurements APIs whenever possible.

 As of iOS 10, macOS 10.12, tvOS 10, and watchOS 3, Foundation provides the [`MeasurementFormatter`](measurementformatter.md) class, which can be used to represent quantities of [`UnitEnergy`](unitenergy.md) to provide equivalent functionality to [`EnergyFormatter`](energyformatter.md). You are encouraged to transition to these new Foundation Units and Measurements APIs whenever possible.

## Topics

### Formatting Energy Strings
- [var isForFoodEnergyUse: Bool](energyformatter/isforfoodenergyuse.md)
  A Boolean value that indicates whether the energy value is used to measure food energy.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](energyformatter/getobjectvalue(_:for:errordescription:).md)
  This method is not supported for the `NSEnergyFormatter` class.
- [var numberFormatter: NumberFormatter!](energyformatter/numberformatter.md)
  The number formatter used to format the numbers in energy strings.
- [func string(fromJoules: Double) -> String](energyformatter/string(fromjoules:).md)
  Returns an energy string for the provided value.
- [func string(fromValue: Double, unit: EnergyFormatter.Unit) -> String](energyformatter/string(fromvalue:unit:).md)
  Returns a properly formatted energy string for the given value and unit.
- [func unitString(fromJoules: Double, usedUnit: UnsafeMutablePointer<EnergyFormatter.Unit>?) -> String](energyformatter/unitstring(fromjoules:usedunit:).md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: EnergyFormatter.Unit) -> String](energyformatter/unitstring(fromvalue:unit:).md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](energyformatter/unitstyle.md)
  The unit style used by this formatter.
### Constants
- [EnergyFormatter.Unit](energyformatter/unit.md)
  The units supported by the `NSEnergyFormatter` class.

## Relationships

### Inherits From
- [Formatter](formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class LengthFormatter](lengthformatter.md)
  A formatter that provides localized descriptions of linear distances, such as length and height measurements.
- [class MassFormatter](massformatter.md)
  A formatter that provides localized descriptions of mass and weight values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/energyformatter)*