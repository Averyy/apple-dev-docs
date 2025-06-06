# CFTimeZoneCopySystem()

**Framework**: Core Foundation  
**Kind**: func

Returns the time zone currently used by the system.

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
func CFTimeZoneCopySystem() -> CFTimeZone!
```

#### Return Value

A time zone representing the time zone currently used by the system, or the GMT time zone if the current zone cannot be determined. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

- [func CFTimeZoneCopyAbbreviationDictionary() -> CFDictionary!](cftimezonecopyabbreviationdictionary().md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [func CFTimeZoneCopyAbbreviation(CFTimeZone!, CFAbsoluteTime) -> CFString!](cftimezonecopyabbreviation(_:_:).md)
  Returns the abbreviation of a time zone at a specified date.
- [func CFTimeZoneCopyDefault() -> CFTimeZone!](cftimezonecopydefault().md)
  Returns the default time zone set for your application.
- [func CFTimeZoneSetDefault(CFTimeZone!)](cftimezonesetdefault(_:).md)
  Sets the default time zone for your application the given time zone.
- [func CFTimeZoneCopyKnownNames() -> CFArray!](cftimezonecopyknownnames().md)
  Returns an array of strings containing the names of all the time zones known to the system.
- [func CFTimeZoneResetSystem()](cftimezoneresetsystem().md)
  Clears the previously determined system time zone, if any.
- [func CFTimeZoneSetAbbreviationDictionary(CFDictionary!)](cftimezonesetabbreviationdictionary(_:).md)
  Sets the abbreviation dictionary to a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecopysystem())*