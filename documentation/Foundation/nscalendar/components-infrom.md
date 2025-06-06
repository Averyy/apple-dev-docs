# components(in:from:)

**Framework**: Foundation  
**Kind**: method

Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).

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
func components(in timezone: TimeZone, from date: Date) -> DateComponents
```

#### Return Value

An `NSDateComponents` object containing all the components from the given date, calculated using the given time zone.

#### Discussion

If you want “date information in a given time zone” for the purpose to displaying it, you should use [`DateFormatter`](dateformatter.md) to format the date.

## Parameters

- `timezone`: The time zone to use when returning the components. This value overrides the time zone of the receiving  .
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
- [func getEra(UnsafeMutablePointer<Int>?, year: UnsafeMutablePointer<Int>?, month: UnsafeMutablePointer<Int>?, day: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/getera(_:year:month:day:from:).md)
  Returns by reference the era, year, week of year, and weekday component values for a given date.
- [func getEra(UnsafeMutablePointer<Int>?, yearForWeekOfYear: UnsafeMutablePointer<Int>?, weekOfYear: UnsafeMutablePointer<Int>?, weekday: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/getera(_:yearforweekofyear:weekofyear:weekday:from:).md)
  Returns by reference the era, year, week of year, and weekday component values for a given date.
- [func getHour(UnsafeMutablePointer<Int>?, minute: UnsafeMutablePointer<Int>?, second: UnsafeMutablePointer<Int>?, nanosecond: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/gethour(_:minute:second:nanosecond:from:).md)
  Returns by reference the hour, minute, second, and nanosecond component values for a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/components(in:from:))*