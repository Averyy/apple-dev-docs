# CFTimeZoneCopyAbbreviation(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the abbreviation of a time zone at a specified date.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFTimeZoneCopyAbbreviation(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> CFString!
```

#### Return Value

A string containing the time zone abbreviation of `at`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Note that the abbreviation may be different at different dates. For example, during daylight savings time the US/Eastern time zone has an abbreviation of “EDT.” At other times, its abbreviation is “EST.”

## Parameters

- `tz`: The time zone to use.
- `at`: The absolute time at which to obtain the abbreviation.

## See Also

- [func CFTimeZoneCopyAbbreviationDictionary() -> CFDictionary!](cftimezonecopyabbreviationdictionary().md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [func CFTimeZoneCopyDefault() -> CFTimeZone!](cftimezonecopydefault().md)
  Returns the default time zone set for your application.
- [func CFTimeZoneCopySystem() -> CFTimeZone!](cftimezonecopysystem().md)
  Returns the time zone currently used by the system.
- [func CFTimeZoneSetDefault(CFTimeZone!)](cftimezonesetdefault(_:).md)
  Sets the default time zone for your application the given time zone.
- [func CFTimeZoneCopyKnownNames() -> CFArray!](cftimezonecopyknownnames().md)
  Returns an array of strings containing the names of all the time zones known to the system.
- [func CFTimeZoneResetSystem()](cftimezoneresetsystem().md)
  Clears the previously determined system time zone, if any.
- [func CFTimeZoneSetAbbreviationDictionary(CFDictionary!)](cftimezonesetabbreviationdictionary(_:).md)
  Sets the abbreviation dictionary to a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecopyabbreviation(_:_:))*