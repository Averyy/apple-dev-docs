# includesTimeRemainingPhrase

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether output strings reflect the amount of time remaining.

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
var includesTimeRemainingPhrase: Bool { get set }
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) results in output strings like “30 minutes remaining”.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var allowedUnits: NSCalendar.Unit](datecomponentsformatter/allowedunits.md)
  The bitmask of calendrical units such as day and month to include in the output string.
- [var allowsFractionalUnits: Bool](datecomponentsformatter/allowsfractionalunits.md)
  A Boolean indicating whether non-integer units may be used for values.
- [var calendar: Calendar?](datecomponentsformatter/calendar.md)
  The default calendar to use when formatting date components.
- [var collapsesLargestUnit: Bool](datecomponentsformatter/collapseslargestunit.md)
  A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [var includesApproximationPhrase: Bool](datecomponentsformatter/includesapproximationphrase.md)
  A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [var maximumUnitCount: Int](datecomponentsformatter/maximumunitcount.md)
  The maximum number of time units to include in the output string.
- [var unitsStyle: DateComponentsFormatter.UnitsStyle](datecomponentsformatter/unitsstyle-swift.property.md)
  The formatting style for unit names.
- [var zeroFormattingBehavior: DateComponentsFormatter.ZeroFormattingBehavior](datecomponentsformatter/zeroformattingbehavior-swift.property.md)
  The formatting style for units whose value is 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/includestimeremainingphrase)*