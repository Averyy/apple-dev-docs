# Date Formatter Styles

**Framework**: Core Foundation

Predefined date and time format styles.

#### Overview

The format for these date and time styles is not exact because they depend on the locale, user preference settings, and the operating system version. Do not use these constants if you want an exact format, for example if you are parsing an external data file which contains date information in a fixed format. There are several different “lengths” of the formats:

- “long” era names, for example “Anno Domini” instead of “AD”
- “very short” names for months and weekdays; for example, “F” instead of “Friday”
- “standalone” names for months and weekdays (for some locales or languages, a month name displayed in isolation needs to be written differently than a month name within a displayed date)
- names of quarters; for example, “Q2” for a short quarter name

## Topics

### Constants
- [CFDateFormatterStyle.noStyle](cfdateformatterstyle/nostyle.md)
  Specifies no output.
- [CFDateFormatterStyle.shortStyle](cfdateformatterstyle/shortstyle.md)
  Specifies a short style, typically numeric only, such as “11/23/37” or “3:30pm”.
- [CFDateFormatterStyle.mediumStyle](cfdateformatterstyle/mediumstyle.md)
  Specifies a medium style, typically with abbreviated text, such as “Nov 23, 1937”.
- [CFDateFormatterStyle.longStyle](cfdateformatterstyle/longstyle.md)
  Specifies a long style, typically with full text, such as “November 23, 1937” or “3:30:32pm”.
- [CFDateFormatterStyle.fullStyle](cfdateformatterstyle/fullstyle.md)
  Specifies a full style with complete details, such as “Tuesday, April 12, 1952 AD” or “3:30:42pm PST”.

## See Also

- [Date Formatter Property Keys](date-formatter-property-keys.md)
  Keys used in key-value pairs to discover and specify the value of date formatter properties—used in conjunction with [`CFDateFormatterCopyProperty(_:_:)`](cfdateformattercopyproperty(_:_:).md) and [`CFDateFormatterSetProperty(_:_:_:)`](cfdateformattersetproperty(_:_:_:).md).
- [Calendar Names](calendar-names.md)
  Calendar names used by CFDateFormatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/date_formatter_styles)*