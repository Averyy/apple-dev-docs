# Duration.UnitsFormatStyle.FractionalPartDisplayStrategy

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A strategy that determines how to format the fractional part of a duration if the allowed units can’t represent it exactly.

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
struct FractionalPartDisplayStrategy
```

#### Overview

When using a [`Duration.UnitsFormatStyle`](../unitsformatstyle.md), specifying a `FractionalPartDisplayStrategy` enables you to decide how to balance between accuracy and verbosity when you’re not using all of the available units (hours, minutes, and seconds). When a formatted duration has a fractional part, you can hide it entirely, round the unit up or down while hiding the fractional part, or show the unit with a fraction.

The following example shows different display strategies used with a duration of 1 hour, 15 minutes and unit format styles that only show hours.

```swift
let duration = Duration.seconds(75 * 60) // 1 minute, 15 seconds
let hide = duration.formatted(
    .units(allowed: [.hours],
           width: .wide,
           fractionalPart: .hide)) // 1 hour
let hideRounded = duration.formatted(
    .units(allowed: [.hours],
           width: .wide,
           fractionalPart: .hide(rounded:.up))) // 2 hours
let show = duration.formatted(
    .units(allowed: [.hours],
           width: .wide,
           fractionalPart: .show(length: 2))) // 1.25 hours
```

## Topics

### Creating a fractional part display strategy
- [init<Range>(lengthLimits: Range, roundingRule: FloatingPointRoundingRule, roundingIncrement: Double?)](./fractionalpartdisplaystrategy/init%28lengthlimits,roundingrule,roundingincrement%29.md)
  Creates a fractional part display strategy that uses the provided behaviors.
### Using common strategies
- [static var hide: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](./fractionalpartdisplaystrategy/hide.md)
  A display strategy that hides any fractional part by truncating it.
- [static func hide(rounded: FloatingPointRoundingRule) -> Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](./fractionalpartdisplaystrategy/hide%28rounded%29.md)
  Creates a display strategy that hides any fractional part rounding the unit value.
- [static func show(length: Int, rounded: FloatingPointRoundingRule, increment: Double?) -> Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](./fractionalpartdisplaystrategy/show%28length,rounded,increment%29.md)
  Creates a display strategy that shows a fractional part.
### Working with strategy properties
- [var minimumLength: Int](./fractionalpartdisplaystrategy/minimumlength.md)
  The minimum length of the fractional part, if shown.
- [var maximumLength: Int](./fractionalpartdisplaystrategy/maximumlength.md)
  The maximum length of the fractional part, if shown.
- [var roundingIncrement: Double?](./fractionalpartdisplaystrategy/roundingincrement.md)
  A multiple by which a formatter rounds a fractional part of a duration.
- [var roundingRule: FloatingPointRoundingRule](./fractionalpartdisplaystrategy/roundingrule.md)
  The rule for rounding a unit up or down if it has a fractional part.

## Relationships

### Conforms To
- [Decodable](../../decodable.md)
- [Encodable](../../encodable.md)
- [Equatable](../../equatable.md)
- [Hashable](../../hashable.md)
- [Sendable](../../sendable.md)
- [SendableMetatype](../../sendablemetatype.md)

## See Also

### Working with fractional values
- [var fractionalPartDisplay: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](./fractionalpartdisplay.md)
  The strategy for displaying a duration if it cannot be represented exactly with the allowed units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy)*