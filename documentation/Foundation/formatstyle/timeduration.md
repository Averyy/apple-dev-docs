# timeDuration

**Framework**: Foundation  
**Kind**: property

A style for formatting a duration expressed as a range of dates.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var timeDuration: Date.ComponentsFormatStyle { get }
```

#### Discussion

Use this type property when the call point allows the use of [`Date.FormatStyle`](date/formatstyle.md). You typically do this when calling the [`formatted(_:)`](date/formatted(_:).md) method of [`Date`](date.md).

The following example creates a one hour, thirty-five minute range between two dates, then uses SELF to format this duration as a string.

```swift
let now = Date.now
let future = now.addingTimeInterval(95)
let dateRange = now..<future
let formatted = dateRange.formatted(.timeDuration) // "1:35"
XCTAssertEqual(formatted, "1:35")
```

To use the Swift [`Duration`](https://developer.apple.com/documentation/Swift/Duration) type rather than `Date`, use [`Duration.TimeFormatStyle`](https://developer.apple.com/documentation/Swift/Duration/TimeFormatStyle) or [`Duration.UnitsFormatStyle`](https://developer.apple.com/documentation/Swift/Duration/UnitsFormatStyle) instead, and their corresponding static accessors, [`time(pattern:)`](formatstyle/time(pattern:).md) and [`units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)`](formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelength:fractionalpart:).md).

## See Also

- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.
- [static func time(pattern: Duration.TimeFormatStyle.Pattern) -> Self](formatstyle/time(pattern:).md)
  Returns a style for formatting a duration using a provided pattern.
- [static func units(allowed: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLength: Int?, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy) -> Self](formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelength:fractionalpart:).md)
  Returns a style for formatting a duration that uses the specified units.
- [static func units<ValueRange>(allowed: Set<Duration.UnitsFormatStyle.Unit>, width: Duration.UnitsFormatStyle.UnitWidth, maximumUnitCount: Int?, zeroValueUnits: Duration.UnitsFormatStyle.ZeroValueUnitsDisplayStrategy, valueLengthLimits: ValueRange, fractionalPart: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy) -> Self](formatstyle/units(allowed:width:maximumunitcount:zerovalueunits:valuelengthlimits:fractionalpart:).md)
  Returns a style for formatting a duration range that uses the specified units, with padding/truncating behavior defined as a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/timeduration)*