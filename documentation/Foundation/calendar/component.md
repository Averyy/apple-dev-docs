# Calendar.Component

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

You use one or more [`Calendar.Component`](./component.md) values with the [`component(_:from:)`](./component%28_,from%29.md) or [`dateComponents(_:from:)`](./datecomponents%28_,from%29.md) methods to specify parts to extract from a given [`Date`](../date.md).

The following code listing shows how to use the year, month, and day components to get the corresponding units of the current Gregorian calendar date as a [`DateComponents`](../datecomponents.md) instance.

```swift
let myCalendar = Calendar(identifier: .gregorian)
let ymd = myCalendar.dateComponents([.year, .month, .day], from: Date())
```

## Topics

### Specifying Years and Months
- [Calendar.Component.era](./component/era.md)
  Identifier for the era unit.
- [Calendar.Component.year](./component/year.md)
  Identifier for the year unit.
- [Calendar.Component.yearForWeekOfYear](./component/yearforweekofyear.md)
  Identifier for the week-counting year unit.
- [Calendar.Component.quarter](./component/quarter.md)
  Identifier for the quarter of the calendar.
- [Calendar.Component.month](./component/month.md)
  Identifier for the month unit.
### Specifying Weeks and Days
- [Calendar.Component.weekOfYear](./component/weekofyear.md)
  Identifier for the week of the year unit.
- [Calendar.Component.weekOfMonth](./component/weekofmonth.md)
  Identifier for the week of the month calendar unit.
- [Calendar.Component.weekday](./component/weekday.md)
  Identifier for the weekday unit.
- [Calendar.Component.weekdayOrdinal](./component/weekdayordinal.md)
  Identifier for the weekday ordinal unit.
- [Calendar.Component.day](./component/day.md)
  Identifier for the day unit.
### Specifying Hours, Minutes, and Seconds
- [Calendar.Component.hour](./component/hour.md)
  Identifier for the hour unit.
- [Calendar.Component.minute](./component/minute.md)
  Identifier for the minute unit.
- [Calendar.Component.second](./component/second.md)
  Identifier for the second unit.
- [Calendar.Component.nanosecond](./component/nanosecond.md)
  Identifier for the nanosecond unit.
### Specifying Calendars and Time Zones
- [Calendar.Component.calendar](./component/calendar.md)
  Identifier for the calendar unit.
- [Calendar.Component.timeZone](./component/timezone.md)
  Identifier for the time zone unit.
### Enumeration Cases
- [Calendar.Component.dayOfYear](./component/dayofyear.md)
- [Calendar.Component.isLeapMonth](./component/isleapmonth.md)
- [Calendar.Component.isRepeatedDay](./component/isrepeatedday.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Extracting Components
- [func date(Date, matchesComponents: DateComponents) -> Bool](./date%28_,matchescomponents%29.md)
  Determines if the date has all of the specified date components.
- [func component(Calendar.Component, from: Date) -> Int](./component%28_,from%29.md)
  Returns the value for one component of a date.
- [func dateComponents(Set<Calendar.Component>, from: Date) -> DateComponents](./datecomponents%28_,from%29.md)
  Returns all the date components of a date, using the calendar time zone.
- [func dateComponents(Set<Calendar.Component>, from: Date, to: Date) -> DateComponents](./datecomponents%28_,from,to%29-2kcg.md)
  Returns the difference between two dates.
- [func dateComponents(Set<Calendar.Component>, from: DateComponents, to: DateComponents) -> DateComponents](./datecomponents%28_,from,to%29-5g20t.md)
  Returns the difference between two dates specified as `DateComponents`.
- [func dateComponents(in: TimeZone, from: Date) -> DateComponents](./datecomponents%28in,from%29.md)
  Returns all the date components of a date, as if in a given time zone (instead of the `Calendar` time zone).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/component)*