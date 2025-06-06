# day()

**Framework**: Foundation  
**Kind**: method

Modifies the date interval format style to include the day.

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
func day() -> Date.IntervalFormatStyle
```

#### Return Value

A date interval format style that includes the day.

#### Discussion

Use a combination of modifier instance methods to customize the format of the date interval. The following example shows several combinations of year, month, and day components in the date interval:

```swift
if let today = Calendar.current.date(byAdding: .day, value: -140, to: Date()),
   let sevenDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -7, to: today) {

    // Create a Range<Date>.
    let weekBefore = sevenDaysBeforeToday..<today

    print(weekBefore.formatted(.interval))
    print(weekBefore.formatted(.interval.day()))
    print(weekBefore.formatted(.interval.day().month(.defaultDigits)))
    print(weekBefore.formatted(.interval.day().month(.wide).year()))
}
// 2/5/21, 6:37 AM – 2/12/21, 6:37 AM
// 5 – 12
// 2/5 – 2/12
// February 5 – 12, 2021
```

## See Also

- [func hour(Date.IntervalFormatStyle.Symbol.Hour) -> Date.IntervalFormatStyle](date/intervalformatstyle/hour(_:).md)
  Modifies the date interval format style to use the specified hour format style.
- [func minute() -> Date.IntervalFormatStyle](date/intervalformatstyle/minute.md)
  Modifies the date interval format style to include the minutes.
- [func month(Date.IntervalFormatStyle.Symbol.Month) -> Date.IntervalFormatStyle](date/intervalformatstyle/month(_:).md)
  Modifies the date interval format style to include the month.
- [func second() -> Date.IntervalFormatStyle](date/intervalformatstyle/second.md)
  Modifies the date interval format style to include the seconds.
- [func weekday(Date.IntervalFormatStyle.Symbol.Weekday) -> Date.IntervalFormatStyle](date/intervalformatstyle/weekday(_:).md)
  Modifies the date interval format style to include the specified weekday style.
- [func year() -> Date.IntervalFormatStyle](date/intervalformatstyle/year.md)
  Modifies the date interval format style to include the year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/intervalformatstyle/day())*