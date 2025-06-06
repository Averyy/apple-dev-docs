# Locale Calendar Identifiers

**Framework**: Core Foundation

Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.

#### Overview

Locale objects use key-value pairs to store property values. Use the [`CFLocaleGetValue(_:_:)`](cflocalegetvalue(_:_:).md) function to get the value of a specific property listed above.

## Topics

### Constants
- [static let gregorianCalendar: CFCalendarIdentifier!](cfcalendaridentifier/gregoriancalendar.md)
  The name of the calendar currently supported by the [`calendarName`](cfdateformatterkey/calendarname.md) property.
- [static let buddhistCalendar: CFCalendarIdentifier!](cfcalendaridentifier/buddhistcalendar.md)
  Specifies the Buddhist calendar.
- [static let chineseCalendar: CFCalendarIdentifier!](cfcalendaridentifier/chinesecalendar.md)
  Specifies the Chinese calendar.
- [static let hebrewCalendar: CFCalendarIdentifier!](cfcalendaridentifier/hebrewcalendar.md)
  Specifies the Hebrew calendar.
- [static let islamicCalendar: CFCalendarIdentifier!](cfcalendaridentifier/islamiccalendar.md)
  Specifies the Islamic calendar.
- [static let islamicCivilCalendar: CFCalendarIdentifier!](cfcalendaridentifier/islamiccivilcalendar.md)
  Specifies the Islamic tabular calendar with Friday (civil) origin.
- [static let islamicTabularCalendar: CFCalendarIdentifier!](cfcalendaridentifier/islamictabularcalendar.md)
  Specifies the Islamic tabular calendar with Thursday (astronomical) origin.
- [static let islamicUmmAlQuraCalendar: CFCalendarIdentifier!](cfcalendaridentifier/islamicummalquracalendar.md)
  Specifies the Islamic Umm Al Qura calendar.
- [static let japaneseCalendar: CFCalendarIdentifier!](cfcalendaridentifier/japanesecalendar.md)
  Specifies the Japanese calendar.
- [static let republicOfChinaCalendar: CFCalendarIdentifier!](cfcalendaridentifier/republicofchinacalendar.md)
  Specifies the calendar for the Republic of China.
- [static let persianCalendar: CFCalendarIdentifier!](cfcalendaridentifier/persiancalendar.md)
  Specifies the Persian calendar.
- [static let indianCalendar: CFCalendarIdentifier!](cfcalendaridentifier/indiancalendar.md)
  Specifies the Indian calendar.
- [static let cfiso8601Calendar: CFCalendarIdentifier!](cfcalendaridentifier/cfiso8601calendar.md)
  Specifies the ISO 8601 calendar.

## See Also

- [enum CFLocaleLanguageDirection](cflocalelanguagedirection.md)
  These constants describe the text direction for a language. They are returned by the functions [`CFLocaleGetLanguageCharacterDirection(_:)`](cflocalegetlanguagecharacterdirection(_:).md) and [`CFLocaleGetLanguageLineDirection(_:)`](cflocalegetlanguagelinedirection(_:).md).
- [Locale Property Keys](locale-property-keys.md)
  Predefined locale keys used to get property values.
- [Locale Change Notification](locale-change-notification.md)
  Identifier for notification sent if the current locale changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/locale-calendar-identifiers)*