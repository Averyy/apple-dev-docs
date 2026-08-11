# kColorSyncDraftQuality

**Framework**: ColorSync  
**Kind**: var

A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that coalesces all transforms and does not interpolate.

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
var kColorSyncDraftQuality: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncBestQuality: Unmanaged<CFString>!](kcolorsyncbestquality.md)
  A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that does not coalesce profile transforms; the default.
- [var kColorSyncBlackPointCompensation: Unmanaged<CFString>!](kcolorsyncblackpointcompensation.md)
  A key whose `CFBooleanRef` value enables or disables black point compensation.
- [var kColorSyncConvertQuality: Unmanaged<CFString>!](kcolorsyncconvertquality.md)
  A key for the quality of the conversion performed by the transform.
- [var kColorSyncNormalQuality: Unmanaged<CFString>!](kcolorsyncnormalquality.md)
  A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that coalesces all transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncdraftquality)*