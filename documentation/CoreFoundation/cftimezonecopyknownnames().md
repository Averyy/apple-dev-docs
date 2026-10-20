# CFTimeZoneCopyKnownNames()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns an array of strings containing the names of all the time zones known to the system.

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
func CFTimeZoneCopyKnownNames() -> CFArray!
```

```c
extern CFArrayRefCFTimeZoneCopyKnownNames();
```

#### Return Value

An array containing CFString objects representing all the known time zone names. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

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
- [func CFTimeZoneResetSystem()](./cftimezoneresetsystem%28%29.md)
  Clears the previously determined system time zone, if any.
- [func CFTimeZoneSetAbbreviationDictionary(CFDictionary!)](./cftimezonesetabbreviationdictionary%28_%29.md)
  Sets the abbreviation dictionary to a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecopyknownnames())*