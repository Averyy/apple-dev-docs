# ColorSyncProfileCopyHeader(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Copies the header from a profile.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func ColorSyncProfileCopyHeader(_ prof: ColorSyncProfile!) -> Unmanaged<CFData>!
```

```c
extern CFDataRefColorSyncProfileCopyHeader(ColorSyncProfileRef prof);
```

## Return Value

The profile header (in host endianness), or `NULL` in case of failure.

## Parameters

- `prof`: The profile to copy the header from.

## See Also

### Reading profile data
- [func ColorSyncProfileCopyDescriptionString(ColorSyncProfile!) -> Unmanaged<CFString>?](./colorsyncprofilecopydescriptionstring%28_%29.md)
  Copies the localized description string of a profile.
- [func ColorSyncProfileGetURL(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>!](./colorsyncprofilegeturl%28_,_%29.md)
  Returns the URL of a profile.
- [func ColorSyncProfileGetTypeID() -> CFTypeID](./colorsyncprofilegettypeid%28%29.md)
  Returns the unique identifier for the ColorSync profile opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecopyheader(_:))*