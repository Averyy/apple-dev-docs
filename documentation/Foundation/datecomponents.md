# DateComponents

**Framework**: Foundation  
**Kind**: struct

A date or time specified in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct DateComponents
```

#### Overview

`DateComponents` encapsulates the components of a date in an extendable, structured manner.

It is used to specify a date by providing the temporal components that make up a date and time in a particular calendar: hour, minutes, seconds, day, month, year, and so on. It can also be used to specify a duration of time, for example, 5 hours and 16 minutes. A `DateComponents` is not required to define all the component fields.

When a new instance of `DateComponents` is created, the date components are set to `nil`.

## Topics

### Initializing Date Components
- [init(calendar: Calendar?, timeZone: TimeZone?, era: Int?, year: Int?, month: Int?, day: Int?, hour: Int?, minute: Int?, second: Int?, nanosecond: Int?, weekday: Int?, weekdayOrdinal: Int?, quarter: Int?, weekOfMonth: Int?, weekOfYear: Int?, yearForWeekOfYear: Int?)](datecomponents/init(calendar:timezone:era:year:month:day:hour:minute:second:nanosecond:weekday:weekdayordinal:quarter:weekofmonth:weekofyear:yearforweekofyear:).md)
  Initializes a date components value, optionally specifying values for its fields.
- [var calendar: Calendar?](datecomponents/calendar.md)
  The calendar used to interpret the other values in this structure.
- [var timeZone: TimeZone?](datecomponents/timezone.md)
  A time zone.
### Validating a Date
- [var isValidDate: Bool](datecomponents/isvaliddate.md)
  Indicates whether the current combination of properties represents a date which exists in the current calendar.
- [func isValidDate(in: Calendar) -> Bool](datecomponents/isvaliddate(in:).md)
  Indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [var date: Date?](datecomponents/date.md)
  The date calculated from the current components using the stored calendar.
### Accessing Months and Years
- [var era: Int?](datecomponents/era.md)
  An era or count of eras.
- [var year: Int?](datecomponents/year.md)
  A year or count of years.
- [var yearForWeekOfYear: Int?](datecomponents/yearforweekofyear.md)
  The year corresponding to a week-counting week.
- [var quarter: Int?](datecomponents/quarter.md)
  A quarter or count of quarters.
- [var month: Int?](datecomponents/month.md)
  A month or count of months.
- [var isLeapMonth: Bool?](datecomponents/isleapmonth.md)
  Set to true if these components represent a leap month.
### Accessing Weeks and Days
- [var weekOfMonth: Int?](datecomponents/weekofmonth.md)
  A week of the month or a count of weeks of the month.
- [var weekOfYear: Int?](datecomponents/weekofyear.md)
  A week of the year or count of the weeks of the year.
- [var weekday: Int?](datecomponents/weekday.md)
  A weekday or count of weekdays.
- [var weekdayOrdinal: Int?](datecomponents/weekdayordinal.md)
  A weekday ordinal or count of weekday ordinals.
- [var day: Int?](datecomponents/day.md)
  A day or count of days.
### Accessing Hours and Seconds
- [var hour: Int?](datecomponents/hour.md)
  An hour or count of hours.
- [var minute: Int?](datecomponents/minute.md)
  A minute or count of minutes.
- [var second: Int?](datecomponents/second.md)
  A second or count of seconds.
- [var nanosecond: Int?](datecomponents/nanosecond.md)
  A nanosecond or count of nanoseconds.
### Accessing Calendar Components
- [func value(for: Calendar.Component) -> Int?](datecomponents/value(for:).md)
  Returns the value of one of the properties, using an enumeration value instead of a property name.
- [func setValue(Int?, for: Calendar.Component)](datecomponents/setvalue(_:for:).md)
  Set the value of one of the properties, using an enumeration value instead of a property name.
- [Calendar.Component](calendar/component.md)
  An enumeration for the various components of a calendar date.
### Comparing Date Components
- [static func != (Self, Self) -> Bool](datecomponents/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Using Reference Types
- [class NSDateComponents](nsdatecomponents.md)
  An object that specifies a date or time in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.
### Initializers
- [init(subscriptionPeriod: Product.SubscriptionPeriod)](datecomponents/init(subscriptionperiod:).md)
### Instance Properties
- [var dayOfYear: Int?](datecomponents/dayofyear.md)
### Type Aliases
- [DateComponents.Specification](datecomponents/specification.md)
- [DateComponents.UnwrappedType](datecomponents/unwrappedtype.md)
- [DateComponents.ValueType](datecomponents/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](datecomponents/defaultresolverspecification.md)
### Default Implementations
- [Equatable Implementations](datecomponents/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Calendar](calendar.md)
  A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.
- [struct TimeZone](timezone.md)
  Information about standard time conventions associated with a specific geopolitical region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents)*