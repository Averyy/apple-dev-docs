# LengthFormatter

**Framework**: Foundation  
**Kind**: class

A formatter that provides localized descriptions of linear distances, such as length and height measurements.

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
class LengthFormatter
```

#### Overview

> **Note**:  As of iOS 10, macOS 10.12, tvOS 10, and watchOS 3, Foundation provides the [`MeasurementFormatter`](measurementformatter.md) class, which can be used to represent quantities of [`UnitLength`](unitlength.md) to provide equivalent functionality to [`LengthFormatter`](lengthformatter.md). You are encouraged to transition to these new Foundation Units and Measurements APIs whenever possible.

## Topics

### Formatting Length Strings
- [var isForPersonHeightUse: Bool](lengthformatter/isforpersonheightuse.md)
  A Boolean value that indicates whether the resulting string represents a person’s height.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, errorDescription: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](lengthformatter/getobjectvalue(_:for:errordescription:).md)
  This method is not supported for the `NSLengthFormatter` class.
- [var numberFormatter: NumberFormatter!](lengthformatter/numberformatter.md)
  The number formatter used to format the numbers in length strings.
- [func string(fromMeters: Double) -> String](lengthformatter/string(frommeters:).md)
  Returns a length string for the provided value.
- [func string(fromValue: Double, unit: LengthFormatter.Unit) -> String](lengthformatter/string(fromvalue:unit:).md)
  Returns a properly formatted length string for the given value and unit.
- [func unitString(fromMeters: Double, usedUnit: UnsafeMutablePointer<LengthFormatter.Unit>?) -> String](lengthformatter/unitstring(frommeters:usedunit:).md)
  Returns the unit string for the provided value.
- [func unitString(fromValue: Double, unit: LengthFormatter.Unit) -> String](lengthformatter/unitstring(fromvalue:unit:).md)
  Returns the unit string based on the provided value and unit.
- [var unitStyle: Formatter.UnitStyle](lengthformatter/unitstyle.md)
  The unit style used by this formatter.
### Constants
- [LengthFormatter.Unit](lengthformatter/unit.md)
  The units supported by the `NSLengthFormatter` class.

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

- [class MassFormatter](massformatter.md)
  A formatter that provides localized descriptions of mass and weight values.
- [class EnergyFormatter](energyformatter.md)
  A formatter that provides localized descriptions of energy values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/lengthformatter)*