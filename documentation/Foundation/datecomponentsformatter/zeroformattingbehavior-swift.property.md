# zeroFormattingBehavior

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The formatting style for units whose value is 0.

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
var zeroFormattingBehavior: DateComponentsFormatter.ZeroFormattingBehavior { get set }
```

```objc
@property NSDateComponentsFormatterZeroFormattingBehavior zeroFormattingBehavior;
```

#### Discussion

When the value for a particular unit is 0, the zero formatting behavior determines whether that value is retained or omitted from any resulting strings. For example, when the formatting behavior is [`dropTrailing`](./zeroformattingbehavior-swift.struct/droptrailing.md), the value of one hour, ten minutes, and zero seconds would omit the mention of seconds.

The default value of this property is [`default`](./zeroformattingbehavior-swift.struct/default.md).

## See Also

### Configuring the Formatter Options
- [var allowedUnits: NSCalendar.Unit](./allowedunits.md)
  The bitmask of calendrical units such as day and month to include in the output string.
- [var allowsFractionalUnits: Bool](./allowsfractionalunits.md)
  A Boolean indicating whether non-integer units may be used for values.
- [var calendar: Calendar?](./calendar.md)
  The default calendar to use when formatting date components.
- [var collapsesLargestUnit: Bool](./collapseslargestunit.md)
  A Boolean value indicating whether to collapse the largest unit into smaller units when a certain threshold is met.
- [var includesApproximationPhrase: Bool](./includesapproximationphrase.md)
  A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [var includesTimeRemainingPhrase: Bool](./includestimeremainingphrase.md)
  A Boolean value indicating whether output strings reflect the amount of time remaining.
- [var maximumUnitCount: Int](./maximumunitcount.md)
  The maximum number of time units to include in the output string.
- [var unitsStyle: DateComponentsFormatter.UnitsStyle](./unitsstyle-swift.property.md)
  The formatting style for unit names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/zeroformattingbehavior-swift.property)*