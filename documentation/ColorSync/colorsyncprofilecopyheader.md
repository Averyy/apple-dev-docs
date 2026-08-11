# ColorSyncProfileCopyHeader(_:)

**Framework**: ColorSync  
**Kind**: func

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

#### Return Value

The profile header (in host endianness), or `NULL` in case of failure.

## Parameters

- `prof`: The profile to copy the header from.

## See Also

- [func ColorSyncProfileCopyDescriptionString(ColorSyncProfile!) -> Unmanaged<CFString>?](colorsyncprofilecopydescriptionstring(_:).md)
  Copies the localized description string of a profile.
- [func ColorSyncProfileGetURL(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>!](colorsyncprofilegeturl(_:_:).md)
  Returns the URL of a profile.
- [func ColorSyncProfileGetTypeID() -> CFTypeID](colorsyncprofilegettypeid().md)
  Returns the unique identifier for the ColorSync profile opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecopyheader(_:))*