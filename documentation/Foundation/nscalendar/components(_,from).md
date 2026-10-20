# components(_:from:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the date components representing a given date.

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
func components(_ unitFlags: NSCalendar.Unit, from date: Date) -> DateComponents
```

```objc
- (NSDateComponents *) components:(NSCalendarUnit) unitFlags fromDate:(NSDate *) date;
```

#### Return Value

An `NSDateComponents` object containing `date` decomposed into the components specified by `unitFlags`. Returns `nil` if `date` falls outside of the defined range of the receiver or if the computation cannot be performed.

#### Discussion

The Weekday ordinality, when requested, refers to the next larger (than Week) of the requested units. Some computations can take a relatively long time.

The following example shows how to use this method to determine the current year, month, and day, using an existing calendar (`gregorian`):

```objc
unsigned unitFlags = NSYearCalendarUnit | NSMonthCalendarUnit |  NSDayCalendarUnit;
NSDate *date = [NSDate date];
NSDateComponents *comps = [gregorian components:unitFlags fromDate:date];
```

## Parameters

- `unitFlags`: The components into which to decompose `date`.
- `date`: The date for which to perform the calculation.

## See Also

### Related Documentation
- [func date(from: DateComponents) -> Date?](./date%28from%29.md)
  Returns a date representing the absolute time calculated from given components.
- [func date(byAdding: DateComponents, to: Date, options: NSCalendar.Options) -> Date?](./date%28byadding,to,options%29.md)
  Returns a date representing the absolute time calculated by adding given components to a given date.
### Extracting Components
- [func date(Date, matchesComponents: DateComponents) -> Bool](./date%28_,matchescomponents%29.md)
  Returns whether a given date matches all of the given date components.
- [func component(NSCalendar.Unit, from: Date) -> Int](./component%28_,from%29.md)
  Returns the specified date component from a given date.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/components(_:from:))*