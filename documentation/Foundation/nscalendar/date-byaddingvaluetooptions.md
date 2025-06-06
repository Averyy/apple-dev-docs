# date(byAdding:value:to:options:)

**Framework**: Foundation  
**Kind**: method

Returns a date representing the absolute time calculated by adding the value of a given component to a given date.

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
func date(byAdding unit: NSCalendar.Unit, value: Int, to date: Date, options: NSCalendar.Options = []) -> Date?
```

#### Return Value

A new `NSDate` object representing the absolute time calculated by adding to `date` the `value` of the given calendrical `unit` using the options specified by `options`. Returns `nil` if `date` falls outside the defined range of the receiver or if the computation cannot be performed.

## Parameters

- `unit`: The unit to use for the calculation. For possible values, see  .
- `value`: The value for the given unit.
- `date`: The date to use to perform the calculation.
- `options`: If you specify a “wrap” option ( ), the specified components are incremented and wrap around to zero/one on overflow, but do not cause higher units to be incremented. When the wrap option is false, overflow in a unit carries into the higher units, as in typical addition.

## See Also

- [func date(from: DateComponents) -> Date?](nscalendar/date(from:).md)
  Returns a date representing the absolute time calculated from given components.
- [func date(byAdding: DateComponents, to: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(byadding:to:options:).md)
  Returns a date representing the absolute time calculated by adding given components to a given date.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/date(byadding:value:to:options:))*