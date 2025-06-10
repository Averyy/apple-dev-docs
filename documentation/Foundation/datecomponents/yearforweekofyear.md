# yearForWeekOfYear

**Framework**: Foundation  
**Kind**: property

The year corresponding to a week-counting week.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var yearForWeekOfYear: Int? { get set }
```

#### Discussion

The Gregorian calendar defines a week to have 7 days, and a year to have 365 days, or 366 in a leap year. However, neither 365 or 366 divide evenly into a 7-day week, so it is often the case that the last week of a year ends on a day in the next year, and the first week of a year begins in the preceding year. To reconcile this, ISO 8601 defines a week-numbering year, consisting of either 52 or 53 full weeks (364 or 371 days), such that the first week of a year is designated to be the week containing the first Thursday of the year. For a given date, the [`weekOfYear`](datecomponents/weekofyear.md) property indicates which week the date falls in, and [`yearForWeekOfYear`](datecomponents/yearforweekofyear.md) provides the corresponding week-numbering year.

> ❗ **Important**:  The values of [`weekOfYear`](datecomponents/weekofyear.md) and [`yearForWeekOfYear`](datecomponents/yearforweekofyear.md) depend on the calendar they are used with. For example, the ISO 8601 calendar starts a week on Monday, and uses the first Thursday to determine the first week of the year. However, the Gregorian calendar as used in North America starts the week on Sunday, and uses the year’s first Saturday to determine the first week.

You can use the week-numbering year when specifying a date with [`DateComponents`](datecomponents.md), usually in combination with the [`weekOfYear`](datecomponents/weekofyear.md). The code listing below shows this approach. It creates a [`DateComponents`](datecomponents.md) instance specifying the first Friday (weekday 6) of the first week of 2016, which started on a Friday. Therefore, this date is January 1, 2016 in the Gregorian calendar. However, on the ISO 8601 calendar, the first week of 2016 begins on the following Monday. This means the first Friday in the first week of 2016 is January 8, 2016 on the ISO 8601 calendar.

```swift
let comps = DateComponents(weekday: 6, weekOfYear: 1, yearForWeekOfYear: 2016)
let gregorianCalendar = Calendar(identifier: .gregorian)
let gregorianDate = gregorianCalendar.date(from: comps)!
let iso8601Calendar = Calendar(identifier: .iso8601)
let iso8601Date = iso8601Calendar.date(from: comps)!

let formatter = DateFormatter()
formatter.dateStyle = .full
formatter.calendar = gregorianCalendar
print ("\(formatter.string(from: gregorianDate))") // "Friday, January 1, 2016"
formatter.calendar = iso8601Calendar
print ("\(formatter.string(from: iso8601Date))") // "Friday, January 8, 2016"


```

## See Also

- [var era: Int?](datecomponents/era.md)
  An era or count of eras.
- [var year: Int?](datecomponents/year.md)
  A year or count of years.
- [var quarter: Int?](datecomponents/quarter.md)
  A quarter or count of quarters.
- [var month: Int?](datecomponents/month.md)
  A month or count of months.
- [var isLeapMonth: Bool?](datecomponents/isleapmonth.md)
  Set to true if these components represent a leap month.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/yearforweekofyear)*