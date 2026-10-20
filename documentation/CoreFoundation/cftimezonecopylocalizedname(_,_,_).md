# CFTimeZoneCopyLocalizedName(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the localized name of a given time zone.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFTimeZoneCopyLocalizedName(_ tz: CFTimeZone!, _ style: CFTimeZoneNameStyle, _ locale: CFLocale!) -> CFString!
```

```c
extern CFStringRefCFTimeZoneCopyLocalizedName(CFTimeZoneRef tz, CFTimeZoneNameStyle style, CFLocaleRef locale);
```

#### Return Value

The name of `tz` localized for `locale`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `tz`: The time zone to analyze.
- `style`: The style for the returned name.
- `locale`: The locale for which to localize the returned name.

## See Also

### Getting Information About Time Zones
- [func CFTimeZoneGetName(CFTimeZone!) -> CFString!](./cftimezonegetname%28_%29.md)
  Returns the geopolitical region name that identifies a given time zone.
- [func CFTimeZoneGetSecondsFromGMT(CFTimeZone!, CFAbsoluteTime) -> CFTimeInterval](./cftimezonegetsecondsfromgmt%28_,_%29.md)
  Returns the difference in seconds between the receiver and Greenwich Mean Time (GMT) at the specified date.
- [func CFTimeZoneGetData(CFTimeZone!) -> CFData!](./cftimezonegetdata%28_%29.md)
  Returns the data that stores the information used by a time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftimezonecopylocalizedname(_:_:_:))*