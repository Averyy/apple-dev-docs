# component(_:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the specified date component from a given date.

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
func component(_ unit: NSCalendar.Unit, from date: Date) -> Int
```

```objc
- (NSInteger) component:(NSCalendarUnit) unit fromDate:(NSDate *) date;
```

## Return Value

An `NSInteger` value for the requested component.

## Parameters

- `unit`: The component to return. For possible values, see [`NSCalendar.Unit`](./unit.md).
- `date`: The date for which to perform the calculation.

## See Also

### Extracting Components
- [func date(Date, matchesComponents: DateComponents) -> Bool](./date%28_,matchescomponents%29.md)
  Returns whether a given date matches all of the given date components.
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
- [func getHour(UnsafeMutablePointer<Int>?, minute: UnsafeMutablePointer<Int>?, second: UnsafeMutablePointer<Int>?, nanosecond: UnsafeMutablePointer<Int>?, from: Date)](./gethour%28_,minute,second,nanosecond,from%29.md)
  Returns by reference the hour, minute, second, and nanosecond component values for a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/component(_:from:))*