# CFTimeZoneResetSystem()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Clears the previously determined system time zone, if any.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFTimeZoneResetSystem()
```

```c
extern void CFTimeZoneResetSystem();
```

#### Discussion

If the default time zone is set to the same value as the system time zone or has not been explicitly set, this function clears it as well.

Subsequent calls to [`CFTimeZoneCopySystem()`](./cftimezonecopysystem%28%29.md) will attempt to re-determine the system time zone.

## See Also

### System and Default Time Zones and Information
- [func CFTimeZoneCopyAbbreviationDictionary() -> CFDictionary!](./cftimezonecopyabbreviationdictionary%28%29.md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [func CFTimeZoneCopyAbbreviation(CFTimeZone!, CFAbsoluteTime) -> CFString!](./cftimezonecopyabbreviation%28_,_%29.md)
  Returns the abbreviation of a time zone at a specified date.
- [func CFTimeZoneCopyDefault() -> CFTimeZone!](./cftimezonecopydefault%28%29.md)
  Returns the default time zone set for your application.
- [func CFTimeZoneCopySystem() -> CFTimeZone!](./cftimezonecopysystem%28%29.md)
  Returns the time zone currently used by the system.
- [func CFTimeZoneSetDefault(CFTimeZone!)](./cftimezonesetdefault%28_%29.md)
  Sets the default time zone for your application the given time zone.
- [func CFTimeZoneCopyKnownNames() -> CFArray!](./cftimezonecopyknownnames%28%29.md)
  Returns an array of strings containing the names of all the time zones known to the system.
- [func CFTimeZoneSetAbbreviationDictionary(CFDictionary!)](./cftimezonesetabbreviationdictionary%28_%29.md)
  Sets the abbreviation dictionary to a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezoneresetsystem())*