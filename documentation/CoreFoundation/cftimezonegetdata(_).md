# CFTimeZoneGetData(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the data that stores the information used by a time zone.

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
func CFTimeZoneGetData(_ tz: CFTimeZone!) -> CFData!
```

```c
extern CFDataRefCFTimeZoneGetData(CFTimeZoneRef tz);
```

## Return Value

The data used to store `tz`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1). May be `NULL` if the timezone does not have any data or use Olson data for its information.

## Parameters

- `tz`: The time zone to analyze.

## See Also

### Getting Information About Time Zones
- [func CFTimeZoneGetName(CFTimeZone!) -> CFString!](./cftimezonegetname%28_%29.md)
  Returns the geopolitical region name that identifies a given time zone.
- [func CFTimeZoneCopyLocalizedName(CFTimeZone!, CFTimeZoneNameStyle, CFLocale!) -> CFString!](./cftimezonecopylocalizedname%28_,_,_%29.md)
  Returns the localized name of a given time zone.
- [func CFTimeZoneGetSecondsFromGMT(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval](./cftimezonegetsecondsfromgmt%28_,_%29.md)
  Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonegetdata(_:))*