# allowedUnits

**Framework**: Foundation  
**Kind**: property

The bitmask of calendrical units such as day and month to include in the output string.

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
var allowedUnits: NSCalendar.Unit { get set }
```

#### Discussion

The allowed calendar units are:

- [`year`](nscalendar/unit/year.md)
- [`month`](nscalendar/unit/month.md)
- [`weekOfMonth`](nscalendar/unit/weekofmonth.md)
- [`day`](nscalendar/unit/day.md)
- [`hour`](nscalendar/unit/hour.md)
- [`minute`](nscalendar/unit/minute.md)
- [`second`](nscalendar/unit/second.md)

Assigning any other calendar units to this property results in an exception.

## See Also

- [var allowsFractionalUnits: Bool](datecomponentsformatter/allowsfractionalunits.md)
  A Boolean indicating whether non-integer units may be used for values.
- [var calendar: Calendar?](datecomponentsformatter/calendar.md)
  The default calendar to use when formatting date components.
- [var collapsesLargestUnit: Bool](datecomponentsformatter/collapseslargestunit.md)
  A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [var includesApproximationPhrase: Bool](datecomponentsformatter/includesapproximationphrase.md)
  A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [var includesTimeRemainingPhrase: Bool](datecomponentsformatter/includestimeremainingphrase.md)
  A Boolean value indicating whether output strings reflect the amount of time remaining.
- [var maximumUnitCount: Int](datecomponentsformatter/maximumunitcount.md)
  The maximum number of time units to include in the output string.
- [var unitsStyle: DateComponentsFormatter.UnitsStyle](datecomponentsformatter/unitsstyle-swift.property.md)
  The formatting style for unit names.
- [var zeroFormattingBehavior: DateComponentsFormatter.ZeroFormattingBehavior](datecomponentsformatter/zeroformattingbehavior-swift.property.md)
  The formatting style for units whose value is 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/allowedunits)*