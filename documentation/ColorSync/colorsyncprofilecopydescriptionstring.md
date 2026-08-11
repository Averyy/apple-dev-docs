# ColorSyncProfileCopyDescriptionString(_:)

**Framework**: ColorSync  
**Kind**: func

Copies the localized description string of a profile.

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
func ColorSyncProfileCopyDescriptionString(_ prof: ColorSyncProfile!) -> Unmanaged<CFString>?
```

#### Return Value

The profile description, localized to the current locale.

## Parameters

- `prof`: The profile to copy the description string from.

## See Also

- [func ColorSyncProfileCopyHeader(ColorSyncProfile!) -> Unmanaged<CFData>!](colorsyncprofilecopyheader(_:).md)
  Copies the header from a profile.
- [func ColorSyncProfileGetURL(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>!](colorsyncprofilegeturl(_:_:).md)
  Returns the URL of a profile.
- [func ColorSyncProfileGetTypeID() -> CFTypeID](colorsyncprofilegettypeid().md)
  Returns the unique identifier for the ColorSync profile opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecopydescriptionstring(_:))*