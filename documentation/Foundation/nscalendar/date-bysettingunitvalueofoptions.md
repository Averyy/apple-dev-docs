# date(bySettingUnit:value:of:options:)

**Framework**: Foundation  
**Kind**: method

Returns a new date representing the date calculated by setting a specific component of a given date to a given value, while trying to keep lower components the same.

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
func date(bySettingUnit unit: NSCalendar.Unit, value v: Int, of date: Date, options opts: NSCalendar.Options = []) -> Date?
```

#### Return Value

A new `NSDate` instance representing the date calculated by setting a specific component of a given date to a given value. If the unit already has that value, this may result in a date which is the same as the given date. If no such time exists for the specified components, the next available date is returned, which may be on a different calendar day.

#### Discussion

Changing a component’s value often requires higher or coupled components to change as well. For example, setting the `weekday` to “Thursday” will require the `day` component to change its value, and possibly the `month` and `year` as well. You can use the [`nextDate(after:matching:value:options:)`](nscalendar/nextdate(after:matching:value:options:).md) method to specify more precise behavior for determining the next or previous date for a given date component.

## Parameters

- `unit`: The unit to set with the given value. For possible values, see  .
- `v`: The value to set for the given calendar unit.
- `date`: The date to use to perform the calculation.
- `opts`: Options for the calculation. For possible values, see  .

## See Also

- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:value:options:).md)
  Returns the next date after a given date matching the given calendar unit value.
- [func date(from: DateComponents) -> Date?](nscalendar/date(from:).md)
  Returns a date representing the absolute time calculated from given components.
- [func date(byAdding: DateComponents, to: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(byadding:to:options:).md)
  Returns a date representing the absolute time calculated by adding given components to a given date.
- [func date(byAdding: NSCalendar.Unit, value: Int, to: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(byadding:value:to:options:).md)
  Returns a date representing the absolute time calculated by adding the value of a given component to a given date.
- [func date(bySettingHour: Int, minute: Int, second: Int, of: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(bysettinghour:minute:second:of:options:).md)
  Creates a new date calculated with the given time.
- [func date(era: Int, year: Int, month: Int, day: Int, hour: Int, minute: Int, second: Int, nanosecond: Int) -> Date?](nscalendar/date(era:year:month:day:hour:minute:second:nanosecond:).md)
  Returns a date created with the given components.
- [func date(era: Int, yearForWeekOfYear: Int, weekOfYear: Int, weekday: Int, hour: Int, minute: Int, second: Int, nanosecond: Int) -> Date?](nscalendar/date(era:yearforweekofyear:weekofyear:weekday:hour:minute:second:nanosecond:).md)
  Returns a new date created with the given components base on a week-of-year value.
- [func nextWeekendStart(AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, options: NSCalendar.Options, after: Date) -> Bool](nscalendar/nextweekendstart(_:interval:options:after:).md)
  Returns by reference the starting date and time interval range of the next weekend period after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/date(bysettingunit:value:of:options:))*