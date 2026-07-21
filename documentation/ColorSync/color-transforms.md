# Color transforms

**Framework**: ColorSync

Convert color from one profile’s color space to another.

#### Overview

A [`ColorSyncTransform`](colorsynctransform.md) precomputes the conversion between a sequence of profiles. Color conversion requires significant computation, so the way you apply a transform affects performance. To convert pixels directly, call [`ColorSyncTransformConvert(_:_:_:_:_:_:_:_:_:_:_:_:)`](colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:).md). For production code or large buffers, get better performance by extracting a ColorSync *code fragment* with [`ColorSyncCreateCodeFragment(_:_:)`](colorsynccreatecodefragment(_:_:).md) and running it through [`vImage`](https://developer.apple.com/documentation/Accelerate/vImage). Describe the layout of your pixel buffers with the pixel-format constants in [`Pixel format and data layout`](pixel-format.md).

## Topics

### Representing transforms
- [class ColorSyncTransform](colorsynctransform.md)
### Creating and applying a transform
- [func ColorSyncTransformCreate(CFArray?, CFDictionary?) -> Unmanaged<ColorSyncTransform>?](colorsynctransformcreate(_:_:).md)
- [func ColorSyncTransformConvert(ColorSyncTransform!, Int, Int, UnsafeMutableRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, UnsafeRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool](colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](colorsynctransformgetprofilesequence(_:).md)
- [func ColorSyncTransformCopyProperty(ColorSyncTransform!, CFTypeRef!, CFDictionary?) -> Unmanaged<CFTypeRef>?](colorsynctransformcopyproperty(_:_:_:).md)
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](colorsynctransformsetproperty(_:_:_:).md)
- [func ColorSyncTransformGetTypeID() -> CFTypeID](colorsynctransformgettypeid().md)
### Choosing rendering intents
- [var kColorSyncRenderingIntent: Unmanaged<CFString>!](kcolorsyncrenderingintent.md)
- [var kColorSyncRenderingIntentPerceptual: Unmanaged<CFString>!](kcolorsyncrenderingintentperceptual.md)
- [var kColorSyncRenderingIntentRelative: Unmanaged<CFString>!](kcolorsyncrenderingintentrelative.md)
- [var kColorSyncRenderingIntentSaturation: Unmanaged<CFString>!](kcolorsyncrenderingintentsaturation.md)
- [var kColorSyncRenderingIntentAbsolute: Unmanaged<CFString>!](kcolorsyncrenderingintentabsolute.md)
- [var kColorSyncRenderingIntentUseProfileHeader: Unmanaged<CFString>!](kcolorsyncrenderingintentuseprofileheader.md)
### Proofing and gamut checking
- [func ColorSyncProfileCreateLink(CFArray!, CFDictionary?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatelink(_:_:).md)
- [var kColorSyncTransformDeviceToDevice: Unmanaged<CFString>!](kcolorsynctransformdevicetodevice.md)
- [var kColorSyncTransformGamutCheck: Unmanaged<CFString>!](kcolorsynctransformgamutcheck.md)
### Accessing transform properties
- [var kColorSyncProfile: Unmanaged<CFString>!](kcolorsyncprofile.md)
- [var kColorSyncTransformCreator: Unmanaged<CFString>!](kcolorsynctransformcreator.md)
- [var kColorSyncTransformDeviceToPCS: Unmanaged<CFString>!](kcolorsynctransformdevicetopcs.md)
- [var kColorSyncTransformDstSpace: Unmanaged<CFString>!](kcolorsynctransformdstspace.md)
- [var kColorSyncTransformInfo: Unmanaged<CFString>!](kcolorsynctransforminfo.md)
- [var kColorSyncTransformPCSToDevice: Unmanaged<CFString>!](kcolorsynctransformpcstodevice.md)
- [var kColorSyncTransformPCSToPCS: Unmanaged<CFString>!](kcolorsynctransformpcstopcs.md)
- [var kColorSyncTransformProfileSequnce: Unmanaged<CFString>!](kcolorsynctransformprofilesequnce.md)
- [var kColorSyncTransformSrcSpace: Unmanaged<CFString>!](kcolorsynctransformsrcspace.md)
- [var kColorSyncTransformTag: Unmanaged<CFString>!](kcolorsynctransformtag.md)
### Extracting a conversion for vImage
- [func ColorSyncCreateCodeFragment(CFArray!, CFDictionary!) -> Unmanaged<CFTypeRef>!](colorsynccreatecodefragment(_:_:).md)
- [var kColorSyncTransformCodeFragmentType: Unmanaged<CFString>!](kcolorsynctransformcodefragmenttype.md)
- [var kColorSyncTransformCodeFragmentMD5: Unmanaged<CFString>!](kcolorsynctransformcodefragmentmd5.md)
### Reading conversion data sets
- [var kColorSyncTransformFullConversionData: Unmanaged<CFString>!](kcolorsynctransformfullconversiondata.md)
- [var kColorSyncTransformParametricConversionData: Unmanaged<CFString>!](kcolorsynctransformparametricconversiondata.md)
- [var kColorSyncTransformSimplifiedConversionData: Unmanaged<CFString>!](kcolorsynctransformsimplifiedconversiondata.md)
- [var kColorSyncConversionBPC: Unmanaged<CFString>!](kcolorsyncconversionbpc.md)
- [var kColorSyncFixedPointRange: Unmanaged<CFString>!](kcolorsyncfixedpointrange.md)
### Reading curves and matrices
- [var kColorSyncConversionParamCurve0: Unmanaged<CFString>!](kcolorsyncconversionparamcurve0.md)
- [var kColorSyncConversionParamCurve1: Unmanaged<CFString>!](kcolorsyncconversionparamcurve1.md)
- [var kColorSyncConversionParamCurve2: Unmanaged<CFString>!](kcolorsyncconversionparamcurve2.md)
- [var kColorSyncConversionParamCurve3: Unmanaged<CFString>!](kcolorsyncconversionparamcurve3.md)
- [var kColorSyncConversionParamCurve4: Unmanaged<CFString>!](kcolorsyncconversionparamcurve4.md)
- [var kColorSyncConversionMatrix: Unmanaged<CFString>!](kcolorsyncconversionmatrix.md)
### Reading lookup tables
- [var kColorSyncConversion1DLut: Unmanaged<CFString>!](kcolorsyncconversion1dlut.md)
- [var kColorSyncConversion3DLut: Unmanaged<CFString>!](kcolorsyncconversion3dlut.md)
- [var kColorSyncConversionNDLut: Unmanaged<CFString>!](kcolorsyncconversionndlut.md)
- [var kColorSyncConversionGridPoints: Unmanaged<CFString>!](kcolorsyncconversiongridpoints.md)
- [var kColorSyncConversionChannelID: Unmanaged<CFString>!](kcolorsyncconversionchannelid.md)
- [var kColorSyncConversionInpChan: Unmanaged<CFString>!](kcolorsyncconversioninpchan.md)
- [var kColorSyncConversionOutChan: Unmanaged<CFString>!](kcolorsyncconversionoutchan.md)
### Setting conversion quality
- [var kColorSyncBestQuality: Unmanaged<CFString>!](kcolorsyncbestquality.md)
- [var kColorSyncBlackPointCompensation: Unmanaged<CFString>!](kcolorsyncblackpointcompensation.md)
- [var kColorSyncConvertQuality: Unmanaged<CFString>!](kcolorsyncconvertquality.md)
- [var kColorSyncDraftQuality: Unmanaged<CFString>!](kcolorsyncdraftquality.md)
- [var kColorSyncNormalQuality: Unmanaged<CFString>!](kcolorsyncnormalquality.md)
### Handling HDR and extended range
- [var kColorSyncExtendedRange: Unmanaged<CFString>!](kcolorsyncextendedrange.md)
- [var kColorSyncConvertUseExtendedRange: Unmanaged<CFString>!](kcolorsyncconvertuseextendedrange.md)
- [var kColorSyncTransformUseITU709OETF: Unmanaged<CFString>!](kcolorsynctransformuseitu709oetf.md)
- [var kColorSyncHDRDerivative: Unmanaged<CFString>!](kcolorsynchdrderivative.md)
- [var kColorSyncPQDerivative: Unmanaged<CFString>!](kcolorsyncpqderivative.md)
- [var kColorSyncHLGDerivative: Unmanaged<CFString>!](kcolorsynchlgderivative.md)
### Choosing a color management module
- [var kColorSyncPreferredCMM: Unmanaged<CFString>!](kcolorsyncpreferredcmm.md)

## See Also

- [Pixel format and data layout](pixel-format.md)
  Describe the memory layout of the pixel buffers a color transform reads and writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/color-transforms)*