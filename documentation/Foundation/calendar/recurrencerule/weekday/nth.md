# Calendar.RecurrenceRule.Weekday.nth(_:_:)

**Framework**: Foundation  
**Kind**: case

Repeat on the n-th instance of the specified weekday in a month, if the recurrence has a monthly frequency. If the recurrence has a yearly frequency, repeat on the n-th week of the year.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
case nth(Int, Locale.Weekday)
```

#### Discussion

If n is negative, repeat on the n-to-last of the given weekday.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/weekday/nth(_:_:))*