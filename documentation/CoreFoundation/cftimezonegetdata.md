# CFTimeZoneGetData(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the data that stores the information used by a time zone.

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
func CFTimeZoneGetData(_ tz: CFTimeZone!) -> CFData!
```

#### Return Value

The data used to store `tz`. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1). May be `NULL` if the timezone does not have any data or use Olson data for its information.

## Parameters

- `tz`: The time zone to analyze.

## See Also

- [func CFTimeZoneGetName(CFTimeZone!) -> CFString!](cftimezonegetname(_:).md)
  Returns the geopolitical region name that identifies a given time zone.
- [func CFTimeZoneCopyLocalizedName(CFTimeZone!, CFTimeZoneNameStyle, CFLocale!) -> CFString!](cftimezonecopylocalizedname(_:_:_:).md)
  Returns the localized name of a given time zone.
- [func CFTimeZoneGetSecondsFromGMT(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval](cftimezonegetsecondsfromgmt(_:_:).md)
  Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonegetdata(_:))*