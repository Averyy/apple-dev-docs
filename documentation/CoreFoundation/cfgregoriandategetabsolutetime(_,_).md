# CFGregorianDateGetAbsoluteTime(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Converts a Gregorian date value into an absolute time value.

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
func CFGregorianDateGetAbsoluteTime(_ gdate: CFGregorianDate, _ tz: CFTimeZone!) -> CFAbsoluteTime
```

```c
extern CFAbsoluteTime CFGregorianDateGetAbsoluteTime(CFGregorianDate gdate, CFTimeZoneRef tz);
```

#### Return Value

The absolute time equivalent of `gdate`.

## Parameters

- `gdate`: The Gregorian date to convert.
- `tz`: The time zone to use for time correction. Pass `NULL` for GMT.

## See Also

### Core Foundation Time Utilities Miscellaneous Functions
- [func CFAbsoluteTimeAddGregorianUnits(CFAbsoluteTime, CFTimeZone!, CFGregorianUnits) -> CFAbsoluteTime](./cfabsolutetimeaddgregorianunits%28_,_,_%29.md)
  Adds a time interval, expressed as Gregorian units, to a given absolute time.
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
- [func CFGregorianDateIsValid(CFGregorianDate, CFOptionFlags) -> Bool](./cfgregoriandateisvalid%28_,_%29.md)
  Checks the specified fields of a CFGregorianDate structure for valid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgregoriandategetabsolutetime(_:_:))*