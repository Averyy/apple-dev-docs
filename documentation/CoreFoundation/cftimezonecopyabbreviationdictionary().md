# CFTimeZoneCopyAbbreviationDictionary()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a dictionary holding the mappings of time zone abbreviations to time zone names.

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
func CFTimeZoneCopyAbbreviationDictionary() -> CFDictionary!
```

```c
extern CFDictionaryRefCFTimeZoneCopyAbbreviationDictionary();
```

#### Return Value

A dictionary containing the mappings of time zone abbreviations to time zone names. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

More than one time zone may have the same abbreviation. For example, US/Pacific and Canada/Pacific both use the abbreviation “PST.” In these cases this function chooses a single name to map the abbreviation to.

## See Also

### System and Default Time Zones and Information
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
- [func CFTimeZoneResetSystem()](./cftimezoneresetsystem%28%29.md)
  Clears the previously determined system time zone, if any.
- [func CFTimeZoneSetAbbreviationDictionary(CFDictionary!)](./cftimezonesetabbreviationdictionary%28_%29.md)
  Sets the abbreviation dictionary to a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecopyabbreviationdictionary())*