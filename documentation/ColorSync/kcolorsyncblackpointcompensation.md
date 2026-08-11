# kColorSyncBlackPointCompensation

**Framework**: ColorSync  
**Kind**: var

A key whose `CFBooleanRef` value enables or disables black point compensation.

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
var kColorSyncBlackPointCompensation: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncBestQuality: Unmanaged<CFString>!](kcolorsyncbestquality.md)
  A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that does not coalesce profile transforms; the default.
- [var kColorSyncConvertQuality: Unmanaged<CFString>!](kcolorsyncconvertquality.md)
  A key for the quality of the conversion performed by the transform.
- [var kColorSyncDraftQuality: Unmanaged<CFString>!](kcolorsyncdraftquality.md)
  A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that coalesces all transforms and does not interpolate.
- [var kColorSyncNormalQuality: Unmanaged<CFString>!](kcolorsyncnormalquality.md)
  A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that coalesces all transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncblackpointcompensation)*