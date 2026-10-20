# ColorSyncProfileGetMD5(_:)

**Framework**: ColorSync  
**Kind**: func

Returns the MD5 digest for a profile.

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
func ColorSyncProfileGetMD5(_ prof: ColorSyncProfile!) -> ColorSyncMD5
```

#### Return Value

The MD5 digest for the profile, calculated as defined by the ICC specification, or a “zero” signature (filled with zeros) in case of failure.

## Parameters

- `prof`: The profile to compute the digest for.

## See Also

- [struct ColorSyncMD5](colorsyncmd5.md)
  An MD5 digest that uniquely identifies a profile, as defined by the ICC specification.
- [var COLORSYNC_MD5_LENGTH: Int32](colorsync_md5_length.md)
- [var kColorSyncProfileMD5Digest: Unmanaged<CFString>!](kcolorsyncprofilemd5digest.md)
  A key for the profile’s MD5 digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilegetmd5(_:))*