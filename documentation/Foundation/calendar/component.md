# Calendar.Component

**Framework**: Foundation  
**Kind**: enum

An enumeration for the various components of a calendar date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Component
```

#### Overview

You use one or more [`Calendar.Component`](calendar/component.md) values with the [`component(_:from:)`](calendar/component(_:from:).md) or [`dateComponents(_:from:)`](calendar/datecomponents(_:from:).md) methods to specify parts to extract from a given [`Date`](date.md).

The following code listing shows how to use the year, month, and day components to get the corresponding units of the current Gregorian calendar date as a [`DateComponents`](datecomponents.md) instance.

```swift
let myCalendar = Calendar(identifier: .gregorian)
let ymd = myCalendar.dateComponents([.year, .month, .day], from: Date())
```

## Topics

### Specifying Years and Months
- [Calendar.Component.era](calendar/component/era.md)
  Identifier for the era unit.
- [Calendar.Component.year](calendar/component/year.md)
  Identifier for the year unit.
- [Calendar.Component.yearForWeekOfYear](calendar/component/yearforweekofyear.md)
  Identifier for the week-counting year unit.
- [Calendar.Component.quarter](calendar/component/quarter.md)
  Identifier for the quarter of the calendar.
- [Calendar.Component.month](calendar/component/month.md)
  Identifier for the month unit.
### Specifying Weeks and Days
- [Calendar.Component.weekOfYear](calendar/component/weekofyear.md)
  Identifier for the week of the year unit.
- [Calendar.Component.weekOfMonth](calendar/component/weekofmonth.md)
  Identifier for the week of the month calendar unit.
- [Calendar.Component.weekday](calendar/component/weekday.md)
  Identifier for the weekday unit.
- [Calendar.Component.weekdayOrdinal](calendar/component/weekdayordinal.md)
  Identifier for the weekday ordinal unit.
- [Calendar.Component.day](calendar/component/day.md)
  Identifier for the day unit.
### Specifying Hours, Minutes, and Seconds
- [Calendar.Component.hour](calendar/component/hour.md)
  Identifier for the hour unit.
- [Calendar.Component.minute](calendar/component/minute.md)
  Identifier for the minute unit.
- [Calendar.Component.second](calendar/component/second.md)
  Identifier for the second unit.
- [Calendar.Component.nanosecond](calendar/component/nanosecond.md)
  Identifier for the nanosecond unit.
### Specifying Calendars and Time Zones
- [Calendar.Component.calendar](calendar/component/calendar.md)
  Identifier for the calendar unit.
- [Calendar.Component.timeZone](calendar/component/timezone.md)
  Identifier for the time zone unit.
### Enumeration Cases
- [Calendar.Component.dayOfYear](calendar/component/dayofyear.md)
- [Calendar.Component.isLeapMonth](calendar/component/isleapmonth.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func date(Date, matchesComponents: DateComponents) -> Bool](calendar/date(_:matchescomponents:).md)
  Determines if the date has all of the specified date components.
- [func component(Calendar.Component, from: Date) -> Int](calendar/component(_:from:).md)
  Returns the value for one component of a date.
- [func dateComponents(Set<Calendar.Component>, from: Date) -> DateComponents](calendar/datecomponents(_:from:).md)
  Returns all the date components of a date, using the calendar time zone.
- [func dateComponents(Set<Calendar.Component>, from: Date, to: Date) -> DateComponents](calendar/datecomponents(_:from:to:)-2kcg.md)
  Returns the difference between two dates.
- [func dateComponents(Set<Calendar.Component>, from: DateComponents, to: DateComponents) -> DateComponents](calendar/datecomponents(_:from:to:)-5g20t.md)
  Returns the difference between two dates specified as `DateComponents`.
- [func dateComponents(in: TimeZone, from: Date) -> DateComponents](calendar/datecomponents(in:from:).md)
  Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/component)*