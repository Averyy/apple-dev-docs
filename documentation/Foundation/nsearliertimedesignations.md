# NSEarlierTimeDesignations

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Key for an array of strings that denote a time in the past.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: There is no direct replacement. If you need to localize words such as “prior,” you should use a strings file as you would for any other localizable text—see Localizing String Resources.

## Declaration

```c
extern NSString * const NSEarlierTimeDesignations;
```

## Discussion

These are adjectives that modify values from `NSYearMonthWeekDesignations`. The defaults are “prior,” “last,” “past,” and “ago.”

## See Also

### Date & Time Information
- [NSAMPMDesignation](./nsampmdesignation.md)
  Key for the value that specifies how the morning and afternoon designations are printed, affecting strings that use the `%p` format specifier.
- [NSDateFormatString](./nsdateformatstring.md)
  Key for the format string that specifies how dates are printed using the date format specifiers.
- [NSDateTimeOrdering](./nsdatetimeordering.md)
  Key for the string that specifies how to use ambiguous numbers in date strings.
- [NSHourNameDesignations](./nshournamedesignations.md)
  Key for strings that identify the time of day.
- [NSLaterTimeDesignations](./nslatertimedesignations.md)
  Key for an array of strings that denote a time in the future.
- [NSMonthNameArray](./nsmonthnamearray.md)
  Key for the value that specifies the names for the months, affecting strings that use the `%B` format specifier.
- [NSNextDayDesignations](./nsnextdaydesignations.md)
  Key for an array of strings that denote the day after today.
- [NSNextNextDayDesignations](./nsnextnextdaydesignations.md)
  Key for an array of strings that denote the day after tomorrow.
- [NSPriorDayDesignations](./nspriordaydesignations.md)
  Key for an array of strings that denote the day before today.
- [NSShortDateFormatString](./nsshortdateformatstring.md)
  Key for a format string that specifies how dates are abbreviated.
- [NSShortWeekDayNameArray](./nsshortweekdaynamearray.md)
  Key for an array of strings that specify the abbreviations for the days of the week, affecting strings that use the %a format specifier.
- [NSShortMonthNameArray](./nsshortmonthnamearray.md)
  Key for an array of strings that specify the abbreviations for the months, affecting strings that use the `%b` format specifier.
- [NSShortTimeDateFormatString](./nsshorttimedateformatstring.md)
  Key for a format string that specifies how times and dates are abbreviated.
- [NSThisDayDesignations](./nsthisdaydesignations.md)
  Key for an array of strings that specify what this day is called.
- [NSTimeDateFormatString](./nstimedateformatstring.md)
  Key for the value that specifies how dates with times are printed, affecting strings that use the format specifiers `%c`, `%X`, or `%x`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsearliertimedesignations)*