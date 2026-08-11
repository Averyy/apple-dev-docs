# Profile tags and signatures

**Framework**: ColorSync

Identify the four-character signatures that describe an ICC profile’s tags, class, and color space.

#### Overview

An International Color Consortium (ICC) profile is a collection of tags, represented as a four-character signature constant. Use these constants to look up a tag with [`ColorSyncProfileCopyTag(_:_:)`](colorsyncprofilecopytag(_:_:).md), or test for one with [`ColorSyncProfileContainsTag(_:_:)`](colorsyncprofilecontainstag(_:_:).md), and to interpret a profile’s class and color space.

## Topics

### Identifying profile classes
- [var kColorSyncSigAbstractClass: Unmanaged<CFString>!](kcolorsyncsigabstractclass.md)
  The signature identifying an abstract profile class.
- [var kColorSyncSigColorSpaceClass: Unmanaged<CFString>!](kcolorsyncsigcolorspaceclass.md)
  The signature identifying a color-space conversion profile class.
- [var kColorSyncSigDisplayClass: Unmanaged<CFString>!](kcolorsyncsigdisplayclass.md)
  The signature identifying a display device profile class.
- [var kColorSyncSigInputClass: Unmanaged<CFString>!](kcolorsyncsiginputclass.md)
  The signature identifying an input (scanner or camera) device profile class.
- [var kColorSyncSigLinkClass: Unmanaged<CFString>!](kcolorsyncsiglinkclass.md)
  The signature identifying a device-link profile class.
- [var kColorSyncSigNamedColorClass: Unmanaged<CFString>!](kcolorsyncsignamedcolorclass.md)
  The signature identifying a named color profile class.
- [var kColorSyncSigOutputClass: Unmanaged<CFString>!](kcolorsyncsigoutputclass.md)
  The signature identifying an output (printer) device profile class.
### Identifying color spaces
- [var kColorSyncSigCmykData: Unmanaged<CFString>!](kcolorsyncsigcmykdata.md)
  The signature identifying the CMYK data color space.
- [var kColorSyncSigGrayData: Unmanaged<CFString>!](kcolorsyncsiggraydata.md)
  The signature identifying the grayscale data color space.
- [var kColorSyncSigLabData: Unmanaged<CFString>!](kcolorsyncsiglabdata.md)
  The signature identifying the CIELAB data color space.
- [var kColorSyncSigRgbData: Unmanaged<CFString>!](kcolorsyncsigrgbdata.md)
  The signature identifying the RGB data color space.
- [var kColorSyncSigXYZData: Unmanaged<CFString>!](kcolorsyncsigxyzdata.md)
  The signature identifying the CIEXYZ data color space.
### Identifying transform tags
- [var kColorSyncSigAToB0Tag: Unmanaged<CFString>!](kcolorsyncsigatob0tag.md)
  The signature of the device-to-PCS transform tag for the perceptual rendering intent.
- [var kColorSyncSigAToB1Tag: Unmanaged<CFString>!](kcolorsyncsigatob1tag.md)
  The signature of the device-to-PCS transform tag for the media-relative colorimetric rendering intent.
- [var kColorSyncSigAToB2Tag: Unmanaged<CFString>!](kcolorsyncsigatob2tag.md)
  The signature of the device-to-PCS transform tag for the saturation rendering intent.
- [var kColorSyncSigBToA0Tag: Unmanaged<CFString>!](kcolorsyncsigbtoa0tag.md)
  The signature of the PCS-to-device transform tag for the perceptual rendering intent.
- [var kColorSyncSigBToA1Tag: Unmanaged<CFString>!](kcolorsyncsigbtoa1tag.md)
  The signature of the PCS-to-device transform tag for the media-relative colorimetric rendering intent.
- [var kColorSyncSigBToA2Tag: Unmanaged<CFString>!](kcolorsyncsigbtoa2tag.md)
  The signature of the PCS-to-device transform tag for the saturation rendering intent.
### Identifying colorant and curve tags
- [var kColorSyncSigRedColorantTag: Unmanaged<CFString>!](kcolorsyncsigredcoloranttag.md)
  The signature of the red colorant tag, giving the red channel’s PCSXYZ values.
- [var kColorSyncSigGreenColorantTag: Unmanaged<CFString>!](kcolorsyncsiggreencoloranttag.md)
  The signature of the green colorant tag, giving the green channel’s PCSXYZ values.
- [var kColorSyncSigBlueColorantTag: Unmanaged<CFString>!](kcolorsyncsigbluecoloranttag.md)
  The signature of the blue colorant tag, giving the blue channel’s PCSXYZ values.
- [var kColorSyncSigRedTRCTag: Unmanaged<CFString>!](kcolorsyncsigredtrctag.md)
  The signature of the red channel’s tone reproduction curve (TRC) tag.
- [var kColorSyncSigGreenTRCTag: Unmanaged<CFString>!](kcolorsyncsiggreentrctag.md)
  The signature of the green channel’s tone reproduction curve (TRC) tag.
- [var kColorSyncSigBlueTRCTag: Unmanaged<CFString>!](kcolorsyncsigbluetrctag.md)
  The signature of the blue channel’s tone reproduction curve (TRC) tag.
- [var kColorSyncSigGrayTRCTag: Unmanaged<CFString>!](kcolorsyncsiggraytrctag.md)
  The signature of the grayscale tone reproduction curve (TRC) tag.
### Identifying white and black points
- [var kColorSyncSigMediaBlackPointTag: Unmanaged<CFString>!](kcolorsyncsigmediablackpointtag.md)
  The signature of the media black point tag.
- [var kColorSyncSigMediaWhitePointTag: Unmanaged<CFString>!](kcolorsyncsigmediawhitepointtag.md)
  The signature of the media white point tag.
### Identifying preview tags
- [var kColorSyncSigPreview0Tag: Unmanaged<CFString>!](kcolorsyncsigpreview0tag.md)
  The signature of the preview tag for the perceptual rendering intent.
- [var kColorSyncSigPreview1Tag: Unmanaged<CFString>!](kcolorsyncsigpreview1tag.md)
  The signature of the preview tag for the media-relative colorimetric rendering intent.
- [var kColorSyncSigPreview2Tag: Unmanaged<CFString>!](kcolorsyncsigpreview2tag.md)
  The signature of the preview tag for the saturation rendering intent.
### Identifying metadata tags
- [var kColorSyncSigCopyrightTag: Unmanaged<CFString>!](kcolorsyncsigcopyrighttag.md)
  The signature of the profile copyright tag.
- [var kColorSyncSigDeviceMfgDescTag: Unmanaged<CFString>!](kcolorsyncsigdevicemfgdesctag.md)
  The signature of the device manufacturer description tag.
- [var kColorSyncSigDeviceModelDescTag: Unmanaged<CFString>!](kcolorsyncsigdevicemodeldesctag.md)
  The signature of the device model description tag.
- [var kColorSyncSigGamutTag: Unmanaged<CFString>!](kcolorsyncsiggamuttag.md)
  The signature of the gamut tag, marking which PCS colors fall outside the device gamut.
- [var kColorSyncSigNamedColor2Tag: Unmanaged<CFString>!](kcolorsyncsignamedcolor2tag.md)
  The signature of the named color (version 2) tag.
- [var kColorSyncSigProfileDescriptionTag: Unmanaged<CFString>!](kcolorsyncsigprofiledescriptiontag.md)
  The signature of the profile description tag.
- [var kColorSyncSigProfileSequenceDescTag: Unmanaged<CFString>!](kcolorsyncsigprofilesequencedesctag.md)
  The signature of the profile sequence description tag.
- [var kColorSyncSigTechnologyTag: Unmanaged<CFString>!](kcolorsyncsigtechnologytag.md)
  The signature of the technology tag, identifying the device technology.
- [var kColorSyncSigViewingCondDescTag: Unmanaged<CFString>!](kcolorsyncsigviewingconddesctag.md)
  The signature of the viewing conditions description tag.
- [var kColorSyncSigViewingConditionsTag: Unmanaged<CFString>!](kcolorsyncsigviewingconditionstag.md)
  The signature of the viewing conditions tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/profile-tags-and-signatures)*