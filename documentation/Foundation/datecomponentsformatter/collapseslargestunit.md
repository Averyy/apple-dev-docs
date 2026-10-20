# collapsesLargestUnit

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL collapsesLargestUnit;
```

#### Discussion

An example of when this property might apply is when expressing 63 seconds worth of time. When this property is set to [`true`](../../Swift/true.md), the formatted value would be “63s”. When the value of this property is [`false`](../../Swift/false.md), the formatted value would be “1m 3s”.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the Formatter Options
- [var allowedUnits: NSCalendar.Unit](./allowedunits.md)
  The bitmask of calendrical units such as day and month to include in the output string.
- [var allowsFractionalUnits: Bool](./allowsfractionalunits.md)
  A Boolean indicating whether non-integer units may be used for values.
- [var calendar: Calendar?](./calendar.md)
  The default calendar to use when formatting date components.
- [var includesApproximationPhrase: Bool](./includesapproximationphrase.md)
  A Boolean value indicating whether the resulting phrase reflects an inexact time value.
- [var includesTimeRemainingPhrase: Bool](./includestimeremainingphrase.md)
  A Boolean value indicating whether output strings reflect the amount of time remaining.
- [var maximumUnitCount: Int](./maximumunitcount.md)
  The maximum number of time units to include in the output string.
- [var unitsStyle: DateComponentsFormatter.UnitsStyle](./unitsstyle-swift.property.md)
  The formatting style for unit names.
- [var zeroFormattingBehavior: DateComponentsFormatter.ZeroFormattingBehavior](./zeroformattingbehavior-swift.property.md)
  The formatting style for units whose value is 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/collapseslargestunit)*