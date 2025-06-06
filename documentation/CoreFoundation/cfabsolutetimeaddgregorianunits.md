# CFAbsoluteTimeAddGregorianUnits(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a time interval, expressed as Gregorian units, to a given absolute time.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFAbsoluteTimeAddGregorianUnits(_ at: CFAbsoluteTime, _ tz: CFTimeZone!, _ units: CFGregorianUnits) -> CFAbsoluteTime
```

#### Return Value

An absolute time value equal to the sum of `at` and `units`.

## Parameters

- `at`: The absolute time to which the interval is added.
- `tz`: The time zone to use for time correction. Pass   for GMT.
- `units`: The time interval to add to  .

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfabsolutetimeaddgregorianunits(_:_:_:))*