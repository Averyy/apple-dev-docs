# allowsFractionalUnits

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether non-integer units may be used for values.

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
var allowsFractionalUnits: Bool { get set }
```

```objc
@property BOOL allowsFractionalUnits;
```

## Discussion

Fractional units may be used when a value cannot be exactly represented using the available units. For example, if minutes are not allowed, the value “1h 30m” could be formatted as “1.5h”.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Configuring the Formatter Options
- [var allowedUnits: NSCalendar.Unit](./allowedunits.md)
  The bitmask of calendrical units such as day and month to include in the output string.
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
- [var zeroFormattingBehavior: DateComponentsFormatter.ZeroFormattingBehavior](./zeroformattingbehavior-swift.property.md)
  The formatting style for units whose value is 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/allowsfractionalunits)*