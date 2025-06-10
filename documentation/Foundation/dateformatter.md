# DateFormatter

**Framework**: Foundation  
**Kind**: class

A formatter that converts between dates and their textual representations.

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
class DateFormatter
```

#### Overview

Instances of [`DateFormatter`](dateformatter.md) create string representations of [`NSDate`](nsdate.md) objects, and convert textual representations of dates and times into [`NSDate`](nsdate.md) objects. For user-visible representations of dates and times, [`DateFormatter`](dateformatter.md) provides a variety of localized presets and configuration options. For fixed format representations of dates and times, you can specify a custom format string.

When working with date representations in ISO 8601 format, use [`ISO8601DateFormatter`](iso8601dateformatter.md) instead.

To represent an interval between two [`NSDate`](nsdate.md) objects, use [`DateIntervalFormatter`](dateintervalformatter.md) instead.

To represent a quantity of time specified by an [`NSDateComponents`](nsdatecomponents.md) object, use [`DateComponentsFormatter`](datecomponentsformatter.md) instead.

> 💡 **Tip**:  In Swift, you can use [`Date.FormatStyle`](date/formatstyle.md) or [`Date.VerbatimFormatStyle`](date/verbatimformatstyle.md) rather than [`DateFormatter`](dateformatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

##### Working with User Visible Representations of Dates and Times

When displaying a date to a user, you set the [`dateStyle`](dateformatter/datestyle.md) and [`timeStyle`](dateformatter/timestyle.md) properties of the date formatter according to your particular needs. For example, if you want to show the month, day, and year without showing the time, you would set the [`dateStyle`](dateformatter/datestyle.md) property to [`DateFormatter.Style.long`](dateformatter/style/long.md) and the [`timeStyle`](dateformatter/timestyle.md) property to [`DateFormatter.Style.none`](dateformatter/style/none.md). Conversely, if you want to show only the time, you would set the `dateStyle` property to [`DateFormatter.Style.none`](dateformatter/style/none.md) and the [`timeStyle`](dateformatter/timestyle.md) property to [`DateFormatter.Style.short`](dateformatter/style/short.md). Based on the values of the [`dateStyle`](dateformatter/datestyle.md) and [`timeStyle`](dateformatter/timestyle.md) properties, [`DateFormatter`](dateformatter.md) provides a representation of a specified date that is appropriate for a given locale.

If you need to define a format that cannot be achieved using the predefined styles, you can use the [`setLocalizedDateFormatFromTemplate(_:)`](dateformatter/setlocalizeddateformatfromtemplate(_:).md) to specify a localized date format from a template.

##### Working with Fixed Format Date Representations

> ❗ **Important**:  In macOS 10.12 and later or iOS 10 and later, use the [`ISO8601DateFormatter`](iso8601dateformatter.md) class when working with ISO 8601 date representations.

When working with fixed format dates, such as RFC 3339, you set the [`dateFormat`](dateformatter/dateformat.md) property to specify a format string. For most fixed formats, you should also set the [`locale`](dateformatter/locale.md) property to a POSIX locale (`"en_US_POSIX"`), and set the [`timeZone`](dateformatter/timezone.md) property to UTC.

For more information, see [`Technical Q&A QA1480 “NSDateFormatter and Internet Dates”`](https://developer.apple.comhttps://developer.apple.com/library/mac/qa/qa1480/).

##### Thread Safety

On iOS 7 and later `NSDateFormatter` is thread safe.

In macOS 10.9 and later `NSDateFormatter` is thread safe so long as you are using the modern behavior in a 64-bit app.

On earlier versions of the operating system, or when using the legacy formatter behavior or running in 32-bit in macOS, `NSDateFormatter` is not thread safe, and you therefore must not mutate a date formatter simultaneously from multiple threads.

## Topics

### Converting Objects
- [func date(from: String) -> Date?](dateformatter/date(from:).md)
  Returns a date representation of a specified string that the system interprets using the receiver’s current settings.
- [func string(from: Date) -> String](dateformatter/string(from:).md)
  Returns a string representation of a specified date that the system formats using the receiver’s current settings.
- [class func localizedString(from: Date, dateStyle: DateFormatter.Style, timeStyle: DateFormatter.Style) -> String](dateformatter/localizedstring(from:datestyle:timestyle:).md)
  Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.
- [func getObjectValue(AutoreleasingUnsafeMutablePointer<AnyObject?>?, for: String, range: UnsafeMutablePointer<NSRange>?) throws](dateformatter/getobjectvalue(_:for:range:).md)
  Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.
### Managing Formats and Styles
- [var dateStyle: DateFormatter.Style](dateformatter/datestyle.md)
  The date style of the receiver.
- [var timeStyle: DateFormatter.Style](dateformatter/timestyle.md)
  The time style of the receiver.
- [var dateFormat: String!](dateformatter/dateformat.md)
  The date format string used by the receiver.
- [func setLocalizedDateFormatFromTemplate(String)](dateformatter/setlocalizeddateformatfromtemplate(_:).md)
  Sets the date format from a template using the specified locale for the receiver.
- [class func dateFormat(fromTemplate: String, options: Int, locale: Locale?) -> String?](dateformatter/dateformat(fromtemplate:options:locale:).md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
- [var formattingContext: Formatter.Context](dateformatter/formattingcontext.md)
  The capitalization formatting context used when formatting a date.
### Managing Attributes
- [var calendar: Calendar!](dateformatter/calendar.md)
  The calendar for the receiver.
- [var defaultDate: Date?](dateformatter/defaultdate.md)
  The default date for the receiver.
- [var locale: Locale!](dateformatter/locale.md)
  The locale for the receiver.
- [var timeZone: TimeZone!](dateformatter/timezone.md)
  The time zone for the receiver.
- [var twoDigitStartDate: Date?](dateformatter/twodigitstartdate.md)
  The earliest date that can be denoted by a two-digit year specifier.
- [var gregorianStartDate: Date?](dateformatter/gregorianstartdate.md)
  The start date of the Gregorian calendar for the receiver.
### Managing Behavior Version
- [var formatterBehavior: DateFormatter.Behavior](dateformatter/formatterbehavior.md)
  The formatter behavior for the receiver.
- [class var defaultFormatterBehavior: DateFormatter.Behavior](dateformatter/defaultformatterbehavior.md)
  Returns the default formatting behavior for instances of the class.
### Managing Natural Language Support
- [var isLenient: Bool](dateformatter/islenient.md)
  A Boolean value that indicates whether the receiver uses heuristics when parsing a string.
- [var doesRelativeDateFormatting: Bool](dateformatter/doesrelativedateformatting.md)
  A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.
### Managing AM and PM Symbols
- [var amSymbol: String!](dateformatter/amsymbol.md)
  The AM symbol for the receiver.
- [var pmSymbol: String!](dateformatter/pmsymbol.md)
  The PM symbol for the receiver.
### Managing Weekday Symbols
- [var weekdaySymbols: [String]!](dateformatter/weekdaysymbols.md)
  The array of weekday symbols for the receiver.
- [var shortWeekdaySymbols: [String]!](dateformatter/shortweekdaysymbols.md)
  The array of short weekday symbols for the receiver.
- [var veryShortWeekdaySymbols: [String]!](dateformatter/veryshortweekdaysymbols.md)
  The array of very short weekday symbols for the receiver.
- [var standaloneWeekdaySymbols: [String]!](dateformatter/standaloneweekdaysymbols.md)
  The array of standalone weekday symbols for the receiver.
- [var shortStandaloneWeekdaySymbols: [String]!](dateformatter/shortstandaloneweekdaysymbols.md)
  The array of short standalone weekday symbols for the receiver.
- [var veryShortStandaloneWeekdaySymbols: [String]!](dateformatter/veryshortstandaloneweekdaysymbols.md)
  The array of very short standalone weekday symbols for the receiver.
### Managing Month Symbols
- [var monthSymbols: [String]!](dateformatter/monthsymbols.md)
  The month symbols for the receiver.
- [var shortMonthSymbols: [String]!](dateformatter/shortmonthsymbols.md)
  The array of short month symbols for the receiver.
- [var veryShortMonthSymbols: [String]!](dateformatter/veryshortmonthsymbols.md)
  The very short month symbols for the receiver.
- [var standaloneMonthSymbols: [String]!](dateformatter/standalonemonthsymbols.md)
  The standalone month symbols for the receiver.
- [var shortStandaloneMonthSymbols: [String]!](dateformatter/shortstandalonemonthsymbols.md)
  The short standalone month symbols for the receiver.
- [var veryShortStandaloneMonthSymbols: [String]!](dateformatter/veryshortstandalonemonthsymbols.md)
  The very short month symbols for the receiver.
### Managing Quarter Symbols
- [var quarterSymbols: [String]!](dateformatter/quartersymbols.md)
  The quarter symbols for the receiver.
- [var shortQuarterSymbols: [String]!](dateformatter/shortquartersymbols.md)
  The short quarter symbols for the receiver.
- [var standaloneQuarterSymbols: [String]!](dateformatter/standalonequartersymbols.md)
  The standalone quarter symbols for the receiver.
- [var shortStandaloneQuarterSymbols: [String]!](dateformatter/shortstandalonequartersymbols.md)
  The short standalone quarter symbols for the receiver.
### Managing Era Symbols
- [var eraSymbols: [String]!](dateformatter/erasymbols.md)
  The era symbols for the receiver.
- [var longEraSymbols: [String]!](dateformatter/longerasymbols.md)
  The long era symbols for the receiver
### Deprecated
- [var generatesCalendarDates: Bool](dateformatter/generatescalendardates.md)
  Indicates whether the formatter generates the deprecated calendar date type.
### Constants
- [DateFormatter.Style](dateformatter/style.md)
  The following constants specify predefined format styles for dates and times.
- [DateFormatter.Behavior](dateformatter/behavior.md)
  Constants that specify the behavior `NSDateFormatter` should exhibit.

## Relationships

### Inherits From
- [Formatter](formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class DateComponentsFormatter](datecomponentsformatter.md)
  A formatter that creates string representations of quantities of time.
- [class RelativeDateTimeFormatter](relativedatetimeformatter.md)
  A formatter that creates locale-aware string representations of a relative date or time.
- [class DateIntervalFormatter](dateintervalformatter.md)
  A formatter that creates string representations of time intervals.
- [class ISO8601DateFormatter](iso8601dateformatter.md)
  A formatter that converts between dates and their ISO 8601 string representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateformatter)*