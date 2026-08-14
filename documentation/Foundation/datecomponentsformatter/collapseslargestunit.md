# collapsesLargestUnit

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.

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
var collapsesLargestUnit: Bool { get set }
```

#### Discussion

An example of when this property might apply is when expressing 63 seconds worth of time. When this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the formatted value would be “63s”. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the formatted value would be “1m 3s”.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var allowedUnits: NSCalendar.Unit](datecomponentsformatter/allowedunits.md)
  The bitmask of calendrical units such as day and month to include in the output string.
- [var allowsFractionalUnits: Bool](datecomponentsformatter/allowsfractionalunits.md)
  A Boolean indicating whether non-integer units may be used for values.
- [var calendar: Calendar?](datecomponentsformatter/calendar.md)
  The default calendar to use when formatting date components.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/collapseslargestunit)*