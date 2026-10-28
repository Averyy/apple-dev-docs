# includesApproximationPhrase

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the resulting phrase reflects an inexact time value.

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
var includesApproximationPhrase: Bool { get set }
```

```objc
@property BOOL includesApproximationPhrase;
```

## Discussion

Setting the value of this property to [`true`](../../Swift/true.md) adds phrasing to output strings to reflect that the given time value is approximate and not exact. Using this property yields more correct phrasing than simply prepending the string “About” to an output string.

The default value of this property is [`false`](../../Swift/false.md).

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
- [var includesTimeRemainingPhrase: Bool](./includestimeremainingphrase.md)
  A Boolean value indicating whether output strings reflect the amount of time remaining.
- [var maximumUnitCount: Int](./maximumunitcount.md)
  The maximum number of time units to include in the output string.
- [var unitsStyle: DateComponentsFormatter.UnitsStyle](./unitsstyle-swift.property.md)
  The formatting style for unit names.
- [var zeroFormattingBehavior: DateComponentsFormatter.ZeroFormattingBehavior](./zeroformattingbehavior-swift.property.md)
  The formatting style for units whose value is 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/includesapproximationphrase)*