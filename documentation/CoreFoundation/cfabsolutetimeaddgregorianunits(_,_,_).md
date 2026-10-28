# CFAbsoluteTimeAddGregorianUnits(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Adds a time interval, expressed as Gregorian units, to a given absolute time.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use CFCalendar or NSCalendar API instead

## Declaration

```swift
func CFAbsoluteTimeAddGregorianUnits(_ at: CFAbsoluteTime, _ tz: CFTimeZone!, _ units: CFGregorianUnits) -> CFAbsoluteTime
```

```c
extern CFAbsoluteTime CFAbsoluteTimeAddGregorianUnits(CFAbsoluteTime at, CFTimeZoneRef tz, CFGregorianUnits units);
```

## Return Value

An absolute time value equal to the sum of `at` and `units`.

## Parameters

- `at`: The absolute time to which the interval is added.
- `tz`: The time zone to use for time correction. Pass `NULL` for GMT.
- `units`: The time interval to add to `at`.

## See Also

### Core Foundation Time Utilities Miscellaneous Functions
- [func CFAbsoluteTimeGetCurrent() -> CFAbsoluteTime](./cfabsolutetimegetcurrent%28%29.md)
  Returns the current system absolute time.
- [func CFAbsoluteTimeGetDayOfWeek(CFAbsoluteTime, CFTimeZone!) -> Int32](./cfabsolutetimegetdayofweek%28_,_%29.md)
  Returns an integer representing the day of the week indicated by the specified absolute time.
- [func CFAbsoluteTimeGetDayOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32](./cfabsolutetimegetdayofyear%28_,_%29.md)
  Returns an integer representing the day of the year indicated by the specified absolute time.
- [func CFAbsoluteTimeGetDifferenceAsGregorianUnits(CFAbsoluteTime, CFAbsoluteTime, CFTimeZone!, CFOptionFlags) -> CFGregorianUnits](./cfabsolutetimegetdifferenceasgregorianunits%28_,_,_,_%29.md)
  Computes the time difference between two specified absolute times and returns the result as an interval in Gregorian units.
- [func CFAbsoluteTimeGetGregorianDate(CFAbsoluteTime, CFTimeZone!) -> CFGregorianDate](./cfabsolutetimegetgregoriandate%28_,_%29.md)
  Converts an absolute time value into a Gregorian date.
- [func CFAbsoluteTimeGetWeekOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32](./cfabsolutetimegetweekofyear%28_,_%29.md)
  Returns an integer representing the week of the year indicated by the specified absolute time.
- [func CFGregorianDateGetAbsoluteTime(CFGregorianDate, CFTimeZone!) -> CFAbsoluteTime](./cfgregoriandategetabsolutetime%28_,_%29.md)
  Converts a Gregorian date value into an absolute time value.
- [func CFGregorianDateIsValid(CFGregorianDate, CFOptionFlags) -> Bool](./cfgregoriandateisvalid%28_,_%29.md)
  Checks the specified fields of a CFGregorianDate structure for valid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfabsolutetimeaddgregorianunits(_:_:_:))*