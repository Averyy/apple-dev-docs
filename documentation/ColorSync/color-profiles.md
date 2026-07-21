# Color profiles

**Framework**: ColorSync

Work with the ICC profiles that describe device and working color spaces.

#### Overview

A [`ColorSyncProfile`](colorsyncprofile.md) wraps an ICC profile, the description of a device or working color space that ColorSync uses to convert color accurately. Create profiles from a name, a file, or raw ICC data, and read a profile’s tags and header. To round trip a profile through raw ICC bytes, use [`ColorSyncProfileCopyData(_:_:)`](colorsyncprofilecopydata(_:_:).md) to get the bytes you embed in an image or file, and [`ColorSyncProfileCreate(_:_:)`](colorsyncprofilecreate(_:_:).md) to reconstruct a profile from bytes you extract. On macOS, you can also install a profile for the current user in `~/Library/ColorSync/Profiles`, or for everyone on the system in `/Library/ColorSync/Profiles`. To convert color between profiles, build a [`ColorSyncTransform`](colorsynctransform.md). To bridge to Core Graphics, pass a profile to [`CGColorSpaceCreateWithColorSyncProfile(_:_:)`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpaceCreateWithColorSyncProfile(_:_:)).

## Topics

### Profiling objects
- [class ColorSyncMutableProfile](colorsyncmutableprofile.md)
- [class ColorSyncProfile](colorsyncprofile.md)
### Creating a profile
- [func ColorSyncProfileCreateWithName(CFString!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithname(_:).md)
- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurl(_:_:).md)
- [func ColorSyncProfileCreateWithURLAndOptions(CFURL!, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurlandoptions(_:_:_:).md)
- [func ColorSyncProfileCreateMutable() -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutable().md)
- [func ColorSyncProfileCreateMutableCopy(ColorSyncProfile!) -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutablecopy(_:).md)
### Embedding and extracting profiles
- [func ColorSyncProfileCopyData(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFData>!](colorsyncprofilecopydata(_:_:).md)
- [func ColorSyncProfileCreate(CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreate(_:_:).md)
### Accessing standard RGB profiles
- [var kColorSyncSRGBProfile: Unmanaged<CFString>!](kcolorsyncsrgbprofile.md)
- [var kColorSyncAdobeRGB1998Profile: Unmanaged<CFString>!](kcolorsyncadobergb1998profile.md)
- [var kColorSyncDisplayP3Profile: Unmanaged<CFString>!](kcolorsyncdisplayp3profile.md)
- [var kColorSyncDCIP3Profile: Unmanaged<CFString>!](kcolorsyncdcip3profile.md)
- [var kColorSyncITUR709Profile: Unmanaged<CFString>!](kcolorsyncitur709profile.md)
- [var kColorSyncITUR2020Profile: Unmanaged<CFString>!](kcolorsyncitur2020profile.md)
- [var kColorSyncROMMRGBProfile: Unmanaged<CFString>!](kcolorsyncrommrgbprofile.md)
- [var kColorSyncACESCGLinearProfile: Unmanaged<CFString>!](kcolorsyncacescglinearprofile.md)
- [var kColorSyncGenericRGBProfile: Unmanaged<CFString>!](kcolorsyncgenericrgbprofile.md)
### Accessing generic and special profiles
- [var kColorSyncGenericGrayProfile: Unmanaged<CFString>!](kcolorsyncgenericgrayprofile.md)
- [var kColorSyncGenericGrayGamma22Profile: Unmanaged<CFString>!](kcolorsyncgenericgraygamma22profile.md)
- [var kColorSyncGenericCMYKProfile: Unmanaged<CFString>!](kcolorsyncgenericcmykprofile.md)
- [var kColorSyncGenericLabProfile: Unmanaged<CFString>!](kcolorsyncgenericlabprofile.md)
- [var kColorSyncGenericXYZProfile: Unmanaged<CFString>!](kcolorsyncgenericxyzprofile.md)
- [var kColorSyncWebSafeColorsProfile: Unmanaged<CFString>!](kcolorsyncwebsafecolorsprofile.md)
### Reading profile data
- [func ColorSyncProfileCopyDescriptionString(ColorSyncProfile!) -> Unmanaged<CFString>?](colorsyncprofilecopydescriptionstring(_:).md)
- [func ColorSyncProfileCopyHeader(ColorSyncProfile!) -> Unmanaged<CFData>!](colorsyncprofilecopyheader(_:).md)
- [func ColorSyncProfileGetURL(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>!](colorsyncprofilegeturl(_:_:).md)
- [func ColorSyncProfileGetTypeID() -> CFTypeID](colorsyncprofilegettypeid().md)
### Managing tags and the header
- [func ColorSyncProfileContainsTag(ColorSyncProfile!, CFString!) -> Bool](colorsyncprofilecontainstag(_:_:).md)
- [func ColorSyncProfileCopyTag(ColorSyncProfile!, CFString!) -> Unmanaged<CFData>?](colorsyncprofilecopytag(_:_:).md)
- [func ColorSyncProfileCopyTagSignatures(ColorSyncProfile!) -> Unmanaged<CFArray>?](colorsyncprofilecopytagsignatures(_:).md)
- [func ColorSyncProfileRemoveTag(ColorSyncMutableProfile!, CFString!)](colorsyncprofileremovetag(_:_:).md)
- [func ColorSyncProfileSetHeader(ColorSyncMutableProfile!, CFData!)](colorsyncprofilesetheader(_:_:).md)
- [func ColorSyncProfileSetTag(ColorSyncMutableProfile!, CFString!, CFData!)](colorsyncprofilesettag(_:_:_:).md)
### Inspecting color characteristics
- [func ColorSyncProfileIsWideGamut(ColorSyncProfile!) -> Bool](colorsyncprofileiswidegamut(_:).md)
- [func ColorSyncProfileIsPQBased(ColorSyncProfile!) -> Bool](colorsyncprofileispqbased(_:).md)
- [func ColorSyncProfileIsHLGBased(ColorSyncProfile!) -> Bool](colorsyncprofileishlgbased(_:).md)
- [func ColorSyncProfileIsMatrixBased(ColorSyncProfile!) -> Bool](colorsyncprofileismatrixbased(_:).md)
- [func ColorSyncProfileEstimateGamma(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](colorsyncprofileestimategamma(_:_:).md)
- [func ColorSyncProfileVerify(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileverify(_:_:_:).md)
### Finding installed profiles
- [func ColorSyncIterateInstalledProfiles(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofiles(_:_:_:_:).md)
- [typealias ColorSyncProfileIterateCallback](colorsyncprofileiteratecallback.md)
### Installing profiles
- [func ColorSyncProfileInstall(ColorSyncProfile!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileinstall(_:_:_:_:).md)
- [func ColorSyncProfileUninstall(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileuninstall(_:_:).md)
- [func ColorSyncIterateInstalledProfilesWithOptions(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:).md)
- [var COLORSYNC_PROFILE_INSTALL_ENTITLEMENT: String](colorsync_profile_install_entitlement.md)
- [var kColorSyncProfileComputerDomain: Unmanaged<CFString>!](kcolorsyncprofilecomputerdomain.md)
- [var kColorSyncProfileUserDomain: Unmanaged<CFString>!](kcolorsyncprofileuserdomain.md)
### Accessing profile properties
- [var kColorSyncProfileClass: Unmanaged<CFString>!](kcolorsyncprofileclass.md)
- [var kColorSyncProfileColorSpace: Unmanaged<CFString>!](kcolorsyncprofilecolorspace.md)
- [var kColorSyncProfileDescription: Unmanaged<CFString>!](kcolorsyncprofiledescription.md)
- [var kColorSyncProfileHeader: Unmanaged<CFString>!](kcolorsyncprofileheader.md)
- [var kColorSyncProfileIsValid: Unmanaged<CFString>!](kcolorsyncprofileisvalid.md)
- [var kColorSyncProfilePCS: Unmanaged<CFString>!](kcolorsyncprofilepcs.md)
- [var kColorSyncProfileURL: Unmanaged<CFString>!](kcolorsyncprofileurl.md)
### Computing profile digests
- [func ColorSyncProfileGetMD5(ColorSyncProfile!) -> ColorSyncMD5](colorsyncprofilegetmd5(_:).md)
- [struct ColorSyncMD5](colorsyncmd5.md)
- [var COLORSYNC_MD5_LENGTH: Int32](colorsync_md5_length.md)
- [var kColorSyncProfileMD5Digest: Unmanaged<CFString>!](kcolorsyncprofilemd5digest.md)
### Tracking changes and cache
- [var kColorSyncProfileRepositoryChangeNotification: Unmanaged<CFString>!](kcolorsyncprofilerepositorychangenotification.md)
- [var kColorSyncProfileCacheSeed: Unmanaged<CFString>!](kcolorsyncprofilecacheseed.md)
- [var kColorSyncWaitForCacheReply: Unmanaged<CFString>!](kcolorsyncwaitforcachereply.md)

## See Also

- [Headroom Adaptive Gain Curve](headroom-adaptive-gain-curve.md)
  Work with SMPTE ST 2094-50 tone-mapping metadata shared between HDR stills and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/color-profiles)*