# getHour(_:minute:second:nanosecond:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) getHour:(NSInteger *) hourValuePointer minute:(NSInteger *) minuteValuePointer second:(NSInteger *) secondValuePointer nanosecond:(NSInteger *) nanosecondValuePointer fromDate:(NSDate *) date;
```

#### Discussion

Pass `NULL` to ignore any individual component parameter.

This is a convenience method for getting the time components of a given date using [`components(_:from:)`](./components%28_,from%29.md)

## Parameters

- `hourValuePointer`: Upon return, contains the hour of the given date.
- `minuteValuePointer`: Upon return, contains the minute of the given date.
- `secondValuePointer`: Upon return, contains the second of the given date.
- `nanosecondValuePointer`: Upon return, contains the nanosecond of the given date.
- `date`: The date for which to perform the calculation.

## See Also

### Extracting Components
- [func date(Date, matchesComponents: DateComponents) -> Bool](./date%28_,matchescomponents%29.md)
  Returns whether a given date matches all of the given date components.
- [func component(NSCalendar.Unit, from: Date) -> Int](./component%28_,from%29.md)
  Returns the specified date component from a given date.
- [func components(NSCalendar.Unit, from: Date) -> DateComponents](./components%28_,from%29.md)
  Returns the date components representing a given date.
- [func components(NSCalendar.Unit, from: Date, to: Date, options: NSCalendar.Options) -> DateComponents](./components%28_,from,to,options%29-84y5w.md)
  Returns the difference between two supplied dates as date components.
- [func components(NSCalendar.Unit, from: DateComponents, to: DateComponents, options: NSCalendar.Options) -> DateComponents](./components%28_,from,to,options%29-49lo8.md)
  Returns the difference between start and end dates given as date components.
- [func components(in: TimeZone, from: Date) -> DateComponents](./components%28in,from%29.md)
  Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).
- [func getEra(UnsafeMutablePointer<Int>?, year: UnsafeMutablePointer<Int>?, month: UnsafeMutablePointer<Int>?, day: UnsafeMutablePointer<Int>?, from: Date)](./getera%28_,year,month,day,from%29.md)
  Returns by reference the era, year, week of year, and weekday component values for a given date.
- [func getEra(UnsafeMutablePointer<Int>?, yearForWeekOfYear: UnsafeMutablePointer<Int>?, weekOfYear: UnsafeMutablePointer<Int>?, weekday: UnsafeMutablePointer<Int>?, from: Date)](./getera%28_,yearforweekofyear,weekofyear,weekday,from%29.md)
  Returns by reference the era, year, week of year, and weekday component values for a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/gethour(_:minute:second:nanosecond:from:))*