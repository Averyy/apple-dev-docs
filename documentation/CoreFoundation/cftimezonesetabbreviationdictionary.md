# CFTimeZoneSetAbbreviationDictionary(_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the abbreviation dictionary to a given dictionary.

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
func CFTimeZoneSetAbbreviationDictionary(_ dict: CFDictionary!)
```

## Parameters

- `dict`: A dictionary containing key-value pairs for looking up time zone names given their abbreviations. The keys should be CFString objects containing the abbreviations; the values should be CFString objects containing their corresponding geopolitical region names.

## See Also

- [func CFTimeZoneCopyAbbreviationDictionary() -> CFDictionary!](cftimezonecopyabbreviationdictionary().md)
  Returns a dictionary holding the mappings of time zone abbreviations to time zone names.
- [func CFTimeZoneCopyAbbreviation(CFTimeZone!, CFAbsoluteTime) -> CFString!](cftimezonecopyabbreviation(_:_:).md)
  Returns the abbreviation of a time zone at a specified date.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonesetabbreviationdictionary(_:))*