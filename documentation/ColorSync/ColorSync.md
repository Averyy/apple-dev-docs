# ColorSync

**Framework**: ColorSync  
**Kind**: module

Reproduce colors accurately across a range of input, output, and display devices.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Topics

### Reference
- [ColorSync Constants](colorsync-constants.md)
- [ColorSync Functions](colorsync-functions.md)
### Classes
- [class ColorSyncCMM](colorsynccmm.md)
- [class ColorSyncMutableProfile](colorsyncmutableprofile.md)
- [class ColorSyncProfile](colorsyncprofile.md)
- [class ColorSyncTransform](colorsynctransform.md)
### Structures
- [struct ColorSyncAlphaInfo](colorsyncalphainfo.md)
- [struct ColorSyncDataDepth](colorsyncdatadepth.md)
- [struct ColorSyncMD5](colorsyncmd5.md)
### Variables
- [var icVersion4Point4Number: Int](icversion4point4number.md)
- [var kColorSyncAlphaNone: ColorSyncAlphaInfo](kcolorsyncalphanone.md)
- [var kColorSyncAlternateCurveCount: Unmanaged<CFString>](kcolorsyncalternatecurvecount.md)
- [var kColorSyncAlternateCurveHeadroomStops: Unmanaged<CFString>](kcolorsyncalternatecurveheadroomstops.md)
- [var kColorSyncAlternateGainCurveInfo: Unmanaged<CFString>](kcolorsyncalternategaincurveinfo.md)
- [var kColorSyncBaselineHeadroomStops: Unmanaged<CFString>](kcolorsyncbaselineheadroomstops.md)
- [var kColorSyncCoefficientBlue: Unmanaged<CFString>](kcolorsynccoefficientblue.md)
- [var kColorSyncCoefficientComponent: Unmanaged<CFString>](kcolorsynccoefficientcomponent.md)
- [var kColorSyncCoefficientGreen: Unmanaged<CFString>](kcolorsynccoefficientgreen.md)
- [var kColorSyncCoefficientMaxRGB: Unmanaged<CFString>](kcolorsynccoefficientmaxrgb.md)
- [var kColorSyncCoefficientMinRGB: Unmanaged<CFString>](kcolorsynccoefficientminrgb.md)
- [var kColorSyncCoefficientRed: Unmanaged<CFString>](kcolorsynccoefficientred.md)
- [var kColorSyncCommonComponentMixing: Unmanaged<CFString>](kcolorsynccommoncomponentmixing.md)
- [var kColorSyncCommonCurveParameters: Unmanaged<CFString>](kcolorsynccommoncurveparameters.md)
- [var kColorSyncComponentCoefficients: Unmanaged<CFString>](kcolorsynccomponentcoefficients.md)
- [var kColorSyncComponentMix: Unmanaged<CFString>](kcolorsynccomponentmix.md)
- [var kColorSyncControlPointSlopes: Unmanaged<CFString>](kcolorsynccontrolpointslopes.md)
- [var kColorSyncControlPointsX: Unmanaged<CFString>](kcolorsynccontrolpointsx.md)
- [var kColorSyncControlPointsY: Unmanaged<CFString>](kcolorsynccontrolpointsy.md)
- [var kColorSyncCustomHDRReferenceWhite: Unmanaged<CFString>](kcolorsynccustomhdrreferencewhite.md)
- [var kColorSyncDoNotSubstituteProfiles: Unmanaged<CFString>!](kcolorsyncdonotsubstituteprofiles.md)
- [var kColorSyncGainCurveChromaticities: Unmanaged<CFString>](kcolorsyncgaincurvechromaticities.md)
- [var kColorSyncHeadroomAdaptiveGainCurveApplicationVersion: Unmanaged<CFString>](kcolorsyncheadroomadaptivegaincurveapplicationversion.md)
- [var kColorSyncHeadroomAdaptiveGainCurveColorVolumeTransform: Unmanaged<CFString>](kcolorsyncheadroomadaptivegaincurvecolorvolumetransform.md)
- [var kColorSyncHeadroomAdaptiveGainCurveInfo: Unmanaged<CFString>](kcolorsyncheadroomadaptivegaincurveinfo.md)
- [var kColorSyncHeadroomAdaptiveToneMappingInfo: Unmanaged<CFString>](kcolorsyncheadroomadaptivetonemappinginfo.md)
- [var kColorSyncInterpolateSlopes: Unmanaged<CFString>](kcolorsyncinterpolateslopes.md)
- [var kColorSyncMaxControlPointIndex: Unmanaged<CFString>](kcolorsyncmaxcontrolpointindex.md)
- [var kColorSyncTransformUseITU709OETF: Unmanaged<CFString>!](kcolorsynctransformuseitu709oetf.md)
### Functions
- [func ColorSyncProfileContainsHeadroomAdaptiveGainCurve(ColorSyncProfile) -> Bool](colorsyncprofilecontainsheadroomadaptivegaincurve(_:).md)
- [func ColorSyncProfileCreateWithURLAndOptions(CFURL!, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurlandoptions(_:_:_:).md)
### Type Aliases
- [typealias CMMApplyTransformProc](cmmapplytransformproc.md)
- [typealias CMMCreateTransformPropertyProc](cmmcreatetransformpropertyproc.md)
- [typealias CMMInitializeLinkProfileProc](cmminitializelinkprofileproc.md)
- [typealias CMMInitializeTransformProc](cmminitializetransformproc.md)
- [typealias ColorSyncCMMIterateCallback](colorsynccmmiteratecallback.md)
- [typealias ColorSyncDataLayout](colorsyncdatalayout.md)
- [typealias ColorSyncDeviceProfileIterateCallback](colorsyncdeviceprofileiteratecallback.md)
- [typealias ColorSyncProfileIterateCallback](colorsyncprofileiteratecallback.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ColorSync)*