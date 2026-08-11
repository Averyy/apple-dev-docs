# Color transforms

**Framework**: ColorSync

Convert color from one profile’s color space to another.

#### Overview

A [`ColorSyncTransform`](colorsynctransform.md) precomputes the conversion between a sequence of profiles. Color conversion requires significant computation, so the way you apply a transform affects performance. To convert pixels directly, call [`ColorSyncTransformConvert(_:_:_:_:_:_:_:_:_:_:_:_:)`](colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:).md). For production code or large buffers, get better performance by extracting a ColorSync *code fragment* with [`ColorSyncCreateCodeFragment(_:_:)`](colorsynccreatecodefragment(_:_:).md) and running it through [`vImage`](https://developer.apple.com/documentation/Accelerate/vImage). Describe the layout of your pixel buffers with the pixel-format constants in [`Pixel format and data layout`](pixel-format.md).

## Topics

### Representing transforms
- [class ColorSyncTransform](colorsynctransform.md)
  A reference to a color transform that converts color data between profiles.
### Creating and applying a transform
- [func ColorSyncTransformCreate(CFArray?, CFDictionary?) -> Unmanaged<ColorSyncTransform>?](colorsynctransformcreate(_:_:).md)
  Creates a color transform from a sequence of profiles.
- [func ColorSyncTransformConvert(ColorSyncTransform!, Int, Int, UnsafeMutableRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, UnsafeRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool](colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Converts color data from a source layout to a destination layout using a color transform.
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](colorsynctransformgetprofilesequence(_:).md)
  Returns the profile sequence used to create a color transform.
- [func ColorSyncTransformCopyProperty(ColorSyncTransform!, CFTypeRef!, CFDictionary?) -> Unmanaged<CFTypeRef>?](colorsynctransformcopyproperty(_:_:_:).md)
  Copies a property from a color transform.
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](colorsynctransformsetproperty(_:_:_:).md)
  Sets a property on a color transform.
- [func ColorSyncTransformGetTypeID() -> CFTypeID](colorsynctransformgettypeid().md)
  Returns the type identifier for the `ColorSyncTransform` opaque type.
### Choosing rendering intents
- [var kColorSyncRenderingIntent: Unmanaged<CFString>!](kcolorsyncrenderingintent.md)
  A key for the rendering intent to use for the profile in a profile-sequence dictionary.
- [var kColorSyncRenderingIntentPerceptual: Unmanaged<CFString>!](kcolorsyncrenderingintentperceptual.md)
  A [`kColorSyncRenderingIntent`](kcolorsyncrenderingintent.md) value selecting the perceptual rendering intent.
- [var kColorSyncRenderingIntentRelative: Unmanaged<CFString>!](kcolorsyncrenderingintentrelative.md)
  A [`kColorSyncRenderingIntent`](kcolorsyncrenderingintent.md) value selecting the media-relative colorimetric rendering intent.
- [var kColorSyncRenderingIntentSaturation: Unmanaged<CFString>!](kcolorsyncrenderingintentsaturation.md)
  A [`kColorSyncRenderingIntent`](kcolorsyncrenderingintent.md) value selecting the saturation rendering intent.
- [var kColorSyncRenderingIntentAbsolute: Unmanaged<CFString>!](kcolorsyncrenderingintentabsolute.md)
  A [`kColorSyncRenderingIntent`](kcolorsyncrenderingintent.md) value selecting the ICC-absolute colorimetric rendering intent.
- [var kColorSyncRenderingIntentUseProfileHeader: Unmanaged<CFString>!](kcolorsyncrenderingintentuseprofileheader.md)
  A [`kColorSyncRenderingIntent`](kcolorsyncrenderingintent.md) value selecting the rendering intent stored in the profile header.
### Proofing and gamut checking
- [func ColorSyncProfileCreateLink(CFArray!, CFDictionary?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatelink(_:_:).md)
  Creates a device link profile from an array of profiles.
- [var kColorSyncTransformDeviceToDevice: Unmanaged<CFString>!](kcolorsynctransformdevicetodevice.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value selecting the device-to-device conversion direction.
- [var kColorSyncTransformGamutCheck: Unmanaged<CFString>!](kcolorsynctransformgamutcheck.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value that checks whether colors fall outside the destination gamut.
### Accessing transform properties
- [var kColorSyncProfile: Unmanaged<CFString>!](kcolorsyncprofile.md)
  A key for the profile object in a profile-sequence dictionary passed to [`ColorSyncTransformCreate(_:_:)`](colorsynctransformcreate(_:_:).md).
- [var kColorSyncTransformCreator: Unmanaged<CFString>!](kcolorsynctransformcreator.md)
  A key for the name of the CMM that created the transform.
- [var kColorSyncTransformDeviceToPCS: Unmanaged<CFString>!](kcolorsynctransformdevicetopcs.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value selecting the device-to-PCS conversion direction.
- [var kColorSyncTransformDstSpace: Unmanaged<CFString>!](kcolorsynctransformdstspace.md)
  A key for the transform’s destination color space.
- [var kColorSyncTransformInfo: Unmanaged<CFString>!](kcolorsynctransforminfo.md)
  A key for a dictionary of information about the transform.
- [var kColorSyncTransformPCSToDevice: Unmanaged<CFString>!](kcolorsynctransformpcstodevice.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value selecting the PCS-to-device conversion direction.
- [var kColorSyncTransformPCSToPCS: Unmanaged<CFString>!](kcolorsynctransformpcstopcs.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value selecting the PCS-to-PCS conversion direction.
- [var kColorSyncTransformProfileSequnce: Unmanaged<CFString>!](kcolorsynctransformprofilesequnce.md)
  A key for the profile sequence used to create the transform.
- [var kColorSyncTransformSrcSpace: Unmanaged<CFString>!](kcolorsynctransformsrcspace.md)
  A key for the transform’s source color space.
- [var kColorSyncTransformTag: Unmanaged<CFString>!](kcolorsynctransformtag.md)
  A key for the tag identifying which tags of the profile to use in a profile-sequence dictionary.
### Extracting a conversion for vImage
- [func ColorSyncCreateCodeFragment(CFArray!, CFDictionary!) -> Unmanaged<CFTypeRef>!](colorsynccreatecodefragment(_:_:).md)
  Creates a code fragment from a sequence of profiles.
- [var kColorSyncTransformCodeFragmentType: Unmanaged<CFString>!](kcolorsynctransformcodefragmenttype.md)
  A key for the type of code fragment to create, or that the framework created.
- [var kColorSyncTransformCodeFragmentMD5: Unmanaged<CFString>!](kcolorsynctransformcodefragmentmd5.md)
  A key for the MD5 checksum of the code fragment.
### Reading conversion data sets
- [var kColorSyncTransformFullConversionData: Unmanaged<CFString>!](kcolorsynctransformfullconversiondata.md)
  A key for the full-conversion code fragment, containing all non-`NULL` components from the profile sequence.
- [var kColorSyncTransformParametricConversionData: Unmanaged<CFString>!](kcolorsynctransformparametricconversiondata.md)
  A key for the parametric code fragment, consisting only of parametric curves, matrices, and BPC components.
- [var kColorSyncTransformSimplifiedConversionData: Unmanaged<CFString>!](kcolorsynctransformsimplifiedconversiondata.md)
  A key for the simplified code fragment, collapsing the full conversion into one multi-dimensional table.
- [var kColorSyncConversionBPC: Unmanaged<CFString>!](kcolorsyncconversionbpc.md)
  A key for a black point compensation component, represented as a `CFArray` of `Float32` `CFNumber`s.
- [var kColorSyncFixedPointRange: Unmanaged<CFString>!](kcolorsyncfixedpointrange.md)
  A key for the fixed-point range of the conversion data.
### Reading curves and matrices
- [var kColorSyncConversionParamCurve0: Unmanaged<CFString>!](kcolorsyncconversionparamcurve0.md)
  A key for a parametric tone rendering curve of type 0, represented as a `CFArray` of seven `Float32` `CFNumber`s.
- [var kColorSyncConversionParamCurve1: Unmanaged<CFString>!](kcolorsyncconversionparamcurve1.md)
  A key for a parametric tone rendering curve of type 1, represented as a `CFArray` of seven `Float32` `CFNumber`s.
- [var kColorSyncConversionParamCurve2: Unmanaged<CFString>!](kcolorsyncconversionparamcurve2.md)
  A key for a parametric tone rendering curve of type 2, represented as a `CFArray` of seven `Float32` `CFNumber`s.
- [var kColorSyncConversionParamCurve3: Unmanaged<CFString>!](kcolorsyncconversionparamcurve3.md)
  A key for a parametric tone rendering curve of type 3, represented as a `CFArray` of seven `Float32` `CFNumber`s.
- [var kColorSyncConversionParamCurve4: Unmanaged<CFString>!](kcolorsyncconversionparamcurve4.md)
  A key for a parametric tone rendering curve of type 4, represented as a `CFArray` of seven `Float32` `CFNumber`s.
- [var kColorSyncConversionMatrix: Unmanaged<CFString>!](kcolorsyncconversionmatrix.md)
  A key for a conversion matrix component, represented as a `CFArray` of three `CFArray`s of four `Float32` `CFNumber`s.
### Reading lookup tables
- [var kColorSyncConversion1DLut: Unmanaged<CFString>!](kcolorsyncconversion1dlut.md)
  A key for a one-dimensional lookup table with interpolation, represented as `CFData` containing a `Float32` table.
- [var kColorSyncConversion3DLut: Unmanaged<CFString>!](kcolorsyncconversion3dlut.md)
  A key for a three-dimensional lookup table with interpolation, represented as `CFData`.
- [var kColorSyncConversionNDLut: Unmanaged<CFString>!](kcolorsyncconversionndlut.md)
  A key for a multi-dimensional lookup table with interpolation, represented as `CFData` for N inputs and M outputs.
- [var kColorSyncConversionGridPoints: Unmanaged<CFString>!](kcolorsyncconversiongridpoints.md)
  A key for the number of grid points in a lookup table.
- [var kColorSyncConversionChannelID: Unmanaged<CFString>!](kcolorsyncconversionchannelid.md)
  A key for the identifier of the channel a conversion component applies to.
- [var kColorSyncConversionInpChan: Unmanaged<CFString>!](kcolorsyncconversioninpchan.md)
  A key for the number of input channels of a lookup table.
- [var kColorSyncConversionOutChan: Unmanaged<CFString>!](kcolorsyncconversionoutchan.md)
  A key for the number of output channels of a lookup table.
### Setting conversion quality
- [var kColorSyncBestQuality: Unmanaged<CFString>!](kcolorsyncbestquality.md)
  A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that does not coalesce profile transforms; the default.
- [var kColorSyncBlackPointCompensation: Unmanaged<CFString>!](kcolorsyncblackpointcompensation.md)
  A key whose `CFBooleanRef` value enables or disables black point compensation.
- [var kColorSyncConvertQuality: Unmanaged<CFString>!](kcolorsyncconvertquality.md)
  A key for the quality of the conversion performed by the transform.
- [var kColorSyncDraftQuality: Unmanaged<CFString>!](kcolorsyncdraftquality.md)
  A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that coalesces all transforms and does not interpolate.
- [var kColorSyncNormalQuality: Unmanaged<CFString>!](kcolorsyncnormalquality.md)
  A [`kColorSyncConvertQuality`](kcolorsyncconvertquality.md) value that coalesces all transforms.
### Handling HDR and extended range
- [var kColorSyncExtendedRange: Unmanaged<CFString>!](kcolorsyncextendedrange.md)
  A key whose `CFBooleanRef` value enables or disables extended range.
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
### Choosing a color management module
- [var kColorSyncPreferredCMM: Unmanaged<CFString>!](kcolorsyncpreferredcmm.md)
  A key whose value is the [`ColorSyncCMM`](colorsynccmm.md) of the preferred CMM.

## See Also

- [Pixel format and data layout](pixel-format.md)
  Describe the memory layout of the pixel buffers a color transform reads and writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/color-transforms)*