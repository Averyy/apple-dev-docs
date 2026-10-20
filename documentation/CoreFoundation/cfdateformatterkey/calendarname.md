# calendarName

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Specifies the calendar name, a CFString object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static let calendarName: CFDateFormatterKey!
```

```c
extern CFDateFormatterKey const kCFDateFormatterCalendarName;
```

#### Discussion

With OS X version 10.3, [`gregorianCalendar`](../cfcalendaridentifier/gregoriancalendar.md) is the only possible value. With OS X version 10.4, `kCFGregorianCalendar` and other calendar names are specified by CFLocale.

## See Also

### Constants
- [static let isLenient: CFDateFormatterKey!](./islenient.md)
  Specifies the lenient property, a CFBoolean object where a true value indicates that the parsing of strings into date or absolute time values will be fuzzy.
- [static let timeZone: CFDateFormatterKey!](./timezone.md)
  Specifies the time zone property, a CFTimeZone object.
- [static let defaultFormat: CFDateFormatterKey!](./defaultformat.md)
  The original format string for the formatter (given the date & time style and locale specified at creation).
- [static let twoDigitStartDate: CFDateFormatterKey!](./twodigitstartdate.md)
  Specifies the property representing the date from which two-digit years start, a CFDate object.
- [static let defaultDate: CFDateFormatterKey!](./defaultdate.md)
  Specifies the default date property, a CFDate object.
- [static let calendar: CFDateFormatterKey!](./calendar.md)
  Specifies the calendar property, a CFCalendar object.
- [static let eraSymbols: CFDateFormatterKey!](./erasymbols.md)
  Specifies the era symbols property, a CFArray of CFString objects.
- [static let monthSymbols: CFDateFormatterKey!](./monthsymbols.md)
  Specifies the month symbols property, a CFArray of CFString objects.
- [static let shortMonthSymbols: CFDateFormatterKey!](./shortmonthsymbols.md)
  Specifies the short month symbols property, a CFArray of CFString objects.
- [static let weekdaySymbols: CFDateFormatterKey!](./weekdaysymbols.md)
  Specifies the weekday symbols property, a CFArray of CFString objects.
- [static let shortWeekdaySymbols: CFDateFormatterKey!](./shortweekdaysymbols.md)
  Specifies the short weekday symbols property, a CFArray of CFString objects.
- [static let amSymbol: CFDateFormatterKey!](./amsymbol.md)
  Specifies the AM symbol property, a CFString object.
- [static let pmSymbol: CFDateFormatterKey!](./pmsymbol.md)
  Specifies the PM symbol property, a CFString object.
- [static let longEraSymbols: CFDateFormatterKey!](./longerasymbols.md)
  Specifies the long era symbols property, a CFArray of CFString objects.
- [static let veryShortMonthSymbols: CFDateFormatterKey!](./veryshortmonthsymbols.md)
  Specifies the very short month symbols property, a CFArray of CFString objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformatterkey/calendarname)*