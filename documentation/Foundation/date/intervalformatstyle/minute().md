# minute()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date interval format style to include the minutes.

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
func minute() -> Date.IntervalFormatStyle
```

## Return Value

A date interval format style that includes the minutes.

## Discussion

This example shows a combination of date interval format styles that includes the hour and minutes:

```swift
if let today = Calendar.current.date(byAdding: .day, value: -140, to: Date()),
   let sevenDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -7, to: today) {

    // Create a Range<Date>.
    let weekBefore = sevenDaysBeforeToday..<today

    print(weekBefore.formatted(.interval.minute()))
    print(weekBefore.formatted(.interval.day().minute().hour()))
    print(weekBefore.formatted(.interval.day().month().minute().hour(.defaultDigitsNoAMPM)))
    print(weekBefore.formatted(.interval.day().month().minute().hour(.conversationalDefaultDigits(amPM: .wide))))
    print(weekBefore.formatted(.interval.day().month().minute().hour(.conversationalDefaultDigits(amPM: .narrow))))
}
// 2/5/2021, 9 – 2/12/2021, 9
// 5, 7:09 AM – 12, 7:09 AM
// Feb 5, 07:09 – Feb 12, 07:09
// Feb 5, 7:09 AM – Feb 12, 7:09 AM
// Feb 5, 7:09 a – Feb 12, 7:09 a

```

## See Also

### Modifying Date Interval Format Styles
- [func day() -> Date.IntervalFormatStyle](./day%28%29.md)
  Modifies the date interval format style to include the day.
- [func hour(Date.IntervalFormatStyle.Symbol.Hour) -> Date.IntervalFormatStyle](./hour%28_%29.md)
  Modifies the date interval format style to use the specified hour format style.
- [func month(Date.IntervalFormatStyle.Symbol.Month) -> Date.IntervalFormatStyle](./month%28_%29.md)
  Modifies the date interval format style to include the month.
- [func second() -> Date.IntervalFormatStyle](./second%28%29.md)
  Modifies the date interval format style to include the seconds.
- [func weekday(Date.IntervalFormatStyle.Symbol.Weekday) -> Date.IntervalFormatStyle](./weekday%28_%29.md)
  Modifies the date interval format style to include the specified weekday style.
- [func year() -> Date.IntervalFormatStyle](./year%28%29.md)
  Modifies the date interval format style to include the year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/intervalformatstyle/minute())*