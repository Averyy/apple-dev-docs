# weekday(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Modifies the date interval format style to include the specified weekday style.

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
func weekday(_ format: Date.IntervalFormatStyle.Symbol.Weekday = .abbreviated) -> Date.IntervalFormatStyle
```

#### Return Value

A date interval format style that includes the specified weekday style.

#### Discussion

Use a combination of modifier instance methods to customize the format of the date interval. The following example shows a combination date interval format styles that include the weekday:

```swift
if let today = Calendar.current.date(byAdding: .day, value: -140, to: Date()),
   let sevenDaysBeforeToday = Calendar.current.date(byAdding: .day, value: -7, to: today) {

    // Create a Range<Date>.
    let weekBefore = sevenDaysBeforeToday..<today

    print(weekBefore.formatted(.interval.day().month(.wide).year().weekday(.wide)))
    print(weekBefore.formatted(.interval.day().weekday(.abbreviated)))
    print(weekBefore.formatted(.interval.day().month(.wide).weekday(.narrow)))
}
// Friday, February 5 – Friday, February 12, 2021
// 5 Fri – 12 Fri
// F, February 5 – F, February 12
```

## Parameters

- `format`: The weekday format style to apply to the date interval format style.

## See Also

### Modifying Date Interval Format Styles
- [func day() -> Date.IntervalFormatStyle](./day%28%29.md)
  Modifies the date interval format style to include the day.
- [func hour(Date.IntervalFormatStyle.Symbol.Hour) -> Date.IntervalFormatStyle](./hour%28_%29.md)
  Modifies the date interval format style to use the specified hour format style.
- [func minute() -> Date.IntervalFormatStyle](./minute%28%29.md)
  Modifies the date interval format style to include the minutes.
- [func month(Date.IntervalFormatStyle.Symbol.Month) -> Date.IntervalFormatStyle](./month%28_%29.md)
  Modifies the date interval format style to include the month.
- [func second() -> Date.IntervalFormatStyle](./second%28%29.md)
  Modifies the date interval format style to include the seconds.
- [func year() -> Date.IntervalFormatStyle](./year%28%29.md)
  Modifies the date interval format style to include the year.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/intervalformatstyle/weekday(_:))*