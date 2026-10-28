# CFAbsoluteTimeGetDifferenceAsGregorianUnits(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Computes the time difference between two specified absolute times and returns the result as an interval in Gregorian units.

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
func CFAbsoluteTimeGetDifferenceAsGregorianUnits(_ at1: CFAbsoluteTime, _ at2: CFAbsoluteTime, _ tz: CFTimeZone!, _ unitFlags: CFOptionFlags) -> CFGregorianUnits
```

```c
extern CFGregorianUnits CFAbsoluteTimeGetDifferenceAsGregorianUnits(CFAbsoluteTime at1, CFAbsoluteTime at2, CFTimeZoneRef tz, CFOptionFlags unitFlags);
```

## Return Value

The difference between the specified absolute times (as `at1 - at2`—if `at1` is earlier than `at2`, the result is negative) expressed in the units specified by `unitFlags`.

## Discussion

The temporal difference is expressed as accurately as possible, given the units specified. For example, if you asked for the number of months and hours between 2:30pm on April 8 2005 and 5:45pm September 9 2005, the result would be 5 months and 27 hours.

The following example prints the number of hours and minutes between the current time (now) and the reference date (1 January 2001 00:00:00 GMT).

```objc
CFAbsoluteTime now = CFAbsoluteTimeGetCurrent ();
 
CFGregorianUnits units = CFAbsoluteTimeGetDifferenceAsGregorianUnits
    (now, 0, NULL, (kCFGregorianUnitsHours | kCFGregorianUnitsMinutes));
 
CFStringRef output = CFStringCreateWithFormat
    (NULL, 0, CFSTR("hours: %d; minutes: %d"), units.hours, units.minutes);
CFShow(output);
```

## Parameters

- `at1`: An absolute time.
- `at2`: An absolute time.
- `tz`: The time zone to use for time correction. Pass `NULL` for GMT.
- `unitFlags`: A mask that specifies which Gregorian unit fields to use when converting the absolute time difference into a Gregorian interval. See [`CFGregorianUnitFlags`](./cfgregorianunitflags.md) for a list of values from which to construct the mask.

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
- [func CFAbsoluteTimeGetGregorianDate(CFAbsoluteTime, CFTimeZone!) -> CFGregorianDate](./cfabsolutetimegetgregoriandate%28_,_%29.md)
  Converts an absolute time value into a Gregorian date.
- [func CFAbsoluteTimeGetWeekOfYear(CFAbsoluteTime, CFTimeZone!) -> Int32](./cfabsolutetimegetweekofyear%28_,_%29.md)
  Returns an integer representing the week of the year indicated by the specified absolute time.
- [func CFGregorianDateGetAbsoluteTime(CFGregorianDate, CFTimeZone!) -> CFAbsoluteTime](./cfgregoriandategetabsolutetime%28_,_%29.md)
  Converts a Gregorian date value into an absolute time value.
- [func CFGregorianDateIsValid(CFGregorianDate, CFOptionFlags) -> Bool](./cfgregoriandateisvalid%28_,_%29.md)
  Checks the specified fields of a CFGregorianDate structure for valid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfabsolutetimegetdifferenceasgregorianunits(_:_:_:_:))*