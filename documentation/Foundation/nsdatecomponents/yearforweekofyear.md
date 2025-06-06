# yearForWeekOfYear

**Framework**: Foundation  
**Kind**: property

The ISO 8601 week-numbering year.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var yearForWeekOfYear: Int { get set }
```

#### Discussion

The Gregorian calendar defines a week to have 7 days, and a year to have 365 days, or 366 in a leap year. However, neither 365 or 366 divide evenly into a 7-day week, so it is often the case that the last week of a year ends on a day in the next year, and the first week of a year begins in the preceding year. To reconcile this, ISO 8601 defines a week-numbering year, consisting of either 52 or 53 full weeks (364 or 371 days), such that the first week of a year is designated to be the week containing the first Thursday of the year. For a given date, the [`weekOfYear`](nsdatecomponents/weekofyear.md) property indicates which week the date falls in, and [`yearForWeekOfYear`](nsdatecomponents/yearforweekofyear.md) provides the corresponding week-numbering year.

> ❗ **Important**:  The values of [`weekOfYear`](nsdatecomponents/weekofyear.md) and [`yearForWeekOfYear`](nsdatecomponents/yearforweekofyear.md) depend on the calendar they are used with. For example, the ISO 8601 calendar starts a week on Monday, and uses the first Thursday to determine the first week of the year. However, the Gregorian calendar as used in North America starts the week on Sunday, and uses the year’s first Saturday to determine the first week.

 The values of [`weekOfYear`](nsdatecomponents/weekofyear.md) and [`yearForWeekOfYear`](nsdatecomponents/yearforweekofyear.md) depend on the calendar they are used with. For example, the ISO 8601 calendar starts a week on Monday, and uses the first Thursday to determine the first week of the year. However, the Gregorian calendar as used in North America starts the week on Sunday, and uses the year’s first Saturday to determine the first week.

You can use the week-numbering year when specifying a date with [`NSDateComponents`](nsdatecomponents.md), usually in combination with the [`weekOfYear`](nsdatecomponents/weekofyear.md). The code listing below shows this approach. It creates an [`NSDateComponents`](nsdatecomponents.md) instance specifying the first Friday (weekday 6) of the first week of 2016, which started on a Friday. Therefore, this date is January 1, 2016 in the Gregorian calendar. However, on the ISO 8601 calendar, the first week of 2016 begins on the following Monday. This means the first Friday in the first week of 2016 is January 8, 2016 on the ISO 8601 calendar.

```swift
NSDateComponents *comps = [[NSDateComponents alloc] init];
comps.weekday = 6;
comps.weekOfYear = 1;
comps.yearForWeekOfYear = 2016;
NSCalendar *gregorianCalendar = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierGregorian];
NSDate *gregorianDate = [gregorianCalendar dateFromComponents:comps];
NSCalendar *iso8610Calendar = [[NSCalendar alloc] initWithCalendarIdentifier:NSCalendarIdentifierISO8601];
NSDate *iso8610Date = [iso8610Calendar dateFromComponents:comps];

NSDateFormatter *formatter = [[NSDateFormatter alloc] init];
formatter.dateStyle = NSDateFormatterFullStyle;
formatter.calendar = gregorianCalendar;
NSLog (@"%@", [formatter stringFromDate:gregorianDate]); // "Friday, January 1, 2016"
formatter.calendar = iso8610Calendar;
NSLog (@"%@", [formatter stringFromDate:iso8610Date]); // "Friday, January 8, 2016"

```

## See Also

- [var era: Int](nsdatecomponents/era.md)
  The number of eras.
- [var year: Int](nsdatecomponents/year.md)
  The number of years.
- [var quarter: Int](nsdatecomponents/quarter.md)
  The number of quarters.
- [var month: Int](nsdatecomponents/month.md)
  The number of months.
- [var isLeapMonth: Bool](nsdatecomponents/isleapmonth.md)
  A Boolean value that indicates whether the month is a leap month.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/yearforweekofyear)*