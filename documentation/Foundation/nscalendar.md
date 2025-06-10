# NSCalendar

**Framework**: Foundation  
**Kind**: class

A definition of the relationships between calendar units and absolute points in time, providing features for calculation and comparison of dates.

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
class NSCalendar
```

#### Overview

In Swift, this object bridges to [`Calendar`](calendar.md); use [`NSCalendar`](nscalendar.md) when you need reference semantics or other Foundation-specific behavior.

[`NSCalendar`](nscalendar.md) objects encapsulate information about systems of reckoning time in which the beginning, length, and divisions of a year are defined. They provide information about the calendar and support for calendrical computations such as determining the range of a given calendrical unit and adding units to a given absolute time.

[`NSCalendar`](nscalendar.md) is  with its Core Foundation counterpart, [`CFCalendar`](https://developer.apple.com/documentation/CoreFoundation/CFCalendar). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`Calendar`](calendar.md) structure, which bridges to the [`NSCalendar`](nscalendar.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

##### Locales and Calendars

Most locales use the most widely used civil calendar, called the  ([`gregorian`](nscalendar/identifier/gregorian.md)), but there remain exceptions to this trend. For example:

- In Saudi Arabia, some locales use primarily the Islamic Umm al-Qura calendar ([`islamicUmmAlQura`](nscalendar/identifier/islamicummalqura.md)).
- In Ethiopia, some locales use primarily the Ethiopian calendar ([`ethiopicAmeteMihret`](nscalendar/identifier/ethiopicametemihret.md) or [`ethiopicAmeteAlem`](nscalendar/identifier/ethiopicametealem.md)).
- In Iran and Afghanistan, some locales use primarily the Persian calendar ([`persian`](nscalendar/identifier/persian.md)).
- In Thailand, some locales use primarily the Buddhist calendar ([`buddhist`](nscalendar/identifier/buddhist.md)).

Other locales use another calendar alongside the Gregorian calendar. For example:

- India also uses the Indian national calendar ([`indian`](nscalendar/identifier/indian.md)).
- Israel also uses the Hebrew calendar ([`hebrew`](nscalendar/identifier/hebrew.md)).
- China mainland and other regions also use the Chinese calendar ([`chinese`](nscalendar/identifier/chinese.md)), primarily to calculate astronomical date and Chinese traditional holidays.
- Japan also uses the Japanese calendar ([`japanese`](nscalendar/identifier/japanese.md)), primarily to add year names.

Independent of any particular locale, certain calendars are used primarily to calculate dates for religious observances. Among these are the Buddhist ([`buddhist`](nscalendar/identifier/buddhist.md)), Coptic ([`coptic`](nscalendar/identifier/coptic.md)), Hebrew ([`hebrew`](nscalendar/identifier/hebrew.md)), and Islamic ([`islamic`](nscalendar/identifier/islamic.md)) calendars.

##### How Nscalendar Models the Gregorian Calendar

The Gregorian calendar was first introduced in 1582, as a replacement for the Julian Calendar. According to the Julian calendar, a leap day is added to February for any year with a number divisible by 4, which results in an annual disparity of 11 minutes, or 1 day every 128 years. The Gregorian calendar revised the rules for leap day calculation, by skipping the leap day for any year with a number divisible by 100, unless that year number is also divisible by 400, resulting in an annual disparity of only 26 seconds, or 1 day every 3323 years.

To transition from the Julian calendar to the Gregorian calendar, 10 days were dropped from the Gregorian calendar (October 5–14).

After the Gregorian calendar was introduced, many regions continued to use the Julian calendar, with Turkey being the last country or region to adopt the Gregorian calendar, in 1926. As a result of the staggered adoption, the transition period for regions at the time of adoption have different start dates and a different number of skipped days to account for the additional disparity from leap day calculations.

[`NSCalendar`](nscalendar.md) models the behavior of a  Gregorian calendar (), which extends the Gregorian calendar backward in time from the date of its introduction. This behavior should be taken into account when working with dates created before the transition period of the affected locales.

##### Calendar Arithmetic

To do calendar arithmetic, you use [`NSDate`](nsdate.md) objects in conjunction with a calendar. For example, to convert between a decomposed date in one calendar and another calendar, you must first convert the decomposed elements into a date using the first calendar, then decompose it using the second. [`NSDate`](nsdate.md) provides the absolute scale and epoch (reference point) for dates and times, which can then be rendered into a particular calendar, for calendrical computations or user display.

Two [`NSCalendar`](nscalendar.md) methods that return a date object, [`date(from:)`](nscalendar/date(from:).md), [`date(byAdding:to:options:)`](nscalendar/date(byadding:to:options:).md), take as a parameter an [`NSDateComponents`](nsdatecomponents.md) object that describes the calendrical components required for the computation. You can provide as many components as you need (or choose to). When there is incomplete information to compute an absolute time, default values similar to `0` and `1` are usually chosen by a calendar, but this is a calendar-specific choice. If you provide inconsistent information, calendar-specific disambiguation is performed (which may involve ignoring one or more of the parameters). Related methods ([`components(_:from:)`](nscalendar/components(_:from:).md) and [`components(_:from:to:options:)`](nscalendar/components(_:from:to:options:)-84y5w.md)) take a bit mask parameter that specifies which components to calculate when returning an [`NSDateComponents`](nsdatecomponents.md) object. The bit mask is composed of [`NSCalendar.Unit`](nscalendar/unit.md) constants (see `Constants`).

In a calendar, day, week, weekday, month, and year numbers are generally 1-based, but there may be calendar-specific exceptions. Ordinal numbers, where they occur, are 1-based. Some calendars represented by this API may have to map their basic unit concepts into year/month/week/day/… nomenclature. For example, a calendar composed of 4 quarters in a year instead of 12 months uses the month unit to represent quarters. The particular values of the unit are defined by each calendar, and are not necessarily consistent with values for that unit in another calendar.

## Topics

### Creating and Initializing Calendars
- [init?(identifier: NSCalendar.Identifier)](nscalendar/init(identifier:).md)
  Creates a new calendar specified by a given identifier.
- [init?(calendarIdentifier: NSCalendar.Identifier)](nscalendar/init(calendaridentifier:).md)
  Initializes a calendar according to a given identifier.
- [NSCalendar.Identifier](nscalendar/identifier.md)
  The supported calendar types.
### Getting the User’s Calendar
- [class var current: Calendar](nscalendar/current.md)
  The user’s current calendar.
- [class var autoupdatingCurrent: Calendar](nscalendar/autoupdatingcurrent.md)
  A calendar that tracks changes to user’s preferred calendar.
### Extracting Components
- [func date(Date, matchesComponents: DateComponents) -> Bool](nscalendar/date(_:matchescomponents:).md)
  Returns whether a given date matches all of the given date components.
- [func component(NSCalendar.Unit, from: Date) -> Int](nscalendar/component(_:from:).md)
  Returns the specified date component from a given date.
- [func components(NSCalendar.Unit, from: Date) -> DateComponents](nscalendar/components(_:from:).md)
  Returns the date components representing a given date.
- [func components(NSCalendar.Unit, from: Date, to: Date, options: NSCalendar.Options) -> DateComponents](nscalendar/components(_:from:to:options:)-84y5w.md)
  Returns the difference between two supplied dates as date components.
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
### Getting Calendar Information
- [var calendarIdentifier: NSCalendar.Identifier](nscalendar/calendaridentifier.md)
  An identifier for the calendar.
- [var firstWeekday: Int](nscalendar/firstweekday.md)
  The index of the first weekday of the receiver.
- [var locale: Locale?](nscalendar/locale.md)
  The locale of the receiver.
- [var timeZone: TimeZone](nscalendar/timezone.md)
  The time zone for the calendar.
- [func maximumRange(of: NSCalendar.Unit) -> NSRange](nscalendar/maximumrange(of:).md)
  Returns the maximum range limits of the values that a given unit can take on.
- [func minimumRange(of: NSCalendar.Unit) -> NSRange](nscalendar/minimumrange(of:).md)
  Returns the minimum range limits of the values that a given unit can take on.
- [var minimumDaysInFirstWeek: Int](nscalendar/minimumdaysinfirstweek.md)
  The minimum number of days in the first week of the receiver.
- [func ordinality(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> Int](nscalendar/ordinality(of:in:for:).md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar unit (such as a day) within a specified larger calendar unit (such as a week).
- [func range(of: NSCalendar.Unit, in: NSCalendar.Unit, for: Date) -> NSRange](nscalendar/range(of:in:for:).md)
  Returns the range of absolute time values that a smaller calendar unit (such as a day) can take on in a larger calendar unit (such as a month) that includes a specified absolute time.
- [func range(of: NSCalendar.Unit, start: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, for: Date) -> Bool](nscalendar/range(of:start:interval:for:).md)
  Returns by reference the starting time and duration of a given calendar unit that contains a given date.
- [func range(ofWeekendStart: AutoreleasingUnsafeMutablePointer<NSDate?>?, interval: UnsafeMutablePointer<TimeInterval>?, containing: Date) -> Bool](nscalendar/range(ofweekendstart:interval:containing:).md)
  Returns whether a given date falls within a weekend period, and if so, returns by reference the start date and time interval of the weekend range.
- [NSCalendar.Unit](nscalendar/unit.md)
  Calendrical units such as year, month, day and hour.
### Scanning Dates
- [func startOfDay(for: Date) -> Date](nscalendar/startofday(for:).md)
  Returns the first moment of a given date as a date instance.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nscalendar/enumeratedates(startingafter:matching:options:using:).md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:options:).md)
  Returns the next date after a given date matching the given components.
- [func nextDate(after: Date, matchingHour: Int, minute: Int, second: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matchinghour:minute:second:options:).md)
  Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:value:options:).md)
  Returns the next date after a given date matching the given calendar unit value.
- [NSCalendar.Options](nscalendar/options.md)
  The options for arithmetic operations involving calendars.
- [NSWrapCalendarComponents](nswrapcalendarcomponents-api.md)
  A legacy constant used to control overflow in date calculations.
### Calculating Dates
- [func date(from: DateComponents) -> Date?](nscalendar/date(from:).md)
  Returns a date representing the absolute time calculated from given components.
- [func date(byAdding: DateComponents, to: Date, options: NSCalendar.Options) -> Date?](nscalendar/date(byadding:to:options:).md)
  Returns a date representing the absolute time calculated by adding given components to a given date.
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
### Comparing Dates
- [func compare(Date, to: Date, toUnitGranularity: NSCalendar.Unit) -> ComparisonResult](nscalendar/compare(_:to:tounitgranularity:).md)
  Indicates the ordering of two given dates based on their components down to a given unit granularity.
- [func isDate(Date, equalTo: Date, toUnitGranularity: NSCalendar.Unit) -> Bool](nscalendar/isdate(_:equalto:tounitgranularity:).md)
  Indicates whether two dates are equal to a given unit of granularity.
- [func isDate(Date, inSameDayAs: Date) -> Bool](nscalendar/isdate(_:insamedayas:).md)
  Indicates whether two dates are in the same day.
- [func isDateInToday(Date) -> Bool](nscalendar/isdateintoday(_:).md)
  Indicates whether the given date is in “today.”
- [func isDateInTomorrow(Date) -> Bool](nscalendar/isdateintomorrow(_:).md)
  Indicates whether the given date is in “tomorrow.”
- [func isDateInWeekend(Date) -> Bool](nscalendar/isdateinweekend(_:).md)
  Indicates whether a given date falls within a weekend period, as defined by the calendar and the calendar’s locale.
- [func isDateInYesterday(Date) -> Bool](nscalendar/isdateinyesterday(_:).md)
  Indicates whether the given date is in “yesterday.”
### Getting AM and PM Symbols
- [var amSymbol: String](nscalendar/amsymbol.md)
  The symbol used to represent “AM” for this calendar.
- [var pmSymbol: String](nscalendar/pmsymbol.md)
  The symbol used to represent “PM” for this calendar.
### Getting Weekday Symbols
- [var weekdaySymbols: [String]](nscalendar/weekdaysymbols.md)
  A list of weekdays in this calendar.
- [var shortWeekdaySymbols: [String]](nscalendar/shortweekdaysymbols.md)
  A list of shorter-named weekdays in this calendar.
- [var veryShortWeekdaySymbols: [String]](nscalendar/veryshortweekdaysymbols.md)
  A list of very-shortly-named weekdays in this calendar.
- [var standaloneWeekdaySymbols: [String]](nscalendar/standaloneweekdaysymbols.md)
  A list of standalone weekday symbols for this calendar.
- [var shortStandaloneWeekdaySymbols: [String]](nscalendar/shortstandaloneweekdaysymbols.md)
  A list of short standalone weekday symbols for this calendar.
- [var veryShortStandaloneWeekdaySymbols: [String]](nscalendar/veryshortstandaloneweekdaysymbols.md)
  A list of very short standalone weekday symbols for this calendar.
### Getting Month Symbols
- [var monthSymbols: [String]](nscalendar/monthsymbols.md)
  A list of month symbols for this calendar.
- [var shortMonthSymbols: [String]](nscalendar/shortmonthsymbols.md)
  A list of short month symbols for this calendar.
- [var veryShortMonthSymbols: [String]](nscalendar/veryshortmonthsymbols.md)
  A list of very short month symbols for this calendar.
- [var standaloneMonthSymbols: [String]](nscalendar/standalonemonthsymbols.md)
  A list of standalone month symbols for this calendar.
- [var shortStandaloneMonthSymbols: [String]](nscalendar/shortstandalonemonthsymbols.md)
  A list of short standalone month symbols for this calendar.
- [var veryShortStandaloneMonthSymbols: [String]](nscalendar/veryshortstandalonemonthsymbols.md)
  A list of very short month symbols for this calendar.
### Getting Quarter Symbols
- [var quarterSymbols: [String]](nscalendar/quartersymbols.md)
  A list of quarter symbols for this calendar.
- [var shortQuarterSymbols: [String]](nscalendar/shortquartersymbols.md)
  A list of short quarter symbols for this calendar.
- [var standaloneQuarterSymbols: [String]](nscalendar/standalonequartersymbols.md)
  A list of standalone quarter symbols for this calendar.
- [var shortStandaloneQuarterSymbols: [String]](nscalendar/shortstandalonequartersymbols.md)
  A list of short standalone quarter symbols for this calendar.
### Getting Era Symbols
- [var eraSymbols: [String]](nscalendar/erasymbols.md)
  A list of era symbols for this calendar.
- [var longEraSymbols: [String]](nscalendar/longerasymbols.md)
  A list of long era symbols for this calendar.
### Recognizing Notifications
- [static let NSCalendarDayChanged: NSNotification.Name](nsnotification/name-swift.struct/nscalendardaychanged.md)
  A notification that is posted whenever the calendar day of the system changes, as determined by the system calendar, locale, and time zone.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar)*