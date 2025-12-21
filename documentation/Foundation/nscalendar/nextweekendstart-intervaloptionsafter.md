# nextWeekendStart(_:interval:options:after:)

**Framework**: Foundation  
**Kind**: method

Returns by reference the starting date and time interval range of the next weekend period after a given date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func nextWeekendStart(_ datep: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval tip: UnsafeMutablePointer<TimeInterval>?, options: NSCalendar.Options = [], after date: Date) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/Swift/false) if the calendar and locale do not have the concept of a weekend, otherwise [`true`](https://developer.apple.com/documentation/Swift/true).

#### Discussion

Note that a particular calendar day may not necessarily fall entirely within a weekend period, as weekends can start in the middle of a day in some calendars and locales.

## Parameters

- `datep`: Upon return, contains the starting date of the next weekend period.
- `tip`: Upon return, contains the time interval of the next weekend period.
- `options`: Options for the calculation. If you specify a backward search option ( ), the starting date and time interval range of the preceding weekend period will be returned by reference instead.
- `date`: The date for which to perform the calculation.

## See Also

- [func date(from: DateComponents) -> Date?](nscalendar/date(from:).md)
  Returns a date representing the absolute time calculated from given components.
- [func date(byAdding: DateComponents, to: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(byadding:to:options:).md)
  Returns a date representing the absolute time calculated by adding given components to a given date.
- [func date(byAdding: NSCalendar.Unit, value: Int, to: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(byadding:value:to:options:).md)
  Returns a date representing the absolute time calculated by adding the value of a given component to a given date.
- [func date(bySettingHour: Int, minute: Int, second: Int, of: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(bysettinghour:minute:second:of:options:).md)
  Creates a new date calculated with the given time.
- [func date(bySettingUnit: NSCalendar.Unit, value: Int, of: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(bysettingunit:value:of:options:).md)
  Returns a new date representing the date calculated by setting a specific component of a given date to a given value, while trying to keep lower components the same.
- [func date(era: Int, year: Int, month: Int, day: Int, hour: Int, minute: Int, second: Int, nanosecond: Int) -> Date?](nscalendar/date(era:year:month:day:hour:minute:second:nanosecond:).md)
  Returns a date created with the given components.
- [func date(era: Int, yearForWeekOfYear: Int, weekOfYear: Int, weekday: Int, hour: Int, minute: Int, second: Int, nanosecond: Int) -> Date?](nscalendar/date(era:yearforweekofyear:weekofyear:weekday:hour:minute:second:nanosecond:).md)
  Returns a new date created with the given components base on a week-of-year value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/nextweekendstart(_:interval:options:after:))*