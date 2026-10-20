# ColorSyncProfileGetURL(_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Returns the URL of a profile.

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
func ColorSyncProfileGetURL(_ prof: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>!
```

```c
extern CFURLRefColorSyncProfileGetURL(ColorSyncProfileRef prof, CFErrorRef*error);
```

#### Return Value

The profile’s URL on success, or `NULL` in case of failure.

## Parameters

- `prof`: The profile to get the URL from.
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

### Reading profile data
- [func ColorSyncProfileCopyDescriptionString(ColorSyncProfile!) -> Unmanaged<CFString>?](./colorsyncprofilecopydescriptionstring%28_%29.md)
  Copies the localized description string of a profile.
- [func ColorSyncProfileCopyHeader(ColorSyncProfile!) -> Unmanaged<CFData>!](./colorsyncprofilecopyheader%28_%29.md)
  Copies the header from a profile.
- [func ColorSyncProfileGetTypeID() -> CFTypeID](./colorsyncprofilegettypeid%28%29.md)
  Returns the unique identifier for the ColorSync profile opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilegeturl(_:_:))*