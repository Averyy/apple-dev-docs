# Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy

**Framework**: Swift  
**Kind**: struct

A strategy that determines how to format a unit whose value is zero.

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
struct ZeroValueUnitsDisplayStrategy
```

#### Overview

When using a [`Duration.UnitsFormatStyle`](duration/unitsformatstyle.md), specifying a `ZeroValueUnitsDisplayStrategy` enables you to decide whether show a unit whose value is zero.

The following example creates a duration of 25 seconds, then formats it with two different styles. The first style uses the [`hide`](duration/unitsformatstyle/zerovalueunitsdisplaystrategy/hide.md) display strategy, which omits the hours and minutes, since their value is `0`. The second uses [`show(length:)`](duration/unitsformatstyle/zerovalueunitsdisplaystrategy/show(length:).md) to create two-digit representations of the hour and minute fields.

```swift
let duration = Duration.seconds(25)
let hide = duration.formatted(
    .units(allowed: [.hours, .minutes, .seconds],
           width: .abbreviated,
           zeroValueUnits:.hide)) // 25 sec
let showTwo = duration.formatted(
    .units(allowed: [.hours, .minutes, .seconds],
           width: .abbreviated,
           zeroValueUnits:.show(length: 2))) // 00 hr, 00 min, 25 sec
```

## Topics

### Using common strategies
- [static var hide: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy](duration/unitsformatstyle/zerovalueunitsdisplaystrategy/hide.md)
  A display strategy that hides leading fields whose value is zero.
- [static func show(length: Int) -> Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy](duration/unitsformatstyle/zerovalueunitsdisplaystrategy/show(length:).md)
  Returns display strategy that shows leading fields whose value is zero, with a given number of digits.

## Relationships

### Conforms To
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)

## See Also

- [var zeroValueUnitsDisplay: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy](duration/unitsformatstyle/zerovalueunitsdisplay.md)
  The strategy for how zero-value units are handled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/zerovalueunitsdisplaystrategy)*