# CFTimeZoneGetSecondsFromGMT(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.

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
func CFTimeZoneGetSecondsFromGMT(_ tz: CFTimeZone!, _ at: CFAbsoluteTime) -> CFTimeInterval
```

#### Return Value

The difference in seconds between `tz` and GMT at the specified date, `at`.

## Parameters

- `tz`: The time zone to analyze.
- `at`: The date at which the interval is to be computed.

## See Also

- [func CFTimeZoneGetName(CFTimeZone!) -> CFString!](cftimezonegetname(_:).md)
  Returns the geopolitical region name that identifies a given time zone.
- [func CFTimeZoneCopyLocalizedName(CFTimeZone!, CFTimeZoneNameStyle, CFLocale!) -> CFString!](cftimezonecopylocalizedname(_:_:_:).md)
  Returns the localized name of a given time zone.
- [func CFTimeZoneGetData(CFTimeZone!) -> CFData!](cftimezonegetdata(_:).md)
  Returns the data that stores the information used by a time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonegetsecondsfromgmt(_:_:))*