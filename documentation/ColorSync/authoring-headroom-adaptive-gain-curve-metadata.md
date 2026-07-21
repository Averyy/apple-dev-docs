# Authoring Headroom Adaptive Gain Curve metadata

**Framework**: ColorSync

Create tone-mapping metadata that adapts HDR content to a display’s headroom.

#### Overview

A display’s *headroom* is the luminance it can show above reference white. When that headroom is less than an HDR image or video needs, the system tone maps the content to fit. A Headroom Adaptive Gain Curve (HAGC) lets you control that tone mapping instead of relying on the system default, and stores it in a form that travels with both stills and video. You attach a curve to a [`ColorSyncProfile`](colorsyncprofile.md), either by building it from [`Swift`](https://developer.apple.com/documentation/Swift) value types or by supplying a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary). To move a curve between a still image and a video, serialize it to a compact binary encoding defined by SMPTE ST 2094-50, the industry standard for this tone-mapping metadata.

For images, attach a curve only to an ICC profile that has a PQ, HLG, or linear transfer function. For a standard-dynamic-range profile, the profile-creation functions return `nil`.

#### Add Headroom Adaptive Tone Mapping to an Icc Profile

The simplest tone mapping metadata carries only a reference white and a baseline headroom. This reproduces the system’s Reference White Tone Mapping Operator (RWTMO), so rendering stays consistent without defining an explicit curve.

The reference white is a luminance in nits: 203 nits is the HDR diffuse-white anchor defined by ITU-R BT.2408, and you override it only when mastering your content to a different anchor. The baseline headroom represents *stops*, where one stop is a doubling of luminance above reference white. A baseline of two stops describes content authored for highlights up to four times the reference white.

In Swift, build the value-type model and add it to a base profile:

```swift
typealias GainCurve = ColorSyncProfile.HeadroomAdaptiveGainCurve

let toneMapping = try GainCurve.ColorVolumeTransform.ToneMapping(
    baselineHeadroomStops: 2,
    method: .referenceWhiteBased)

let transform = try GainCurve.ColorVolumeTransform(
    customHDRReferenceWhite: 203,
    adaptiveToneMapping: toneMapping)

let curve = try GainCurve(colorVolumeTransform: transform)

let profile = baseProfile.adding(headroomAdaptiveGainCurve: curve)
```

In Objective-C, describe the same curve as a dictionary and create a copy of the profile that embeds it as an ICC HAGC tag:

```objc
NSDictionary *dict = @{
    (__bridge id)kColorSyncHeadroomAdaptiveGainCurveApplicationVersion: @0,
    (__bridge id)kColorSyncHeadroomAdaptiveGainCurveColorVolumeTransform: @{
        (__bridge id)kColorSyncCustomHDRReferenceWhite: @203,
        (__bridge id)kColorSyncHeadroomAdaptiveToneMappingInfo: @{
            (__bridge id)kColorSyncBaselineHeadroomStops: @2,
        },
    },
};

ColorSyncProfileRef profile =
    ColorSyncProfileCreateCopyWithHeadroomAdaptiveGainCurveInfoDictionary(base, (__bridge CFDictionaryRef)dict);
```

> **Note**: Setting `kColorSyncCustomHDRReferenceWhite` to a custom value encodes that value in the binary data. Passing 203 is redundant, because 203 nits is the default the system applies when you omit the key. Leave the key unset to keep the encoding compact and let the default take effect.

#### Define a Custom Gain Curve

A *gain curve* controls how the system tone maps the input signal when the display’s headroom is lower than the content’s headroom (indicated by `kColorSyncBaselineHeadroomStops`). As the system brightness changes, the display’s headroom varies, so you supply one or more custom alternate gain curves, each targeting a specific display headroom. When the content plays, the system interpolates between the two curves closest to the display’s actual headroom and applies the interpolated curve to the input signal. The baseline headroom from the previous section reproduces the system’s default operator, which suits most content. Define custom gain curves when you need precise control over how an image adapts at a given headroom; for example, to shape how highlights compress when a display has less headroom than the content.

Each curve maps an input level to a gain in stops. Input levels are expressed in the extended dynamic range (EDR) domain, where `1.0` corresponds to reference white and higher values represent signal above it. Gain values are non-negative; ColorSync infers whether a curve expands or compresses the dynamic range by comparing the curve’s target headroom to the baseline headroom. The component mix value chooses how the curve derives a single driving signal from the RGB pixel.

```swift
let controlPoints = try GainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints(
    x: [0, 1, 4],
    y: [1, 1, 2],
    slopes: .tangent([0, 0.1, 0.3]))

let alternate = try GainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve(
    headroomStops: 0,
    componentMix: .maxRGB,
    controlPoints: controlPoints)

let adaptiveCurve = try GainCurve.ColorVolumeTransform.ToneMapping.Method.AdaptiveGainCurve(
    chromaticities: .displayP3,
    alternateCurves: [alternate])

let toneMapping = try GainCurve.ColorVolumeTransform.ToneMapping(
    baselineHeadroomStops: 2,
    method: .adaptiveGainCurveMapping(adaptiveCurve))

let curve = try GainCurve(
    colorVolumeTransform: GainCurve.ColorVolumeTransform(adaptiveToneMapping: toneMapping))

let profile = baseProfile.adding(headroomAdaptiveGainCurve: curve)
```

A curve supports up to four alternate curves, each with up to 32 control points. When you supply explicit slopes with [`ColorSyncProfile.HeadroomAdaptiveGainCurve.ColorVolumeTransform.ToneMapping.Method.AlternateCurve.ControlPoints.Slopes.tangent(_:)`](colorsyncprofile/headroomadaptivegaincurve-swift.struct/colorvolumetransform-swift.struct/tonemapping/method-swift.enum/alternatecurve/controlpoints-swift.struct/slopes-swift.enum/tangent(_:).md), provide one slope per control point; choose `.interpolate` to derive them automatically.

The dictionary form nests an `AlternateGainCurveInfo` array under the tone-mapping information:

```objc
NSDictionary *curveInfo = @{
    (__bridge id)kColorSyncAlternateCurveCount: @1,
    (__bridge id)kColorSyncGainCurveChromaticities: @1, // 0=BT.709, 1=Display P3, 2=BT.2020; for custom primaries, pass a `CFArray` of eight floats instead.
    (__bridge id)kColorSyncCommonComponentMixing: @NO,
    (__bridge id)kColorSyncCommonCurveParameters: @NO,
    (__bridge id)kColorSyncAlternateGainCurveInfo: @[@{
        (__bridge id)kColorSyncComponentMix: @0, // 0=MaxRGB, 1=PerComponent, 2=LumaA (weighted luminance), 3=FreeStyle (custom coefficients)
        (__bridge id)kColorSyncAlternateCurveHeadroomStops: @0,
        (__bridge id)kColorSyncMaxControlPointIndex: @2,
        (__bridge id)kColorSyncControlPointsX: @[@0, @1, @4],
        (__bridge id)kColorSyncControlPointsY: @[@1, @1, @2],
        (__bridge id)kColorSyncControlPointSlopes: @[@0, @0.1, @0.3],
        (__bridge id)kColorSyncInterpolateSlopes: @NO,
    }],
};
```

Place `curveInfo` under `kColorSyncHeadroomAdaptiveGainCurveInfo` inside the tone-mapping dictionary, then create the profile copy, as shown in the previous section.

#### Derive a Curve From a Gain Map Image

An HDR image that uses a gain map, as specified in ISO 21496-1, already carries what the system needs to generate a gain curve between full HDR and SDR. When [`Image I/O`](https://developer.apple.com/documentation/ImageIO) decodes such an image to HDR with [`kCGImageSourceDecodeToHDR`](https://developer.apple.com/documentation/ImageIO/kCGImageSourceDecodeToHDR), it derives HAGC metadata and attaches it to the resulting image. Read that metadata back through the image’s color space:

```objc
CGImageSourceRef source = CGImageSourceCreateWithURL(url, NULL);
NSDictionary *opts = @{ (id)kCGImageSourceDecodeToHDR: @YES };
CGImageRef hdrImage = CGImageSourceCreateImageAtIndex(source, 0, (__bridge CFDictionaryRef)opts);

CGColorSpaceRef space = CGImageGetColorSpace(hdrImage); // Get: not owned
CFDataRef iccData = CGColorSpaceCopyICCData(space);
ColorSyncProfileRef profile = ColorSyncProfileCreate(iccData, NULL);
CFRelease(iccData);

CFDictionaryRef dict = ColorSyncProfileCopyHeadroomAdaptiveGainCurveInfoDictionary(profile);

// Release the objects you created when you no longer need them.
CFRelease(hdrImage);
CFRelease(source);
// Release the profile and dictionary after reading the curve.
```

This connects gain-map images to HAGC: take an existing ISO 21496-1 file, let [`Image I/O`](https://developer.apple.com/documentation/ImageIO) produce the metadata, then save the rendition to a non gain-map image format (for example, ISO 22028-5) with an ICC HDR profile, or to an HDR video.

#### Round Trip a Curve Between a Still and a Video

HAGC metadata shares the same binary payload between video (SMPTE ST 2094-50) and images (the ICC HAGC tag), so you can move the metadata you add to a still image directly into a video stream, and move metadata from a video stream into an image. Read the binary from a profile with [`ColorSyncProfileCopyHeadroomAdaptiveGainCurveMetadata`](colorsyncprofilecopyheadroomadaptivegaincurvemetadata.md), and rebuild a profile from binary with [`ColorSyncProfileCreateCopyWithHeadroomAdaptiveGainCurveMetadata`](colorsyncprofilecreatecopywithheadroomadaptivegaincurvemetadata.md):

```objc
// Serialize a profile's curve to the ST 2094-50 binary payload.
CFDataRef metadata = ColorSyncProfileCopyHeadroomAdaptiveGainCurveMetadata(profile);

// Rebuild a profile from a binary payload. Hold the trailing options argument in reserve and pass `NULL`.
ColorSyncProfileRef imported =
    ColorSyncProfileCreateCopyWithHeadroomAdaptiveGainCurveMetadata(base, metadata, NULL);
```

In Swift, read the serialized form from [`headroomAdaptiveGainCurveMetadata`](colorsyncprofile/headroomadaptivegaincurvemetadata.md) and embed it with [`adding(headroomAdaptiveGainCurveMetadata:options:)`](colorsyncprofile/adding(headroomadaptivegaincurvemetadata:options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/authoring-headroom-adaptive-gain-curve-metadata)*