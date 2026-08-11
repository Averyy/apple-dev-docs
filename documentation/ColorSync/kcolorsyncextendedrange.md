# kColorSyncExtendedRange

**Framework**: ColorSync  
**Kind**: var

A key whose `CFBooleanRef` value enables or disables extended range.

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
var kColorSyncExtendedRange: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncConvertUseExtendedRange: Unmanaged<CFString>!](kcolorsyncconvertuseextendedrange.md)
  A key whose `CFBooleanRef` value allows float data to exceed the `[0.0, 1.0]` range.
- [var kColorSyncTransformUseITU709OETF: Unmanaged<CFString>!](kcolorsynctransformuseitu709oetf.md)
  A key whose `CFBooleanRef` value uses the ITU-R BT.709 opto-electronic transfer function.
- [var kColorSyncHDRDerivative: Unmanaged<CFString>!](kcolorsynchdrderivative.md)
  A key for the HDR derivative to apply to the profile in a profile-sequence dictionary.
- [var kColorSyncPQDerivative: Unmanaged<CFString>!](kcolorsyncpqderivative.md)
  A [`kColorSyncHDRDerivative`](kcolorsynchdrderivative.md) value selecting the PQ HDR derivative.
- [var kColorSyncHLGDerivative: Unmanaged<CFString>!](kcolorsynchlgderivative.md)
  A [`kColorSyncHDRDerivative`](kcolorsynchdrderivative.md) value selecting the HLG HDR derivative.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncextendedrange)*