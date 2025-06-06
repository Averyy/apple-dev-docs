# Date Formatter Property Keys

**Framework**: Core Foundation

Keys used in key-value pairs to discover and specify the value of date formatter properties—used in conjunction with [`CFDateFormatterCopyProperty(_:_:)`](cfdateformattercopyproperty(_:_:).md) and [`CFDateFormatterSetProperty(_:_:_:)`](cfdateformattersetproperty(_:_:_:).md).

#### Overview

The values for these keys are all CFType objects. The specific types for each key are specified above.

## Topics

### Constants
- [static let isLenient: CFDateFormatterKey!](cfdateformatterkey/islenient.md)
  Specifies the lenient property, a CFBoolean object where a true value indicates that the parsing of strings into date or absolute time values will be fuzzy.
- [static let timeZone: CFDateFormatterKey!](cfdateformatterkey/timezone.md)
  Specifies the time zone property, a CFTimeZone object.
- [static let calendarName: CFDateFormatterKey!](cfdateformatterkey/calendarname.md)
  Specifies the calendar name, a CFString object.
- [static let defaultFormat: CFDateFormatterKey!](cfdateformatterkey/defaultformat.md)
  The original format string for the formatter (given the date & time style and locale specified at creation).
- [static let twoDigitStartDate: CFDateFormatterKey!](cfdateformatterkey/twodigitstartdate.md)
  Specifies the property representing the date from which two-digit years start, a CFDate object.
- [static let defaultDate: CFDateFormatterKey!](cfdateformatterkey/defaultdate.md)
  Specifies the default date property, a CFDate object.
- [static let calendar: CFDateFormatterKey!](cfdateformatterkey/calendar.md)
  Specifies the calendar property, a CFCalendar object.
- [static let eraSymbols: CFDateFormatterKey!](cfdateformatterkey/erasymbols.md)
  Specifies the era symbols property, a CFArray of CFString objects.
- [static let monthSymbols: CFDateFormatterKey!](cfdateformatterkey/monthsymbols.md)
  Specifies the month symbols property, a CFArray of CFString objects.
- [static let shortMonthSymbols: CFDateFormatterKey!](cfdateformatterkey/shortmonthsymbols.md)
  Specifies the short month symbols property, a CFArray of CFString objects.
- [static let weekdaySymbols: CFDateFormatterKey!](cfdateformatterkey/weekdaysymbols.md)
  Specifies the weekday symbols property, a CFArray of CFString objects.
- [static let shortWeekdaySymbols: CFDateFormatterKey!](cfdateformatterkey/shortweekdaysymbols.md)
  Specifies the short weekday symbols property, a CFArray of CFString objects.
- [static let amSymbol: CFDateFormatterKey!](cfdateformatterkey/amsymbol.md)
  Specifies the AM symbol property, a CFString object.
- [static let pmSymbol: CFDateFormatterKey!](cfdateformatterkey/pmsymbol.md)
  Specifies the PM symbol property, a CFString object.
- [static let longEraSymbols: CFDateFormatterKey!](cfdateformatterkey/longerasymbols.md)
  Specifies the long era symbols property, a CFArray of CFString objects.
- [static let veryShortMonthSymbols: CFDateFormatterKey!](cfdateformatterkey/veryshortmonthsymbols.md)
  Specifies the very short month symbols property, a CFArray of CFString objects.
- [static let standaloneMonthSymbols: CFDateFormatterKey!](cfdateformatterkey/standalonemonthsymbols.md)
  Specifies the standalone month symbols property, a CFArray of CFString objects.
- [static let shortStandaloneMonthSymbols: CFDateFormatterKey!](cfdateformatterkey/shortstandalonemonthsymbols.md)
  Specifies the short standalone month symbols property, a CFArray of CFString objects.
- [static let veryShortStandaloneMonthSymbols: CFDateFormatterKey!](cfdateformatterkey/veryshortstandalonemonthsymbols.md)
  Specifies the very short standalone month symbols property, a CFArray of CFString objects.
- [static let veryShortWeekdaySymbols: CFDateFormatterKey!](cfdateformatterkey/veryshortweekdaysymbols.md)
  Specifies the very short weekday symbols property, a CFArray of CFString objects.
- [static let standaloneWeekdaySymbols: CFDateFormatterKey!](cfdateformatterkey/standaloneweekdaysymbols.md)
  Specifies the standalone weekday symbols property, a CFArray of CFString objects.
- [static let shortStandaloneWeekdaySymbols: CFDateFormatterKey!](cfdateformatterkey/shortstandaloneweekdaysymbols.md)
  Specifies the short standalone weekday symbols property, a CFArray of CFString objects.
- [static let veryShortStandaloneWeekdaySymbols: CFDateFormatterKey!](cfdateformatterkey/veryshortstandaloneweekdaysymbols.md)
  Specifies the very short standalone weekday symbols property, a CFArray of CFString objects.
- [static let quarterSymbols: CFDateFormatterKey!](cfdateformatterkey/quartersymbols.md)
  Specifies the quarter symbols property, a CFArray of CFString objects.
- [static let shortQuarterSymbols: CFDateFormatterKey!](cfdateformatterkey/shortquartersymbols.md)
  Specifies the short quarter symbols property, a CFArray of CFString objects.
- [static let standaloneQuarterSymbols: CFDateFormatterKey!](cfdateformatterkey/standalonequartersymbols.md)
  Specifies the standalone quarter symbols property, a CFArray of CFString objects.
- [static let shortStandaloneQuarterSymbols: CFDateFormatterKey!](cfdateformatterkey/shortstandalonequartersymbols.md)
  Specifies the short standalone quarter symbols property, a CFArray of CFString objects.
- [static let gregorianStartDate: CFDateFormatterKey!](cfdateformatterkey/gregorianstartdate.md)
  Specifies the Gregorian start date property, a CFDate object.
- [static let doesRelativeDateFormattingKey: CFDateFormatterKey!](cfdateformatterkey/doesrelativedateformattingkey.md)
  Specifies the relative date formatting property, a CFBoolean object.

## See Also

- [Date Formatter Styles](date_formatter_styles.md)
  Predefined date and time format styles.
- [Calendar Names](calendar-names.md)
  Calendar names used by CFDateFormatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/date-formatter-property-keys)*