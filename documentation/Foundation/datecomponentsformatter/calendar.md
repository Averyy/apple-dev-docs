# calendar

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The default calendar to use when formatting date components.

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
var calendar: Calendar? { get set }
```

```objc
@property (copy, nullable) NSCalendar * calendar;
```

## Discussion

The formatter uses the calendar in this property to format values that do not have an inherent calendar of their own. For example, the formatter uses this calendar when formatting an [`TimeInterval`](../timeinterval.md) value.

The default value of this property is the calendar returned by the [`autoupdatingCurrent`](../nscalendar/autoupdatingcurrent.md) method of [`NSCalendar`](../nscalendar.md). Setting this property to `nil` causes the formatter to use the Gregorian calendar with the `en_US_POSIX` locale.

## See Also

### Configuring the Formatter Options
- [var allowedUnits: NSCalendar.Unit](./allowedunits.md)
  The bitmask of calendrical units such as day and month to include in the output string.
- [var allowsFractionalUnits: Bool](./allowsfractionalunits.md)
  A Boolean indicating whether non-integer units may be used for values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/calendar)*