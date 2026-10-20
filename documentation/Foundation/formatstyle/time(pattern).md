# time(pattern:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a style for formatting a duration using a provided pattern.

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
static func time(pattern: Duration.TimeFormatStyle.Pattern) -> Self
```

Available when `Self` is `Duration.TimeFormatStyle`.

#### Return Value

A duration time format style customized with the specified pattern.

#### Discussion

Use the dot-notation form of this type method when the call point allows the use of [`Duration.TimeFormatStyle`](../../Swift/duration/timeformatstyle.md). You typically do this when calling the [`formatted(_:)`](../../Swift/duration/formatted%28_%29.md) method of [`Duration`](../../Swift/duration.md).

The following example creates a duration to represent 1 hour, 10 minutes, 32 seconds, and 400 milliseconds. It then uses [`time(pattern:)`](./time%28pattern%29.md) to customize a [`Duration.TimeFormatStyle`](../../Swift/duration/timeformatstyle.md) to show hours, minutes, and seconds, padding the hours part to two digits and limiting the fractional seconds to two digits. When used with the [`formatted(_:)`](../../Swift/duration/formatted%28_%29.md) method, the resulting string is `01:10:32.40`.

```swift
let duration = Duration.seconds(70 * 60 + 32) + Duration.milliseconds(400)
let format = duration.formatted(
    .time(pattern: .hourMinuteSecond(padHourToLength: 2,
                                     fractionalSecondsLength: 2)))
// format == "01:10:32.40"
```

## Parameters

- `pattern`: A [`Duration.TimeFormatStyle.Pattern`](../../Swift/duration/timeformatstyle/pattern-swift.struct.md) that specifies the units to include in the displayed string and the behavior of the units.

## See Also

### Applying duration styles
- [static var timeDuration: Date.ComponentsFormatStyle](./timeduration.md)
  A style for formatting a duration expressed as a range of dates.
- [struct ComponentsFormatStyle](../date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.
- [static func units(allowed: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLength: Int?, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy) -> Self](./units%28allowed,width,maximumunitcount,zerovalueunits,valuelength,fractionalpart%29.md)
  Returns a style for formatting a duration that uses the specified units.
- [static func units<ValueRange>(allowed: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLengthLimits: ValueRange, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy) -> Self](./units%28allowed,width,maximumunitcount,zerovalueunits,valuelengthlimits,fractionalpart%29.md)
  Returns a style for formatting a duration range that uses the specified units, with padding/truncating behavior defined as a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/time(pattern:))*