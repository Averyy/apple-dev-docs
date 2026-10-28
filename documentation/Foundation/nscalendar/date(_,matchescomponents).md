# date(_:matchesComponents:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns whether a given date matches all of the given date components.

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
func date(_ date: Date, matchesComponents components: DateComponents) -> Bool
```

```objc
- (BOOL) date:(NSDate *) date matchesComponents:(NSDateComponents *) components;
```

## Return Value

[`true`](../../Swift/true.md) if the given date matches the given components, otherwise [`false`](../../Swift/false.md).

## Discussion

This method is useful for determining whether dates calculated by methods like  [`nextDate(after:matching:value:options:)`](./nextdate%28after,matching,value,options%29.md) or [`enumerateDates(startingAfter:matching:options:using:)`](./enumeratedates%28startingafter,matching,options,using%29.md) are exact, or required an adjustment due to a nonexistent time.

## Parameters

- `date`: The date for which to perform the calculation.
- `components`: The date components to match.

## See Also

### Related Documentation
- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](./nextdate%28after,matching,value,options%29.md)
  Returns the next date after a given date matching the given calendar unit value.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratedates%28startingafter,matching,options,using%29.md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
### Extracting Components
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
- [func getHour(UnsafeMutablePointer<Int>?, minute: UnsafeMutablePointer<Int>?, second: UnsafeMutablePointer<Int>?, nanosecond: UnsafeMutablePointer<Int>?, from: Date)](./gethour%28_,minute,second,nanosecond,from%29.md)
  Returns by reference the hour, minute, second, and nanosecond component values for a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/date(_:matchescomponents:))*