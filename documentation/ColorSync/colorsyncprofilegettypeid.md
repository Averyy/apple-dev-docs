# ColorSyncProfileGetTypeID()

**Framework**: ColorSync  
**Kind**: func

Returns the unique identifier for the ColorSync profile opaque type.

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
func ColorSyncProfileGetTypeID() -> CFTypeID
```

#### Return Value

The `CFTypeID` for `ColorSyncProfile` objects.

## See Also

- [func ColorSyncProfileCopyDescriptionString(ColorSyncProfile!) -> Unmanaged<CFString>?](colorsyncprofilecopydescriptionstring(_:).md)
  Copies the localized description string of a profile.
- [func ColorSyncProfileCopyHeader(ColorSyncProfile!) -> Unmanaged<CFData>!](colorsyncprofilecopyheader(_:).md)
  Copies the header from a profile.
- [func ColorSyncProfileGetURL(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>!](colorsyncprofilegeturl(_:_:).md)
  Returns the URL of a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilegettypeid())*