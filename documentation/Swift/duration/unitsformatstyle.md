# Duration.UnitsFormatStyle

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A format style that shows durations with localized labeled components

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct UnitsFormatStyle
```

## Overview

This style produces formatted strings that break out a duration’s individual components, like “2 min, 3 sec”.

Create a `UnitsFormatStyle` by providing a set of allowed [`Duration.UnitsFormatStyle.Unit`](./unitsformatstyle/unit.md) instances — such as hours, minutes, or seconds — for formatted strings to include. You also specify a width for displaying these units, which controls whether they appear as full words (“minutes”) or abbreviations (“min”). The initializers also take optional parameters to control things like the handling of zero units and fractional parts. Then create a formatted string by calling [`formatted(_:)`](./formatted%28_%29.md) on a duration, passing the style, or [`format(_:)`](./unitsformatstyle/format%28_%29.md) on the style, passing a duration. You can also use the style’s [`attributed`](./timeformatstyle/attributed-swift.property.md) property to create a style that produces [`AttributedString`](../../Foundation/attributedstring.md) instances, which contains attributes that indicate the unit value of formatted runs of the string.

In situations that expect a [`Duration.UnitsFormatStyle`](./unitsformatstyle.md), such as [`formatted(_:)`](./formatted%28_%29.md), you can use the convenience function `.units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)` to create a [`Duration.UnitsFormatStyle`](./unitsformatstyle.md), rather than using the full initializer.

If you want to reuse a style to format many durations, call [`format(_:)`](./unitsformatstyle/format%28_%29.md) on the style, passing in a new duration each time.

The following example creates `duration` to represent 1 hour, 10 minutes, 32 seconds, and 400 milliseconds. It then creates a [`Duration.UnitsFormatStyle`](./unitsformatstyle.md) to show the hours, minutes, seconds, and milliseconds parts, with a wide width that presents the full name of each unit.

```swift
let duration = Duration.seconds(70 * 60 + 32) + Duration.milliseconds(400)
let format = duration1.formatted(
     .units(allowed: [.hours, .minutes, .seconds, .milliseconds],
            width: .wide))
// format == "1 hour, 10 minutes, 32 seconds, 400 milliseconds"
```

The formatted string omits any units that aren’t needed to accurately represent the value. In the above example, a duration of exactly one minute would format as `1 minute`, omitting the hours, seconds, and milliseconds parts. To override this behavior and show the omitted units, use the initializer’s’ `zeroValueUnits` parameter.

## Topics

### Creating a units format style
- [init(allowedUnits: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLength: Int?, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy)](./unitsformatstyle/init%28allowedunits,width,maximumunitcount,zerovalueunits,valuelength,fractionalpart%29.md)
  Creates a units format style using the given parameters.
- [init<ValueRange>(allowedUnits: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLengthLimits: ValueRange, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy)](./unitsformatstyle/init%28allowedunits,width,maximumunitcount,zerovalueunits,valuelengthlimits,fractionalpart%29.md)
  Creates a units format style using the given parameters.
### Formatting a duration
- [func format(Duration) -> String](./unitsformatstyle/format%28_%29.md)
  Creates a locale-aware string representation from a duration value.
### Formatting a duration as an attributed string
- [var attributed: Duration.UnitsFormatStyle.Attributed](./unitsformatstyle/attributed-swift.property.md)
  A property that formats the duration as an attributed string.
- [Duration.UnitsFormatStyle.Attributed](./unitsformatstyle/attributed-swift.struct.md)
  A format style that formats durations as attributed strings.
### Working with units
- [var allowedUnits: Set<Duration.UnitsFormatStyle.Unit>](./unitsformatstyle/allowedunits.md)
  The units that may be included in the output string.
- [Duration.UnitsFormatStyle.Unit](./unitsformatstyle/unit.md)
  A unit to use in formatting a duration.
- [var maximumUnitCount: Int?](./unitsformatstyle/maximumunitcount.md)
  The maximum number of time units to include in the output string.
- [var valueLengthLimits: Range<Int>?](./unitsformatstyle/valuelengthlimits.md)
  The padding or truncating behavior of the unit value.
### Working with unit widths
- [var unitWidth: Duration.UnitsFormatStyle.UnitWidth](./unitsformatstyle/unitwidth-swift.property.md)
  The width of the unit and the spacing between the value and the unit.
- [Duration.UnitsFormatStyle.UnitWidth](./unitsformatstyle/unitwidth-swift.struct.md)
  The width of a unit to use in formatting a duration.
### Working with zero values
- [var zeroValueUnitsDisplay: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy](./unitsformatstyle/zerovalueunitsdisplay.md)
  The strategy for how zero-value units are handled.
- [Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy](./unitsformatstyle/zerovalueunitsdisplaystrategy.md)
  A strategy that determines how to format a unit whose value is zero.
### Working with fractional values
- [var fractionalPartDisplay: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](./unitsformatstyle/fractionalpartdisplay.md)
  The strategy for displaying a duration if it cannot be represented exactly with the allowed units.
- [Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](./unitsformatstyle/fractionalpartdisplaystrategy.md)
  A strategy that determines how to format the fractional part of a duration if the allowed units can’t represent it exactly.
### Working with locales
- [var locale: Locale](./unitsformatstyle/locale.md)
  The locale to use when formatting the duration.
- [func locale(Locale) -> Duration.UnitsFormatStyle](./unitsformatstyle/locale%28_%29.md)
  A modifier to set the locale of the format style.

## Relationships

### Conforms To
- [Copyable](../copyable.md)
- [Decodable](../decodable.md)
- [DiscreteFormatStyle](../../Foundation/discreteformatstyle.md)
- [Encodable](../encodable.md)
- [Equatable](../equatable.md)
- [Escapable](../escapable.md)
- [FormatStyle](../../Foundation/formatstyle.md)
- [Hashable](../hashable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### Formatting a duration
- [func formatted() -> String](./formatted%28%29.md)
  Formats the string using a localized hour-minute-second time pattern.
- [func formatted<S>(S) -> S.FormatOutput](./formatted%28_%29.md)
  Formats the duration, using the provided format style.
- [Duration.TimeFormatStyle](./timeformatstyle.md)
  A format style that shows durations in a compact, localized format with separators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle)*