# components(_:from:to:options:)

**Framework**: Foundation  
**Kind**: method

Returns the difference between two supplied dates as date components.

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
func components(_ unitFlags: NSCalendar.Unit, from startingDate: Date, to resultDate: Date, options opts: NSCalendar.Options = []) -> DateComponents
```

#### Return Value

An `NSDateComponents` object whose components are specified by `unitFlags` and calculated from the difference between the `resultDate` and `startDate` using the options specified by `options`. Returns `nil` if either date falls outside the defined range of the receiver or if the computation cannot be performed.

#### Discussion

The result is lossy if there is not a small enough unit requested to hold the full precision of the difference. Some operations can be ambiguous, and the behavior of the computation is calendar-specific, but generally larger components will be computed before smaller components; for example, in the Gregorian calendar a result might be 1 month and 5 days instead of, for example, 0 months and 35 days. The resulting component values may be negative if `resultDate` is before `startDate`.

The following example shows how to get the approximate number of months and days between two dates using an existing calendar (`gregorian`):

```objc
NSDate *startDate = ...;
NSDate *endDate = ...;
unsigned int unitFlags = NSMonthCalendarUnit | NSDayCalendarUnit;
NSDateComponents *comps = [gregorian components:unitFlags fromDate:startDate  toDate:endDate  options:0];
int months = [comps month];
int days = [comps day];
```

Note that some computations can take a relatively long time.

## Parameters

- `unitFlags`: Specifies the components for the returned   object.
- `startingDate`: The start date for the calculation.
- `resultDate`: The end date for the calculation.
- `opts`: If you specify a “wrap” option ( ), the specified components are incremented and wrap around to zero/one on overflow, but do not cause higher units to be incremented. When the wrap option is not specified, overflow in a unit carries into the higher units, as in typical addition.

## See Also

- [func date(from: DateComponents) -> Date?](nscalendar/date(from:).md)
  Returns a date representing the absolute time calculated from given components.
- [func date(byAdding: DateComponents, to: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(byadding:to:options:).md)
  Returns a date representing the absolute time calculated by adding given components to a given date.
- [func date(Date, matchesComponents: DateComponents) -> Bool](nscalendar/date(_:matchescomponents:).md)
  Returns whether a given date matches all of the given date components.
- [func component(NSCalendar.Unit, from: Date) -> Int](nscalendar/component(_:from:).md)
  Returns the specified date component from a given date.
- [func components(NSCalendar.Unit, from: Date) -> DateComponents](nscalendar/components(_:from:).md)
  Returns the date components representing a given date.
- [func components(NSCalendar.Unit, from: DateComponents, to: DateComponents, options: NSCalendar.Options) -> DateComponents](nscalendar/components(_:from:to:options:)-49lo8.md)
  Returns the difference between start and end dates given as date components.
- [func components(in: TimeZone, from: Date) -> DateComponents](nscalendar/components(in:from:).md)
  Returns all the date components of a date, as if in a given time zone (instead of the receiving calendar’s time zone).
- [func getEra(UnsafeMutablePointer<Int>?, year: UnsafeMutablePointer<Int>?, month: UnsafeMutablePointer<Int>?, day: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/getera(_:year:month:day:from:).md)
  Returns by reference the era, year, week of year, and weekday component values for a given date.
- [func getEra(UnsafeMutablePointer<Int>?, yearForWeekOfYear: UnsafeMutablePointer<Int>?, weekOfYear: UnsafeMutablePointer<Int>?, weekday: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/getera(_:yearforweekofyear:weekofyear:weekday:from:).md)
  Returns by reference the era, year, week of year, and weekday component values for a given date.
- [func getHour(UnsafeMutablePointer<Int>?, minute: UnsafeMutablePointer<Int>?, second: UnsafeMutablePointer<Int>?, nanosecond: UnsafeMutablePointer<Int>?, from: Date)](nscalendar/gethour(_:minute:second:nanosecond:from:).md)
  Returns by reference the hour, minute, second, and nanosecond component values for a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/components(_:from:to:options:)-84y5w)*