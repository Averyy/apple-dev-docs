# Calendar

**Framework**: Foundation  
**Kind**: struct

A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.

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
struct Calendar
```

#### Overview

`Calendar` encapsulates information about systems of reckoning time in which the beginning, length, and divisions of a year are defined. It provides information about the calendar and support for calendrical computations such as determining the range of a given calendrical unit and adding units to a given absolute time.

## Topics

### Creating a Calendar
- [Calendar.Identifier](calendar/identifier-swift.enum.md)
  An enumeration for the available calendars.
### Getting the User’s Calendar
- [static var autoupdatingCurrent: Calendar](calendar/autoupdatingcurrent.md)
  A calendar that tracks changes to user’s preferred calendar.
- [static var current: Calendar](calendar/current.md)
  The user’s current calendar.
### Extracting Components
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
- [Calendar.Component](calendar/component.md)
  An enumeration for the various components of a calendar date.
### Getting Calendar Information
- [var identifier: Calendar.Identifier](calendar/identifier-swift.property.md)
  The identifier of the calendar.
- [var locale: Locale?](calendar/locale.md)
  The locale of the calendar.
- [var firstWeekday: Int](calendar/firstweekday.md)
  The first day of the week for the calendar.
- [var minimumDaysInFirstWeek: Int](calendar/minimumdaysinfirstweek.md)
  The number of minimum days in the first week.
- [var timeZone: TimeZone](calendar/timezone.md)
  The time zone of the calendar.
- [func maximumRange(of: Calendar.Component) -> Range<Int>?](calendar/maximumrange(of:).md)
  The maximum range limits of the values that a given component can take on.
- [func minimumRange(of: Calendar.Component) -> Range<Int>?](calendar/minimumrange(of:).md)
  Returns the minimum range limits of the values that a given component can take on.
- [func ordinality(of: Calendar.Component, in: Calendar.Component, for: Date) -> Int?](calendar/ordinality(of:in:for:).md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).
- [func range(of: Calendar.Component, in: Calendar.Component, for: Date) -> Range<Int>?](calendar/range(of:in:for:).md)
  Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.
### Scanning Dates
- [func startOfDay(for: Date) -> Date](calendar/startofday(for:).md)
  Returns the first moment of a given Date, as a Date.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection, using: (Date?, Bool, inout Bool) -> Void)](calendar/enumeratedates(startingafter:matching:matchingpolicy:repeatedtimepolicy:direction:using:).md)
  Computes the dates which match (or most closely match) a given set of components, and calls the closure once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection) -> Date?](calendar/nextdate(after:matching:matchingpolicy:repeatedtimepolicy:direction:).md)
  Computes the next date which matches (or most closely matches) a given set of components.
- [Calendar.MatchingPolicy](calendar/matchingpolicy.md)
  A hint to the search algorithm to control the method used for searching for dates.
- [Calendar.RepeatedTimePolicy](calendar/repeatedtimepolicy.md)
  Determines which result to use when a time is repeated on a day in a calendar (for example, during a daylight saving transition when the times between 2:00am and 3:00am may happen twice).
### Calculating Dates from Components
- [func date(from: DateComponents) -> Date?](calendar/date(from:).md)
  Returns a date created from the specified components.
- [func date(byAdding: DateComponents, to: Date, wrappingComponents: Bool) -> Date?](calendar/date(byadding:to:wrappingcomponents:).md)
  Returns a new `Date` representing the date calculated by adding components to a given date.
- [func date(byAdding: Calendar.Component, value: Int, to: Date, wrappingComponents: Bool) -> Date?](calendar/date(byadding:value:to:wrappingcomponents:).md)
  Returns a new `Date` representing the date calculated by adding an amount of a specific component to a given date.
- [func date(bySetting: Calendar.Component, value: Int, of: Date) -> Date?](calendar/date(bysetting:value:of:).md)
  Returns a new `Date` representing the date calculated by setting a specific component to a given time, and trying to keep lower components the same.  If the component already has that value, this may result in a date which is the same as the given date.
- [func date(bySettingHour: Int, minute: Int, second: Int, of: Date, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection) -> Date?](calendar/date(bysettinghour:minute:second:of:matchingpolicy:repeatedtimepolicy:direction:).md)
  Returns a new `Date` representing the date calculated by setting hour, minute, and second to a given time on a specified `Date`.
### Calculating Intervals
- [func dateInterval(of: Calendar.Component, for: Date) -> DateInterval?](calendar/dateinterval(of:for:).md)
  Returns the starting time and duration of a given calendar component that contains a given date.
- [func dateInterval(of: Calendar.Component, start: inout Date, interval: inout TimeInterval, for: Date) -> Bool](calendar/dateinterval(of:start:interval:for:).md)
  Returns, via two inout parameters, the starting time and duration of a given calendar component that contains a given date.
- [func dateIntervalOfWeekend(containing: Date) -> DateInterval?](calendar/dateintervalofweekend(containing:).md)
  Returns a `DateInterval` of the weekend contained by the given date, or `nil` if the date is not in a weekend.
- [func dateIntervalOfWeekend(containing: Date, start: inout Date, interval: inout TimeInterval) -> Bool](calendar/dateintervalofweekend(containing:start:interval:).md)
  Find the range of the weekend around the given date, returned via two by-reference parameters.
- [func nextWeekend(startingAfter: Date, direction: Calendar.SearchDirection) -> DateInterval?](calendar/nextweekend(startingafter:direction:).md)
  Returns a `DateInterval` of the next weekend, which starts strictly after the given date.
- [func nextWeekend(startingAfter: Date, start: inout Date, interval: inout TimeInterval, direction: Calendar.SearchDirection) -> Bool](calendar/nextweekend(startingafter:start:interval:direction:).md)
  Returns the range of the next weekend via two inout parameters. The weekend starts strictly after the given date.
- [Calendar.SearchDirection](calendar/searchdirection.md)
  The direction in time to search.
### Comparing Dates
- [func compare(Date, to: Date, toGranularity: Calendar.Component) -> ComparisonResult](calendar/compare(_:to:togranularity:).md)
  Compares two dates down to the specified component.
- [func isDate(Date, equalTo: Date, toGranularity: Calendar.Component) -> Bool](calendar/isdate(_:equalto:togranularity:).md)
  Returns a Boolean value indicating whether two dates are equal down to the specified component.
- [func isDate(Date, inSameDayAs: Date) -> Bool](calendar/isdate(_:insamedayas:).md)
  Returns a Boolean value indicating whether a date is within the same day as another date.
- [func isDateInToday(Date) -> Bool](calendar/isdateintoday(_:).md)
  Returns a Boolean value indicating whether the given date is within today.
- [func isDateInTomorrow(Date) -> Bool](calendar/isdateintomorrow(_:).md)
  Returns a Boolean value indicating whether the given date is within tomorrow.
- [func isDateInYesterday(Date) -> Bool](calendar/isdateinyesterday(_:).md)
  Returns a Boolean value indicating whether the given date is within yesterday.
- [func isDateInWeekend(Date) -> Bool](calendar/isdateinweekend(_:).md)
  Returns a Boolean value indicating whether the given date is within a weekend period.
### Getting AM and PM symbols
- [var amSymbol: String](calendar/amsymbol.md)
  The symbol used to represent “AM”, localized to the Calendar’s `locale`.
- [var pmSymbol: String](calendar/pmsymbol.md)
  The symbol used to represent “PM”, localized to the Calendar’s `locale`.
### Getting Weekday Symbols
- [var weekdaySymbols: [String]](calendar/weekdaysymbols.md)
  A list of weekdays in this calendar, localized to the Calendar’s `locale`.
- [var shortWeekdaySymbols: [String]](calendar/shortweekdaysymbols.md)
  A list of shorter-named weekdays in this calendar, localized to the Calendar’s `locale`.
- [var veryShortWeekdaySymbols: [String]](calendar/veryshortweekdaysymbols.md)
  A list of very-shortly-named weekdays in this calendar, localized to the Calendar’s `locale`.
- [var standaloneWeekdaySymbols: [String]](calendar/standaloneweekdaysymbols.md)
  A list of standalone weekday names in this calendar, localized to the Calendar’s `locale`.
- [var shortStandaloneWeekdaySymbols: [String]](calendar/shortstandaloneweekdaysymbols.md)
  A list of shorter-named standalone weekdays in this calendar, localized to the Calendar’s `locale`.
- [var veryShortStandaloneWeekdaySymbols: [String]](calendar/veryshortstandaloneweekdaysymbols.md)
  A list of very-shortly-named weekdays in this calendar, localized to the Calendar’s `locale`.
### Getting Month Symbols
- [var monthSymbols: [String]](calendar/monthsymbols.md)
  A list of months in this calendar, localized to the Calendar’s `locale`.
- [var shortMonthSymbols: [String]](calendar/shortmonthsymbols.md)
  A list of shorter-named months in this calendar, localized to the Calendar’s `locale`.
- [var veryShortMonthSymbols: [String]](calendar/veryshortmonthsymbols.md)
  A list of very-shortly-named months in this calendar, localized to the Calendar’s `locale`.
- [var standaloneMonthSymbols: [String]](calendar/standalonemonthsymbols.md)
  A list of standalone months in this calendar, localized to the Calendar’s `locale`.
- [var shortStandaloneMonthSymbols: [String]](calendar/shortstandalonemonthsymbols.md)
  A list of shorter-named standalone months in this calendar, localized to the Calendar’s `locale`.
- [var veryShortStandaloneMonthSymbols: [String]](calendar/veryshortstandalonemonthsymbols.md)
  A list of very-shortly-named standalone months in this calendar, localized to the Calendar’s `locale`.
### Getting Quarter Symbols
- [var quarterSymbols: [String]](calendar/quartersymbols.md)
  A list of quarter names in this calendar, localized to the Calendar’s `locale`.
- [var shortQuarterSymbols: [String]](calendar/shortquartersymbols.md)
  A list of shorter-named quarters in this calendar, localized to the Calendar’s `locale`.
- [var standaloneQuarterSymbols: [String]](calendar/standalonequartersymbols.md)
  A list of standalone quarter names in this calendar, localized to the Calendar’s `locale`.
- [var shortStandaloneQuarterSymbols: [String]](calendar/shortstandalonequartersymbols.md)
  A list of shorter-named standalone quarters in this calendar, localized to the Calendar’s `locale`.
### Getting Era Symbols
- [var eraSymbols: [String]](calendar/erasymbols.md)
  A list of eras in this calendar, localized to the Calendar’s `locale`.
- [var longEraSymbols: [String]](calendar/longerasymbols.md)
  A list of longer-named eras in this calendar, localized to the Calendar’s `locale`.
### Working with notification messages
- [Calendar.CalendarDayChangedMessage](calendar/calendardaychangedmessage.md)
### Using Reference Types
- [class NSCalendar](nscalendar.md)
  A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.
### Structures
- [Calendar.RecurrenceRule](calendar/recurrencerule.md)
  A rule which specifies how often an event should repeat in the future
### Initializers
- [init(identifier: Calendar.Identifier)](calendar/init(identifier:).md)
  Returns a new Calendar.
### Instance Methods
- [func dates(byAdding: DateComponents, startingAt: Date, in: Range<Date>?, wrappingComponents: Bool) -> some Sendable & Sequence<Date>
](calendar/dates(byadding:startingat:in:wrappingcomponents:).md)
  Returns a sequence of `Date`s, calculated by repeatedly adding an amount of `DateComponents` to a starting `Date` and then to each subsequent result. If a range is supplied, the sequence terminates if the next result is not contained in the range. The starting point does not need to be contained in the range, but if the first result is outside of the range then the result will be an empty sequence.
- [func dates(byAdding: Calendar.Component, value: Int, startingAt: Date, in: Range<Date>?, wrappingComponents: Bool) -> some Sendable & Sequence<Date>
](calendar/dates(byadding:value:startingat:in:wrappingcomponents:).md)
  Returns a sequence of `Date`s, calculated by adding a scaled amount of `Calendar.Component`s to a starting `Date`. If a range is supplied, the sequence terminates if the next result is not contained in the range. The starting point does not need to be contained in the range, but if the first result is outside of the range then the result will be an empty sequence.
- [func dates(byMatching: DateComponents, startingAt: Date, in: Range<Date>?, matchingPolicy: Calendar.MatchingPolicy, repeatedTimePolicy: Calendar.RepeatedTimePolicy, direction: Calendar.SearchDirection) -> some Sendable & Sequence<Date>
](calendar/dates(bymatching:startingat:in:matchingpolicy:repeatedtimepolicy:direction:).md)
  Computes the dates which match (or most closely match) a given set of components, returned as a `Sequence`.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DateComponents](datecomponents.md)
  A date or time specified in terms of units (such as year, month, day, hour, and minute) to be evaluated in a calendar system and time zone.
- [struct TimeZone](timezone.md)
  Information about standard time conventions associated with a specific geopolitical region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar)*