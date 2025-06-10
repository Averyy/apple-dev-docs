# NSDateComponents

**Framework**: Foundation  
**Kind**: class

An object that specifies a date or time in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.

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
class NSDateComponents
```

#### Overview

In Swift, this object bridges to [`DateComponents`](datecomponents.md); use [`NSDateComponents`](nsdatecomponents.md) when you need reference semantics or other Foundation-specific behavior.

[`NSDateComponents`](nsdatecomponents.md) encapsulates the components of a date in an extendable, object-oriented manner. It’s used to specify a date by providing the temporal components that make up a date and time: hour, minutes, seconds, day, month, year, and so on. You can also use it to specify a duration of time, for example, 5 hours and 16 minutes. An [`NSDateComponents`](nsdatecomponents.md) object is not required to define all the component fields. When a new instance of [`NSDateComponents`](nsdatecomponents.md) is created, the date components are set to [`NSDateComponentUndefined`](nsdatecomponentundefined.md).

> ❗ **Important**:  An [`NSDateComponents`](nsdatecomponents.md) object is meaningless in itself; you need to know what calendar it is interpreted against, and you need to know whether the values are absolute values of the units, or quantities of the units.

An instance of [`NSDateComponents`](nsdatecomponents.md) is not responsible for answering questions about a date beyond the information with which it was initialized. For example, if you initialize one with May 4, 2017, its weekday is [`NSDateComponentUndefined`](nsdatecomponentundefined.md), not Thursday. To get the correct day of the week, you must create a suitable instance of [`NSCalendar`](nscalendar.md), create an [`NSDate`](nsdate.md) object using [`date(from:)`](nscalendar/date(from:).md) and then use [`components(_:from:)`](nscalendar/components(_:from:).md) to retrieve the weekday—as illustrated in the following example.

For more details, see [`Calendars, Date Components, and Calendar Units`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [`Date and Time Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`DateComponents`](datecomponents.md) structure, which bridges to the [`NSDateComponents`](nsdatecomponents.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Setting a Calendar and Time Zone
- [var calendar: Calendar?](nsdatecomponents/calendar.md)
  The calendar used to interpret the date components.
- [var timeZone: TimeZone?](nsdatecomponents/timezone.md)
  The time zone used to interpret the date components.
### Validating a Date
- [var isValidDate: Bool](nsdatecomponents/isvaliddate.md)
  A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.
- [func isValidDate(in: Calendar) -> Bool](nsdatecomponents/isvaliddate(in:).md)
  Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [var date: Date?](nsdatecomponents/date.md)
  The date calculated from the current components using the stored calendar.
- [Undefined Components](1430344-undefined-components.md)
  Constants that denote that the value of a date component is undefined.
### Accessing Years and Months
- [var era: Int](nsdatecomponents/era.md)
  The number of eras.
- [var year: Int](nsdatecomponents/year.md)
  The number of years.
- [var yearForWeekOfYear: Int](nsdatecomponents/yearforweekofyear.md)
  The ISO 8601 week-numbering year.
- [var quarter: Int](nsdatecomponents/quarter.md)
  The number of quarters.
- [var month: Int](nsdatecomponents/month.md)
  The number of months.
- [var isLeapMonth: Bool](nsdatecomponents/isleapmonth.md)
  A Boolean value that indicates whether the month is a leap month.
### Accessing Weeks and Days
- [var weekday: Int](nsdatecomponents/weekday.md)
  The number of the weekdays.
- [var weekdayOrdinal: Int](nsdatecomponents/weekdayordinal.md)
  The ordinal number of weekdays.
- [var weekOfMonth: Int](nsdatecomponents/weekofmonth.md)
  The week number of the months.
- [var weekOfYear: Int](nsdatecomponents/weekofyear.md)
  The ISO 8601 week date of the year.
- [var day: Int](nsdatecomponents/day.md)
  The number of days.
- [func week() -> Int](nsdatecomponents/week.md)
  Returns the number of weeks.
- [func setWeek(Int)](nsdatecomponents/setweek(_:).md)
  Sets the number of weeks.
### Accessing Hours and Seconds
- [var hour: Int](nsdatecomponents/hour.md)
  The number of hour units for the receiver.
- [var minute: Int](nsdatecomponents/minute.md)
  The number of minute units for the receiver.
- [var second: Int](nsdatecomponents/second.md)
  The number of second units for the receiver.
- [var nanosecond: Int](nsdatecomponents/nanosecond.md)
  The number of nanosecond units for the receiver.
### Accessing Components as Calendrical Units
- [func value(forComponent: NSCalendar.Unit) -> Int](nsdatecomponents/value(forcomponent:).md)
  Returns the value for a given calendar unit.
- [func setValue(Int, forComponent: NSCalendar.Unit)](nsdatecomponents/setvalue(_:forcomponent:).md)
  Sets a value for a given calendar unit.
- [NSCalendar.Unit](nscalendar/unit.md)
  Calendrical units such as year, month, day and hour.
### Instance Properties
- [var dayOfYear: Int](nsdatecomponents/dayofyear.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents)*