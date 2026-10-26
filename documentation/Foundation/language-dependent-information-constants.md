# Language-Dependent Information Constants

**Framework**: Foundation  
**Role**: API Collection

These constants are deprecated and shouldn’t be used.

## Topics

### Date & Time Information
- [NSAMPMDesignation](./nsampmdesignation.md)
  Key for the value that specifies how the morning and afternoon designations are printed, affecting strings that use the `%p` format specifier.
- [NSDateFormatString](./nsdateformatstring.md)
  Key for the format string that specifies how dates are printed using the date format specifiers.
- [NSDateTimeOrdering](./nsdatetimeordering.md)
  Key for the string that specifies how to use ambiguous numbers in date strings.
- [NSEarlierTimeDesignations](./nsearliertimedesignations.md)
  Key for an array of strings that denote a time in the past.
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
- [NSTimeFormatString](./nstimeformatstring.md)
  Key for a format string that specifies how dates with times are printed.
- [NSWeekDayNameArray](./nsweekdaynamearray.md)
  Key for an array of strings that specify the names for the days of the week, affecting strings that use the `%A` format specifier.
- [NSYearMonthWeekDesignations](./nsyearmonthweekdesignations.md)
  Key for an array of strings that specify the words for year, month, and week in the current locale.
### Numeric Information
- [NSCurrencySymbol](./nscurrencysymbol.md)
  A string that specifies the symbol used to denote currency in this language.
- [NSDecimalDigits](./nsdecimaldigits.md)
  Strings that identify the decimal digits in addition to or instead of the ASCII digits.
- [NSDecimalSeparator](./nsdecimalseparator.md)
  A string that specifies the decimal separator.
- [NSInternationalCurrencyString](./nsinternationalcurrencystring.md)
  A string containing a three-letter abbreviation for currency, following the ISO 4217 standard.
- [NSNegativeCurrencyFormatString](./nsnegativecurrencyformatstring.md)
  A format string that specifies how negative numbers are printed when representing a currency value.
- [NSPositiveCurrencyFormatString](./nspositivecurrencyformatstring.md)
  A format string that specifies how positive numbers are printed when representing a currency value.
- [NSThousandsSeparator](./nsthousandsseparator.md)
  A string that specifies the separator character for the thousands place of a decimal number.

## See Also

### Deprecated
- [convenience init?(user: String)](./userdefaults/init%28user%29.md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [func synchronize() -> Bool](./userdefaults/synchronize%28%29.md)
  Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [class func resetStandardUserDefaults()](./userdefaults/resetstandarduserdefaults%28%29.md)
  This method has no effect and shouldn’t be used.
- [func persistentDomainNames() -> [Any]](./userdefaults/persistentdomainnames%28%29.md)
  Returns an array of the current persistent domain names.
- [class let completedInitialCloudSyncNotification: NSNotification.Name](./userdefaults/completedinitialcloudsyncnotification.md)
  Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account.
- [class let didChangeCloudAccountsNotification: NSNotification.Name](./userdefaults/didchangecloudaccountsnotification.md)
  Posted when the user changes the primary iCloud account.
- [class let noCloudAccountNotification: NSNotification.Name](./userdefaults/nocloudaccountnotification.md)
  Posted when a cloud default is set, but no iCloud user is logged in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/language-dependent-information-constants)*