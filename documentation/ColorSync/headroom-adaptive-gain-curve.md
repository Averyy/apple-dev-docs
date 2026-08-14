# Headroom Adaptive Gain Curve

**Framework**: ColorSync

Work with SMPTE ST 2094-50 tone-mapping metadata shared between HDR stills and video.

#### Overview

A Headroom Adaptive Gain Curve (HAGC) is tone-mapping metadata that describes how an HDR image or video adapts its highlights, midtones, and shadows for a display. The metadata takes effect when a display’s *headroom*, the brightness it can show above reference white, is less than the content needs. An HAGC combines an HDR reference white anchor, the content value mapped to the display’s reference white, and an optional set of gain curves, following the SMPTE ST 2094-50 standard and the matching ICC HAGC profile tag. Because still images and video share one binary representation, you can move the metadata you add to a still into a video stream, and move metadata from a video stream into a still.

ColorSync provides HAGC through two APIs that describe the same data:

- In Swift, use [`ColorSyncProfile.HeadroomAdaptiveGainCurve`](colorsyncprofile/headroomadaptivegaincurve-swift.struct.md) to check the curve’s structure at compile time and report invalid values by throwing an error.
- In a C dictionary or binary API, use [`ColorSyncProfile`](colorsyncprofile.md) to read an info dictionary or the raw SMPTE ST 2094-50 binary payload, and create a copy of an ICC profile with the HAGC tag attached.

> **Note**: An ICC profile can carry an HAGC tag only when its transfer function is PQ, HLG, or linear.

When [`Image I/O`](https://developer.apple.com/documentation/imageio) decodes an ISO 21496-1 gain-map image to HDR with [`kCGImageSourceDecodeToHDR`](https://developer.apple.com/documentation/imageio/kcgimagesourcedecodetohdr), it derives HAGC metadata automatically by analyzing the ISO gain map.

When the SDR target isn’t known or can’t be computed, the HAGC metadata can indicate a default headroom-adaptive tone mapping, the Reference White Tone Mapping Operator (RWTMO), which is the recommended tone mapping for ISO 22028-5 images.

The system applies HAGC metadata embedded in HDR images and video automatically. Stills render through [`Core Graphics`](https://developer.apple.com/documentation/coregraphics), [`Core Image`](https://developer.apple.com/documentation/coreimage), and [`Core Animation`](https://developer.apple.com/documentation/quartzcore), including the [`UIImageView`](https://developer.apple.com/documentation/uikit/uiimageview) and [`NSImageView`](https://developer.apple.com/documentation/appkit/nsimageview) classes. Video plays through [`AVFoundation`](https://developer.apple.com/documentation/avfoundation), which carries the HAGC metadata as a SMPTE ST 2094-50 binary payload in a timed-metadata `it35` (ITU-T T.35) `mebx` track, identified by `it35/B500900001:SMPTE-ST2094-50`.

## Topics

### Authoring a gain curve
- [Authoring Headroom Adaptive Gain Curve metadata](authoring-headroom-adaptive-gain-curve-metadata.md)
  Create tone-mapping metadata that adapts HDR content to a display’s headroom.
### Detecting a curve
- [func ColorSyncProfileContainsHeadroomAdaptiveGainCurve(ColorSyncProfile) -> Bool](colorsyncprofilecontainsheadroomadaptivegaincurve(_:).md)
  Returns whether a profile contains a Headroom Adaptive Gain Curve tag.
### Reading a curve in Swift
- [var headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve?](colorsyncprofile/headroomadaptivegaincurve-swift.property.md)
  The Headroom Adaptive Gain Curve embedded in this profile, or `nil` if it carries no HAGC tag.
- [var headroomAdaptiveGainCurveMetadata: Data?](colorsyncprofile/headroomadaptivegaincurvemetadata.md)
  The raw Headroom Adaptive Gain Curve data embedded in this profile, or `nil` if it carries no HAGC tag.
### Describing a curve in Swift
- [ColorSyncProfile.HeadroomAdaptiveGainCurve](colorsyncprofile/headroomadaptivegaincurve-swift.struct.md)
  Headroom Adaptive Gain Curve metadata that describes how to tone map a profile’s HDR content to the dynamic range available on the display.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct.md)
  A color volume transform that maps HDR content into a display’s dynamic range.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping.md)
  Headroom-adaptive tone mapping that adjusts HDR content to the display’s available headroom.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum.md)
  The tone-mapping method: reference-white-based, or a headroom-adaptive gain curve.
- [ColorSyncProfile.HeadroomAdaptiveGainCurve.Error](colorsyncprofile/headroomadaptivegaincurve-swift.struct/error.md)
  An error thrown while constructing Headroom Adaptive Gain Curve metadata.
### Attaching a curve in Swift
- [func adding(headroomAdaptiveGainCurve: ColorSyncProfile.HeadroomAdaptiveGainCurve) -> ColorSyncProfile?](colorsyncprofile/adding(headroomadaptivegaincurve:).md)
  Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.
- [func adding(headroomAdaptiveGainCurveMetadata: Data, options: ColorSyncProfile.HeadroomAdaptiveGainCurveOptions) -> ColorSyncProfile?](colorsyncprofile/adding(headroomadaptivegaincurvemetadata:options:).md)
  Returns a copy of this profile with raw Headroom Adaptive Gain Curve data embedded as an HAGC tag.
- [ColorSyncProfile.HeadroomAdaptiveGainCurveOptions](colorsyncprofile/headroomadaptivegaincurveoptions.md)
  Options that configure how a Headroom Adaptive Gain Curve is read from or embedded in a profile.
### Structuring the info dictionary
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
- [var kColorSyncHeadroomAdaptiveToneMappingInfo: Unmanaged<CFString>](kcolorsyncheadroomadaptivetonemappinginfo.md)
  Container (CFDictionaryRef) for Headroom-Adaptive tone mapping parameters.
### Describing gain curves
- [var kColorSyncAlternateCurveHeadroomStops: Unmanaged<CFString>](kcolorsyncalternatecurveheadroomstops.md)
  Target headroom of this alternate curve in stops (log2) above reference white (float in the range [0.0, 6.0]). The renderer selects the closest alternate to the actual display headroom.
- [var kColorSyncCommonComponentMixing: Unmanaged<CFString>](kcolorsynccommoncomponentmixing.md)
  CFBooleanRef indicating whether alternate curves share one component-mixing configuration.
- [var kColorSyncCommonCurveParameters: Unmanaged<CFString>](kcolorsynccommoncurveparameters.md)
  CFBooleanRef indicating whether alternate curves share common gain-curve parameters.
- [var kColorSyncComponentMix: Unmanaged<CFString>](kcolorsynccomponentmix.md)
  Component mixing type (uint8_t) matching `component_mixing_value` in ST 2094-50.
- [var kColorSyncControlPointSlopes: Unmanaged<CFString>](kcolorsynccontrolpointslopes.md)
  CFArrayRef of floats — explicit tangent slopes at each control point, expressed as tan(slope_angle). Only present when [`kColorSyncInterpolateSlopes`](kcolorsyncinterpolateslopes.md) is false.
- [var kColorSyncControlPointsX: Unmanaged<CFString>](kcolorsynccontrolpointsx.md)
  CFArrayRef of floats — the X-axis coordinates of the gain-curve control points.
- [var kColorSyncControlPointsY: Unmanaged<CFString>](kcolorsynccontrolpointsy.md)
  CFArrayRef of floats — the Y-axis gain offsets at the control points.
- [var kColorSyncGainCurveChromaticities: Unmanaged<CFString>](kcolorsyncgaincurvechromaticities.md)
  Chromaticity primaries used to compute the driving signal for the gain curve.
- [var kColorSyncInterpolateSlopes: Unmanaged<CFString>](kcolorsyncinterpolateslopes.md)
  CFBooleanRef controlling how the framework determines control-point slopes.
- [var kColorSyncMaxControlPointIndex: Unmanaged<CFString>](kcolorsyncmaxcontrolpointindex.md)
  Index of the last control point (uint8_t, 0–31), i.e. the number of control points minus 1. Shared across all alternates from index 0 when [`kColorSyncCommonCurveParameters`](kcolorsynccommoncurveparameters.md) is true.
### Weighting component-mix coefficients
- [var kColorSyncCoefficientBlue: Unmanaged<CFString>](kcolorsynccoefficientblue.md)
  Weight for the blue channel in the free-style component mixing sum.
- [var kColorSyncCoefficientComponent: Unmanaged<CFString>](kcolorsynccoefficientcomponent.md)
  Weight for the ‘component’ term in the free-style component mixing sum.
- [var kColorSyncCoefficientGreen: Unmanaged<CFString>](kcolorsynccoefficientgreen.md)
  Weight for the green channel in the free-style component mixing sum.
- [var kColorSyncCoefficientMaxRGB: Unmanaged<CFString>](kcolorsynccoefficientmaxrgb.md)
  Weight for the MAX(R,G,B) term in the free-style component mixing sum.
- [var kColorSyncCoefficientMinRGB: Unmanaged<CFString>](kcolorsynccoefficientminrgb.md)
  Weight for the MIN(R,G,B) term in the free-style component mixing sum.
- [var kColorSyncCoefficientRed: Unmanaged<CFString>](kcolorsynccoefficientred.md)
  Weight for the red channel in the free-style component mixing sum.
- [var kColorSyncComponentCoefficients: Unmanaged<CFString>](kcolorsynccomponentcoefficients.md)
  Sub-dictionary of custom linear-combination coefficients for free-style component mixing.

## See Also

- [Color profiles](color-profiles.md)
  Work with the ICC profiles that describe device and working color spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/headroom-adaptive-gain-curve)*