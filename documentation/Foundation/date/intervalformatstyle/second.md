# second()

**Framework**: Foundation  
**Kind**: method

Modifies the date interval format style to include the seconds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func second() -> Date.IntervalFormatStyle
```

#### Return Value

A date interval format style that includes the seconds.

#### Discussion

This example shows a combination of date interval format styles that include the hour, minutes, and seconds:

```swift
if let today = Calendar.current.date(byAdding: .day, value: -140, to: Date()),
   let sevenDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -7, to: today) {

    // Create a Range<Date>.
    let weekBefore = sevenDaysBeforeToday..<today

    print(weekBefore.formatted(.interval.minute()))
    print(weekBefore.formatted(.interval.day().minute().hour().second()))
}
// 2/5/2021, 17 – 2/12/2021, 17
// 5, 8:17:19 AM – 12, 8:17:19 AM
```

## See Also

- [func day() -> Date.IntervalFormatStyle](date/intervalformatstyle/day.md)
  Modifies the date interval format style to include the day.
- [func hour(Date.IntervalFormatStyle.Symbol.Hour) -> Date.IntervalFormatStyle](date/intervalformatstyle/hour(_:).md)
  Modifies the date interval format style to use the specified hour format style.
- [func minute() -> Date.IntervalFormatStyle](date/intervalformatstyle/minute.md)
  Modifies the date interval format style to include the minutes.
- [func month(Date.IntervalFormatStyle.Symbol.Month) -> Date.IntervalFormatStyle](date/intervalformatstyle/month(_:).md)
  Modifies the date interval format style to include the month.
- [func weekday(Date.IntervalFormatStyle.Symbol.Weekday) -> Date.IntervalFormatStyle](date/intervalformatstyle/weekday(_:).md)
  Modifies the date interval format style to include the specified weekday style.
- [func year() -> Date.IntervalFormatStyle](date/intervalformatstyle/year.md)
  Modifies the date interval format style to include the year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/intervalformatstyle/second())*