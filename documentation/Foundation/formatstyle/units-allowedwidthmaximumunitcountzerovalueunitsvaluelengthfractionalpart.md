# units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)

**Framework**: Foundation  
**Kind**: method

Returns a style for formatting a duration that uses the specified units.

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
static func units(allowed units: Set<Duration.UnitsFormatStyle.Unit> = [.hours, .minutes, .seconds], width: Duration.UnitsFormatStyle.UnitWidth = .abbreviated, maximumUnitCount: Int? = nil, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy = .hide, valueLength: Int? = nil, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy = .hide) -> Self
```

#### Return Value

A duration units format style that uses the specified units.

#### Discussion

Use the dot-notation form of this type method when the call point allows the use of [`Duration.UnitsFormatStyle`](https://developer.apple.com/documentation/Swift/Duration/UnitsFormatStyle). You typically do this when calling the [`formatted(_:)`](https://developer.apple.com/documentation/Swift/Duration/formatted(_:)) method of [`Duration`](https://developer.apple.com/documentation/Swift/Duration).

The following example creates a duration to represent 1 hour, 10 minutes, 32 seconds, and 400 milliseconds. It then creates a [`Duration.UnitsFormatStyle`](https://developer.apple.com/documentation/Swift/Duration/UnitsFormatStyle) to show the hours, minutes, seconds, and milliseconds parts, with a wide width that presents the full name of each unit.

```swift
let duration = Duration.seconds(70 * 60 + 32) + Duration.milliseconds(400)
let formatted = duration.formatted(
     .units(allowed: [.hours, .minutes, .seconds, .milliseconds],
            width: .wide))
// "1 hour, 10 minutes, 32 seconds, 400 milliseconds"

```

## Parameters

- `units`: The units that the formatted string may include.
- `width`: The width of the unit and the spacing between the value and the unit.
- `maximumUnitCount`: The maximum number of duration units, if any, to include in the output string.
- `zeroValueUnits`: The strategy for handling leading units with zero values.
- `valueLength`: The padding or truncating behavior of the unit value, as an  . Defaults to  , which applies no length limit.
- `fractionalPart`: The strategy for displaying a duration if a formatted string can’t represent it exactly with the allowed units.

## See Also

- [static var timeDuration: Date.ComponentsFormatStyle](formatstyle/timeduration.md)
  A style for formatting a duration expressed as a range of dates.
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.
- [static func time(pattern: Duration.TimeFormatStyle.Pattern) -> Self](formatstyle/time(pattern:).md)
  Returns a style for formatting a duration using a provided pattern.
- [static func units<ValueRange>(allowed: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLengthLimits: ValueRange, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy) -> Self](formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelengthlimits:fractionalpart:).md)
  Returns a style for formatting a duration range that uses the specified units, with padding/truncating behavior defined as a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelength:fractionalpart:))*