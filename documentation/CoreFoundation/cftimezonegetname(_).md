# CFTimeZoneGetName(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the geopolitical region name that identifies a given time zone.

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
func CFTimeZoneGetName(_ tz: CFTimeZone!) -> CFString!
```

```c
extern CFStringRefCFTimeZoneGetName(CFTimeZoneRef tz);
```

## Return Value

A string containing the geopolitical region name that identifies `tz`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `tz`: The time zone to analyze.

## See Also

### Getting Information About Time Zones
- [func CFTimeZoneCopyLocalizedName(CFTimeZone!, CFTimeZoneNameStyle, CFLocale!) -> CFString!](./cftimezonecopylocalizedname%28_,_,_%29.md)
  Returns the localized name of a given time zone.
- [func CFTimeZoneGetSecondsFromGMT(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval](./cftimezonegetsecondsfromgmt%28_,_%29.md)
  Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.
- [func CFTimeZoneGetData(CFTimeZone!) -> CFData!](./cftimezonegetdata%28_%29.md)
  Returns the data that stores the information used by a time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonegetname(_:))*