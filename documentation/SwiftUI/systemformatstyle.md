# SystemFormatStyle

**Framework**: SwiftUI  
**Kind**: enum

A collection of format styles for displaying live-updating time information in text views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum SystemFormatStyle
```

#### Overview

Use the format styles in this namespace to present time-based data in [`Text`](text.md) views that automatically updates as the system clock advances. Each style formats a [`Date`](https://developer.apple.com/documentation/foundation/date) value into an [`AttributedString`](https://developer.apple.com/documentation/foundation/attributedstring) and conforms to both `FormatStyle` and `DiscreteFormatStyle`, allowing SwiftUI to efficiently schedule text updates at exactly the right moments.

You typically use these styles with the [`init(_:format:)`](text/init(_:format:)-8sfgg.md) initializer:

```swift
let startDate = Date.now
let endDate = startDate.addingTimeInterval(300)

Text(.currentDate, format: .offset(to: startDate))
// Output: "3 minutes, 42 seconds"

Text(.currentDate, format: .stopwatch(startingAt: startDate))
// Output: "00:03.42"

Text(.currentDate, format: .timer(countingDownIn: startDate..<endDate))
// Output: "4:17"

Text(.currentDate, format: .reference(to: endDate))
// Output: "in 5 minutes"
```

#### Choosing a Style

| Style | Purpose | Example Output |
| --- | --- | --- |
| [`SystemFormatStyle.DateOffset`](systemformatstyle/dateoffset.md) | Elapsed time since or until a date | `3 minutes, 42 seconds` |
| [`SystemFormatStyle.Stopwatch`](systemformatstyle/stopwatch.md) | Precision stopwatch counting up | `00:03.42` |
| [`SystemFormatStyle.Timer`](systemformatstyle/timer.md) | Countdown or count-up within a bounded interval | `4:17` |
| [`SystemFormatStyle.DateReference`](systemformatstyle/datereference.md) | Natural-language reference to a date | `in 5 minutes`, `yesterday` |

## Topics

### Structures
- [SystemFormatStyle.DateOffset](systemformatstyle/dateoffset.md)
  A format style that displays the time offset between a comparison date and an anchor date that you provide.
- [SystemFormatStyle.DateReference](systemformatstyle/datereference.md)
  A format style that refers to a date using the most natural phrasing based on how much time separates it from the current time.
- [SystemFormatStyle.Stopwatch](systemformatstyle/stopwatch.md)
  A format style that displays elapsed time as a precision stopwatch counting up from zero.
- [SystemFormatStyle.Timer](systemformatstyle/timer.md)
  A format style that displays a countdown or count-up timer within a bounded time interval.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct TimeDataSource](timedatasource.md)
  A source of time related data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle)*