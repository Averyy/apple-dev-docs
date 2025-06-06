# Time Utilities

**Framework**: Core Foundation

#### Overview

Core Foundation measures time in units of seconds. The base data type is the [`CFTimeInterval`](cftimeinterval.md), which measures the difference in seconds between two times. Fixed times, or dates, are defined by the [`CFAbsoluteTime`](cfabsolutetime.md) data type, which measures the time interval between a particular date and the absolute reference date of Jan 1 2001 00:00:00 GMT.

The [`CFGregorianDate`](cfgregoriandate.md) structure represents absolute times in terms of the Gregorian calendar. Functions such as [`CFAbsoluteTimeGetGregorianDate(_:_:)`](cfabsolutetimegetgregoriandate(_:_:).md) use a [`CFTimeZone`](cftimezone.md) object to obtain the local time in a particular time zone.

The [`CFDate`](cfdate.md) opaque type wraps an absolute time into a [`CFTypeRef`](cftyperef.md)-base object, allowing you to put time objects into collections and property lists and to be handled by other object-oriented parts of Core Foundation.

## Topics

### Core Foundation Time Utilities Miscellaneous Functions
- [func CFAbsoluteTimeAddGregorianUnits(CFAbsoluteTime, CFTimeZone!, CFGregorianUnits) -> CFAbsoluteTime](cfabsolutetimeaddgregorianunits(_:_:_:).md)
  Adds a time interval, expressed as Gregorian units, to a given absolute time.
- [func CFAbsoluteTimeGetCurrent() -> CFAbsoluteTime](cfabsolutetimegetcurrent().md)
  Returns the current system absolute time.
- [func CFAbsoluteTimeGetDayOfWeek(CFAbsoluteTime, CFTimeZone!) -> Int32](cfabsolutetimegetdayofweek(_:_:).md)
  Returns an integer representing the day of the week indicated by the specified absolute time.
- [func CFAbsoluteTimeGetDayOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32](cfabsolutetimegetdayofyear(_:_:).md)
  Returns an integer representing the day of the year indicated by the specified absolute time.
- [func CFAbsoluteTimeGetDifferenceAsGregorianUnits(CFAbsoluteTime, CFAbsoluteTime, CFTimeZone!, CFOptionFlags) -> CFGregorianUnits](cfabsolutetimegetdifferenceasgregorianunits(_:_:_:_:).md)
  Computes the time difference between two specified absolute times and returns the result as an interval in Gregorian units.
- [func CFAbsoluteTimeGetGregorianDate(CFAbsoluteTime, CFTimeZone!) -> CFGregorianDate](cfabsolutetimegetgregoriandate(_:_:).md)
  Converts an absolute time value into a Gregorian date.
- [func CFAbsoluteTimeGetWeekOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32](cfabsolutetimegetweekofyear(_:_:).md)
  Returns an integer representing the week of the year indicated by the specified absolute time.
- [func CFGregorianDateGetAbsoluteTime(CFGregorianDate, CFTimeZone!) -> CFAbsoluteTime](cfgregoriandategetabsolutetime(_:_:).md)
  Converts a Gregorian date value into an absolute time value.
- [func CFGregorianDateIsValid(CFGregorianDate, CFOptionFlags) -> Bool](cfgregoriandateisvalid(_:_:).md)
  Checks the specified fields of a CFGregorianDate structure for valid values.
### Data Types
- [typealias CFAbsoluteTime](cfabsolutetime.md)
  Type used to represent a specific point in time relative to the absolute reference date of 1 Jan 2001 00:00:00 GMT.
- [struct CFGregorianDate](cfgregoriandate.md)
  Structure used to represent a point in time using the Gregorian calendar.
- [struct CFGregorianUnits](cfgregorianunits.md)
  Structure used to represent a time interval in Gregorian units.
- [typealias CFTimeInterval](cftimeinterval.md)
  Type used to represent elapsed time in seconds.
### Constants
- [struct CFGregorianUnitFlags](cfgregorianunitflags.md)
  These option flags are used as a mask to indicate a specific set of fields in the CFGregorianDate or CFGregorianUnits structures.
- [Predefined Time Interval Values](predefined-time-interval-values.md)
  Time intervals between the absolute reference date and certain other dates.

## See Also

- [Date and Time Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/CFDatesAndTimes.html#//apple_ref/doc/uid/10000125i)
- [Base Utilities](base-utilities.md)
- [Byte-Order Utilities](byte-order-utilities.md)
- [Core Foundation URL Access Utilities](core-foundation-url-access-utilities.md)
- [Preferences Utilities](preferences-utilities.md)
- [Socket Name Server Utilities](socket-name-server-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/time-utilities)*