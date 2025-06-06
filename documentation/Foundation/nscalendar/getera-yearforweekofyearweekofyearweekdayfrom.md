# getEra(_:yearForWeekOfYear:weekOfYear:weekday:from:)

**Framework**: Foundation  
**Kind**: method

Returns by reference the era, year, week of year, and weekday component values for a given date.

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
func getEra(_ eraValuePointer: UnsafeMutablePointer<Int>?, yearForWeekOfYear yearValuePointer: UnsafeMutablePointer<Int>?, weekOfYear weekValuePointer: UnsafeMutablePointer<Int>?, weekday weekdayValuePointer: UnsafeMutablePointer<Int>?, from date: Date)
```

#### Discussion

Pass `NULL` to ignore any individual component parameter.

This is a convenience method for getting the time components of a given date using [`components(_:from:)`](nscalendar/components(_:from:).md)

## Parameters

- `eraValuePointer`: Upon return, contains the era of the given date.
- `yearValuePointer`: Upon return, contains the year of the given date.
- `weekValuePointer`: Upon return, contains the week of the given date.
- `weekdayValuePointer`: Upon return, contains the weekday of the given date.
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
- [func getHour(UnsafeMutablePointer<Int>?, minute: UnsafeMutablePointer<Int>?, second: UnsafeMutablePointer<Int>?, nanosecond: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/gethour(_:minute:second:nanosecond:from:).md)
  Returns by reference the hour, minute, second, and nanosecond component values for a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/getera(_:yearforweekofyear:weekofyear:weekday:from:))*