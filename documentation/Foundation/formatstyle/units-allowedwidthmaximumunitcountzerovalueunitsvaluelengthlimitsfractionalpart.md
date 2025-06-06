# units(allowed:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)

**Framework**: Foundation  
**Kind**: method

Returns a style for formatting a duration range that uses the specified units, with padding/truncating behavior defined as a range.

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
static func units<ValueRange>(allowed units: Set<Duration.UnitsFormatStyle.Unit> = [.hours, .minutes, .seconds], width: Duration.UnitsFormatStyle.UnitWidth = .abbreviated, maximumUnitCount: Int? = nil, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy = .hide, valueLengthLimits: ValueRange, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy = .hide) -> Self where ValueRange : RangeExpression, ValueRange.Bound == Int
```

#### Return Value

A duration units format style that uses the specified units.

#### Discussion

Use the dot-notation form of this method when the call point allows the use of [`Duration.UnitsFormatStyle`](https://developer.apple.com/documentation/Swift/Duration/UnitsFormatStyle). You typically do this when calling the [`formatted(_:)`](https://developer.apple.com/documentation/Swift/Duration/formatted(_:)) method of [`Duration`](https://developer.apple.com/documentation/Swift/Duration).

The following example creates a duration to represent 1 hour, 10 minutes, 32 seconds, and 400 milliseconds. It then creates a [`Duration.UnitsFormatStyle`](https://developer.apple.com/documentation/Swift/Duration/UnitsFormatStyle) to show the hours, minutes, seconds, and milliseconds parts. Because `valueLengthLimits` is the range `2...3`, the style formats each unit with a minimum of two digits and a maximum of three. This results in zero-padding the hours part as `01 hr`.

```swift
let duration = Duration.seconds(70 * 60 + 32) + Duration.milliseconds(400)
let formatted = duration.formatted(
    .units(
        allowed: [.hours, .minutes, .seconds, .milliseconds],
        valueLengthLimits: 2...3))
// "01 hr, 10 min, 32 sec, 400 ms"
```

## Parameters

- `units`: The units that the formatted string may include.
- `width`: The width of the unit and the spacing between the value and the unit.
- `maximumUnitCount`: The maximum number of duration units, if any, to include in the output string.
- `zeroValueUnits`: The strategy for handling leading units with zero values.
- `valueLengthLimits`: The padding and truncating behavior of the unit value, as a bounded range of   values. The lower bound, if any, expresses the minimum number of digits for all units. The higher bound, if any, expresses the maximum. The style applies leading zeros to units with less than the minimum number of digits, and truncates units above the maximum digits. Defaults to  , which applies no minimum or maximum.
- `fractionalPart`: The strategy for displaying a duration if a formatted string can’t represent it exactly with the allowed units.

## See Also

- [static var timeDuration: Date.ComponentsFormatStyle](formatstyle/timeduration.md)
  A style for formatting a duration expressed as a range of dates.
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.
- [static func time(pattern: Duration.TimeFormatStyle.Pattern) -> Self](formatstyle/time(pattern:).md)
  Returns a style for formatting a duration using a provided pattern.
- [static func units(allowed: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLength: Int?, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy) -> Self](formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelength:fractionalpart:).md)
  Returns a style for formatting a duration that uses the specified units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelengthlimits:fractionalpart:))*