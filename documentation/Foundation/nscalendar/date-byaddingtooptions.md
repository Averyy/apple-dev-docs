# date(byAdding:to:options:)

**Framework**: Foundation  
**Kind**: method

Returns a date representing the absolute time calculated by adding given components to a given date.

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
func date(byAdding comps: DateComponents, to date: Date, options opts: NSCalendar.Options = []) -> Date?
```

#### Return Value

A new `NSDate` object representing the absolute time calculated by adding to `date` the calendrical components specified by `comps` using the options specified by `opts`. Returns `nil` if `date` falls outside the defined range of the receiver or if the computation cannot be performed.

#### Discussion

Some operations can be ambiguous, and the behavior of the computation is calendar-specific, but generally components are added in the order specified.

The following example shows how to add 2 months and 3 days to the current date and time using an existing calendar (`gregorian`):

```objc
NSDate *currentDate = [NSDate date];
NSDateComponents *comps = [[NSDateComponents alloc] init];
[comps setMonth:2];
[comps setDay:3];
NSDate *date = [gregorian dateByAddingComponents:comps toDate:currentDate options:0];
[comps release];
```

Note that some computations can take a relatively long time.

## Parameters

- `comps`: The components to add to  .
- `date`: The date to which   are added.
- `opts`: If you specify no options, overflow in a unit carries into the higher units (as in typical addition).

## See Also

- [func components(NSCalendar.Unit, from: Date, to: Date, options: NSCalendar.Options) -> DateComponents](nscalendar/components(_:from:to:options:)-84y5w.md)
  Returns the difference between two supplied dates as date components.
- [func date(from: DateComponents) -> Date?](nscalendar/date(from:).md)
  Returns a date representing the absolute time calculated from given components.
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
- [func nextWeekendStart(AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, options: NSCalendar.Options, after: Date) -> Bool](nscalendar/nextweekendstart(_:interval:options:after:).md)
  Returns by reference the starting date and time interval range of the next weekend period after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/date(byadding:to:options:))*