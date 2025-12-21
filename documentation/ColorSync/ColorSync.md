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
- [var kColorSyncDoNotSubstituteProfiles: Unmanaged<CFString>!](kcolorsyncdonotsubstituteprofiles.md)
- [var kColorSyncTransformUseITU709OETF: Unmanaged<CFString>!](kcolorsynctransformuseitu709oetf.md)
### Functions
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