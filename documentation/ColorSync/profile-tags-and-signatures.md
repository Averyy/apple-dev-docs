# Profile tags and signatures

**Framework**: ColorSync

Identify the four-character signatures that describe an ICC profile’s tags, class, and color space.

#### Overview

An International Color Consortium (ICC) profile is a collection of tags, represented as a four-character signature constant. Use these constants to look up a tag with [`ColorSyncProfileCopyTag(_:_:)`](colorsyncprofilecopytag(_:_:).md), or test for one with [`ColorSyncProfileContainsTag(_:_:)`](colorsyncprofilecontainstag(_:_:).md), and to interpret a profile’s class and color space.

## Topics

### Identifying profile classes
- [var kColorSyncSigAbstractClass: Unmanaged<CFString>!](kcolorsyncsigabstractclass.md)
- [var kColorSyncSigColorSpaceClass: Unmanaged<CFString>!](kcolorsyncsigcolorspaceclass.md)
- [var kColorSyncSigDisplayClass: Unmanaged<CFString>!](kcolorsyncsigdisplayclass.md)
- [var kColorSyncSigInputClass: Unmanaged<CFString>!](kcolorsyncsiginputclass.md)
- [var kColorSyncSigLinkClass: Unmanaged<CFString>!](kcolorsyncsiglinkclass.md)
- [var kColorSyncSigNamedColorClass: Unmanaged<CFString>!](kcolorsyncsignamedcolorclass.md)
- [var kColorSyncSigOutputClass: Unmanaged<CFString>!](kcolorsyncsigoutputclass.md)
### Identifying color spaces
- [var kColorSyncSigCmykData: Unmanaged<CFString>!](kcolorsyncsigcmykdata.md)
- [var kColorSyncSigGrayData: Unmanaged<CFString>!](kcolorsyncsiggraydata.md)
- [var kColorSyncSigLabData: Unmanaged<CFString>!](kcolorsyncsiglabdata.md)
- [var kColorSyncSigRgbData: Unmanaged<CFString>!](kcolorsyncsigrgbdata.md)
- [var kColorSyncSigXYZData: Unmanaged<CFString>!](kcolorsyncsigxyzdata.md)
### Identifying transform tags
- [var kColorSyncSigAToB0Tag: Unmanaged<CFString>!](kcolorsyncsigatob0tag.md)
- [var kColorSyncSigAToB1Tag: Unmanaged<CFString>!](kcolorsyncsigatob1tag.md)
- [var kColorSyncSigAToB2Tag: Unmanaged<CFString>!](kcolorsyncsigatob2tag.md)
- [var kColorSyncSigBToA0Tag: Unmanaged<CFString>!](kcolorsyncsigbtoa0tag.md)
- [var kColorSyncSigBToA1Tag: Unmanaged<CFString>!](kcolorsyncsigbtoa1tag.md)
- [var kColorSyncSigBToA2Tag: Unmanaged<CFString>!](kcolorsyncsigbtoa2tag.md)
### Identifying colorant and curve tags
- [var kColorSyncSigRedColorantTag: Unmanaged<CFString>!](kcolorsyncsigredcoloranttag.md)
- [var kColorSyncSigGreenColorantTag: Unmanaged<CFString>!](kcolorsyncsiggreencoloranttag.md)
- [var kColorSyncSigBlueColorantTag: Unmanaged<CFString>!](kcolorsyncsigbluecoloranttag.md)
- [var kColorSyncSigRedTRCTag: Unmanaged<CFString>!](kcolorsyncsigredtrctag.md)
- [var kColorSyncSigGreenTRCTag: Unmanaged<CFString>!](kcolorsyncsiggreentrctag.md)
- [var kColorSyncSigBlueTRCTag: Unmanaged<CFString>!](kcolorsyncsigbluetrctag.md)
- [var kColorSyncSigGrayTRCTag: Unmanaged<CFString>!](kcolorsyncsiggraytrctag.md)
### Identifying white and black points
- [var kColorSyncSigMediaBlackPointTag: Unmanaged<CFString>!](kcolorsyncsigmediablackpointtag.md)
- [var kColorSyncSigMediaWhitePointTag: Unmanaged<CFString>!](kcolorsyncsigmediawhitepointtag.md)
### Identifying preview tags
- [var kColorSyncSigPreview0Tag: Unmanaged<CFString>!](kcolorsyncsigpreview0tag.md)
- [var kColorSyncSigPreview1Tag: Unmanaged<CFString>!](kcolorsyncsigpreview1tag.md)
- [var kColorSyncSigPreview2Tag: Unmanaged<CFString>!](kcolorsyncsigpreview2tag.md)
### Identifying metadata tags
- [var kColorSyncSigCopyrightTag: Unmanaged<CFString>!](kcolorsyncsigcopyrighttag.md)
- [var kColorSyncSigDeviceMfgDescTag: Unmanaged<CFString>!](kcolorsyncsigdevicemfgdesctag.md)
- [var kColorSyncSigDeviceModelDescTag: Unmanaged<CFString>!](kcolorsyncsigdevicemodeldesctag.md)
- [var kColorSyncSigGamutTag: Unmanaged<CFString>!](kcolorsyncsiggamuttag.md)
- [var kColorSyncSigNamedColor2Tag: Unmanaged<CFString>!](kcolorsyncsignamedcolor2tag.md)
- [var kColorSyncSigProfileDescriptionTag: Unmanaged<CFString>!](kcolorsyncsigprofiledescriptiontag.md)
- [var kColorSyncSigProfileSequenceDescTag: Unmanaged<CFString>!](kcolorsyncsigprofilesequencedesctag.md)
- [var kColorSyncSigTechnologyTag: Unmanaged<CFString>!](kcolorsyncsigtechnologytag.md)
- [var kColorSyncSigViewingCondDescTag: Unmanaged<CFString>!](kcolorsyncsigviewingconddesctag.md)
- [var kColorSyncSigViewingConditionsTag: Unmanaged<CFString>!](kcolorsyncsigviewingconditionstag.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/profile-tags-and-signatures)*