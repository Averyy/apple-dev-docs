# kColorSyncHeadroomAdaptiveGainCurveColorVolumeTransform

**Framework**: ColorSync  
**Kind**: var

Top-level container (CFDictionaryRef) for the color volume transform.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var kColorSyncHeadroomAdaptiveGainCurveColorVolumeTransform: Unmanaged<CFString>
```

#### Discussion

It may contain parameters for Headroom-Adaptive tone mapping or indicate usage of the Reference-White Tone Mapping Method. It allows for specifying a custom HDR Reference White luminance.

## See Also

- [var kColorSyncAlternateCurveCount: Unmanaged<CFString>](kcolorsyncalternatecurvecount.md)
  Number of alternate (tone-mapped) curves encoded in the metadata (uint8_t in the range [0, 4]). Each alternate targets a different display headroom.
- [var kColorSyncAlternateGainCurveInfo: Unmanaged<CFString>](kcolorsyncalternategaincurveinfo.md)
  CFArrayRef of per-alternate dictionaries.
- [var kColorSyncBaselineHeadroomStops: Unmanaged<CFString>](kcolorsyncbaselineheadroomstops.md)
  Headroom of the source (baseline) curve in stops (log2) above reference white (float in the range [0.0, 6.0]).
- [var kColorSyncCustomHDRReferenceWhite: Unmanaged<CFString>](kcolorsynccustomhdrreferencewhite.md)
  Custom reference white luminance in nits (float), overriding the standard 203-nit reference white.
- [var kColorSyncHeadroomAdaptiveGainCurveApplicationVersion: Unmanaged<CFString>](kcolorsyncheadroomadaptivegaincurveapplicationversion.md)
  Application version (uint8_t). 3-bit field from ST 2094-50 Table C.1. Must be `0`; the framework rejects any other value.
- [var kColorSyncHeadroomAdaptiveGainCurveInfo: Unmanaged<CFString>](kcolorsyncheadroomadaptivegaincurveinfo.md)
  Container (CFDictionaryRef) for the adaptive gain curve data.
- [var kColorSyncHeadroomAdaptiveToneMappingInfo: Unmanaged<CFString>](kcolorsyncheadroomadaptivetonemappinginfo.md)
  Container (CFDictionaryRef) for Headroom-Adaptive tone mapping parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncheadroomadaptivegaincurvecolorvolumetransform)*