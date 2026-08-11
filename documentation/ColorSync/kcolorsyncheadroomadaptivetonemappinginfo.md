# kColorSyncHeadroomAdaptiveToneMappingInfo

**Framework**: ColorSync  
**Kind**: var

Container (CFDictionaryRef) for Headroom-Adaptive tone mapping parameters.

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
var kColorSyncHeadroomAdaptiveToneMappingInfo: Unmanaged<CFString>
```

#### Discussion

Present when Headroom-Adaptive tone mapping is encoded. Contains [`kColorSyncBaselineHeadroomStops`](kcolorsyncbaselineheadroomstops.md) and either [`kColorSyncHeadroomAdaptiveGainCurveInfo`](kcolorsyncheadroomadaptivegaincurveinfo.md) or, when set to `kCFBooleanFalse`, indicates the Reference-White Tone Mapping Operator (RWTMO) method.

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
- [var kColorSyncHeadroomAdaptiveGainCurveColorVolumeTransform: Unmanaged<CFString>](kcolorsyncheadroomadaptivegaincurvecolorvolumetransform.md)
  Top-level container (CFDictionaryRef) for the color volume transform.
- [var kColorSyncHeadroomAdaptiveGainCurveInfo: Unmanaged<CFString>](kcolorsyncheadroomadaptivegaincurveinfo.md)
  Container (CFDictionaryRef) for the adaptive gain curve data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncheadroomadaptivetonemappinginfo)*