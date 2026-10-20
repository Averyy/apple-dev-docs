# getHour(_:minute:second:nanosecond:from:)

**Framework**: Foundation  
**Kind**: method

Returns by reference the hour, minute, second, and nanosecond component values for a given date.

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
func getHour(_ hourValuePointer: UnsafeMutablePointer<Int>?, minute minuteValuePointer: UnsafeMutablePointer<Int>?, second secondValuePointer: UnsafeMutablePointer<Int>?, nanosecond nanosecondValuePointer: UnsafeMutablePointer<Int>?, from date: Date)
```

#### Discussion

Pass `NULL` to ignore any individual component parameter.

This is a convenience method for getting the time components of a given date using [`components(_:from:)`](nscalendar/components(_:from:).md)

## Parameters

- `hourValuePointer`: Upon return, contains the hour of the given date.
- `minuteValuePointer`: Upon return, contains the minute of the given date.
- `secondValuePointer`: Upon return, contains the second of the given date.
- `nanosecondValuePointer`: Upon return, contains the nanosecond of the given date.
- `date`: The date for which to perform the calculation.

## See Also

- [func date(Date, matchesComponents: DateComponents) -> Bool](nscalendar/date(_:matchescomponents:).md)
  Returns whether a given date matches all of the given date components.
- [func component(NSCalendar.Unit, from: Date) -> Int](nscalendar/component(_:from:).md)
  Returns the specified date component from a given date.
- [func components(NSCalendar.Unit, from: Date) -> DateComponents](nscalendar/components(_:from:).md)
  Returns the date components representing a given date.
- [func components(NSCalendar.Unit, from: Date, to: Date, options: NSCalendar.Options) -> DateComponents](nscalendar/components(_:from:to:options:)-84y5w.md)
  Returns the difference between two supplied dates as date components.
- [func components(NSCalendar.Unit, from: DateComponents, to: DateComponents, options: NSCalendar.Options) -> DateComponents](nscalendar/components(_:from:to:options:)-49lo8.md)
  Returns the difference between start and end dates given as date components.
- [func components(in: TimeZone, from: Date) -> DateComponents](nscalendar/components(in:from:).md)
  Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).
- [func getEra(UnsafeMutablePointer<Int>?, year: UnsafeMutablePointer<Int>?, month: UnsafeMutablePointer<Int>?, day: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/getera(_:year:month:day:from:).md)
  Returns by reference the era, year, week of year, and weekday component values for a given date.
- [func getEra(UnsafeMutablePointer<Int>?, yearForWeekOfYear: UnsafeMutablePointer<Int>?, weekOfYear: UnsafeMutablePointer<Int>?, weekday: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/getera(_:yearforweekofyear:weekofyear:weekday:from:).md)
  Returns by reference the era, year, week of year, and weekday component values for a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/gethour(_:minute:second:nanosecond:from:))*