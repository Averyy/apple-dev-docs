# year

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of years.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var year: Int { get set }
```

```objc
@property NSInteger year;
```

## Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Years and Months
- [var era: Int](./era.md)
  The number of eras.
- [var yearForWeekOfYear: Int](./yearforweekofyear.md)
  The ISO 8601 week-numbering year.
- [var quarter: Int](./quarter.md)
  The number of quarters.
- [var month: Int](./month.md)
  The number of months.
- [var isLeapMonth: Bool](./isleapmonth.md)
  A Boolean value that indicates whether the month is a leap month.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/year)*