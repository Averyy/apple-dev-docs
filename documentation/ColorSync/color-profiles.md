# Color profiles

**Framework**: ColorSync

Work with the ICC profiles that describe device and working color spaces.

#### Overview

A [`ColorSyncProfile`](colorsyncprofile.md) wraps an ICC profile, the description of a device or working color space that ColorSync uses to convert color accurately. Create profiles from a name, a file, or raw ICC data, and read a profile’s tags and header. To round trip a profile through raw ICC bytes, use [`ColorSyncProfileCopyData(_:_:)`](colorsyncprofilecopydata(_:_:).md) to get the bytes you embed in an image or file, and [`ColorSyncProfileCreate(_:_:)`](colorsyncprofilecreate(_:_:).md) to reconstruct a profile from bytes you extract. On macOS, you can also install a profile for the current user in `~/Library/ColorSync/Profiles`, or for everyone on the system in `/Library/ColorSync/Profiles`. To convert color between profiles, build a [`ColorSyncTransform`](colorsynctransform.md). To bridge to Core Graphics, pass a profile to [`CGColorSpaceCreateWithColorSyncProfile(_:_:)`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpaceCreateWithColorSyncProfile(_:_:)).

## Topics

### Profiling objects
- [class ColorSyncMutableProfile](colorsyncmutableprofile.md)
  A reference to a mutable ICC color profile.
- [class ColorSyncProfile](colorsyncprofile.md)
  A reference to an immutable International Color Consortium (ICC) color profile.
### Creating a profile
- [func ColorSyncProfileCreateWithName(CFString!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithname(_:).md)
  Creates a profile from a predefined profile name.
- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurl(_:_:).md)
  Creates a profile from ICC profile data at a URL.
- [func ColorSyncProfileCreateWithURLAndOptions(CFURL!, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurlandoptions(_:_:_:).md)
  Creates a profile from ICC profile data at a URL, using the given options.
- [func ColorSyncProfileCreateMutable() -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutable().md)
  Creates an empty mutable profile.
- [func ColorSyncProfileCreateMutableCopy(ColorSyncProfile!) -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutablecopy(_:).md)
  Creates a mutable copy of a profile.
### Embedding and extracting profiles
- [func ColorSyncProfileCopyData(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFData>!](colorsyncprofilecopydata(_:_:).md)
  Copies the flattened data from a profile.
- [func ColorSyncProfileCreate(CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreate(_:_:).md)
  Creates a profile from ICC profile data.
### Accessing standard RGB profiles
- [var kColorSyncSRGBProfile: Unmanaged<CFString>!](kcolorsyncsrgbprofile.md)
  The sRGB color profile.
- [var kColorSyncAdobeRGB1998Profile: Unmanaged<CFString>!](kcolorsyncadobergb1998profile.md)
  The Adobe RGB (1998) color profile.
- [var kColorSyncDisplayP3Profile: Unmanaged<CFString>!](kcolorsyncdisplayp3profile.md)
  The Display P3 color profile.
- [var kColorSyncDCIP3Profile: Unmanaged<CFString>!](kcolorsyncdcip3profile.md)
  The DCI-P3 color profile.
- [var kColorSyncITUR709Profile: Unmanaged<CFString>!](kcolorsyncitur709profile.md)
  The ITU-R BT.709 color profile.
- [var kColorSyncITUR2020Profile: Unmanaged<CFString>!](kcolorsyncitur2020profile.md)
  The ITU-R BT.2020 color profile.
- [var kColorSyncROMMRGBProfile: Unmanaged<CFString>!](kcolorsyncrommrgbprofile.md)
  The ROMM RGB (ProPhoto RGB) color profile.
- [var kColorSyncACESCGLinearProfile: Unmanaged<CFString>!](kcolorsyncacescglinearprofile.md)
  The ACEScg linear color profile.
- [var kColorSyncGenericRGBProfile: Unmanaged<CFString>!](kcolorsyncgenericrgbprofile.md)
  The generic RGB color profile.
### Accessing generic and special profiles
- [var kColorSyncGenericGrayProfile: Unmanaged<CFString>!](kcolorsyncgenericgrayprofile.md)
  The generic gray color profile.
- [var kColorSyncGenericGrayGamma22Profile: Unmanaged<CFString>!](kcolorsyncgenericgraygamma22profile.md)
  The generic gray color profile with a gamma of 2.2.
- [var kColorSyncGenericCMYKProfile: Unmanaged<CFString>!](kcolorsyncgenericcmykprofile.md)
  The generic CMYK color profile.
- [var kColorSyncGenericLabProfile: Unmanaged<CFString>!](kcolorsyncgenericlabprofile.md)
  The generic CIELAB color profile.
- [var kColorSyncGenericXYZProfile: Unmanaged<CFString>!](kcolorsyncgenericxyzprofile.md)
  The generic CIEXYZ color profile.
- [var kColorSyncWebSafeColorsProfile: Unmanaged<CFString>!](kcolorsyncwebsafecolorsprofile.md)
  The web-safe colors profile.
### Reading profile data
- [func ColorSyncProfileCopyDescriptionString(ColorSyncProfile!) -> Unmanaged<CFString>?](colorsyncprofilecopydescriptionstring(_:).md)
  Copies the localized description string of a profile.
- [func ColorSyncProfileCopyHeader(ColorSyncProfile!) -> Unmanaged<CFData>!](colorsyncprofilecopyheader(_:).md)
  Copies the header from a profile.
- [func ColorSyncProfileGetURL(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFURL>!](colorsyncprofilegeturl(_:_:).md)
  Returns the URL of a profile.
- [func ColorSyncProfileGetTypeID() -> CFTypeID](colorsyncprofilegettypeid().md)
  Returns the unique identifier for the ColorSync profile opaque type.
### Managing tags and the header
- [func ColorSyncProfileContainsTag(ColorSyncProfile!, CFString!) -> Bool](colorsyncprofilecontainstag(_:_:).md)
  Returns a Boolean value indicating whether a profile contains a given tag.
- [func ColorSyncProfileCopyTag(ColorSyncProfile!, CFString!) -> Unmanaged<CFData>?](colorsyncprofilecopytag(_:_:).md)
  Copies a tag from a profile.
- [func ColorSyncProfileCopyTagSignatures(ColorSyncProfile!) -> Unmanaged<CFArray>?](colorsyncprofilecopytagsignatures(_:).md)
  Copies the tag signatures of a profile.
- [func ColorSyncProfileRemoveTag(ColorSyncMutableProfile!, CFString!)](colorsyncprofileremovetag(_:_:).md)
  Removes a tag from a mutable profile.
- [func ColorSyncProfileSetHeader(ColorSyncMutableProfile!, CFData!)](colorsyncprofilesetheader(_:_:).md)
  Sets the header of a mutable profile.
- [func ColorSyncProfileSetTag(ColorSyncMutableProfile!, CFString!, CFData!)](colorsyncprofilesettag(_:_:_:).md)
  Sets a tag in a mutable profile.
### Inspecting color characteristics
- [func ColorSyncProfileIsWideGamut(ColorSyncProfile!) -> Bool](colorsyncprofileiswidegamut(_:).md)
  Returns a Boolean value indicating whether the display profile describes a wide-gamut color space.
- [func ColorSyncProfileIsPQBased(ColorSyncProfile!) -> Bool](colorsyncprofileispqbased(_:).md)
  Returns a Boolean value indicating whether the profile uses ITU BT.2100 PQ transfer functions.
- [func ColorSyncProfileIsHLGBased(ColorSyncProfile!) -> Bool](colorsyncprofileishlgbased(_:).md)
  Returns a Boolean value indicating whether the profile uses ITU BT.2100 HLG transfer functions.
- [func ColorSyncProfileIsMatrixBased(ColorSyncProfile!) -> Bool](colorsyncprofileismatrixbased(_:).md)
  Returns a Boolean value indicating whether the profile is matrix-based.
- [func ColorSyncProfileEstimateGamma(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](colorsyncprofileestimategamma(_:_:).md)
  Estimates the gamma of a profile.
- [func ColorSyncProfileVerify(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileverify(_:_:_:).md)
  Verifies whether a profile can be used.
### Finding installed profiles
- [func ColorSyncIterateInstalledProfiles(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofiles(_:_:_:_:).md)
  Iterates over the installed profiles.
- [typealias ColorSyncProfileIterateCallback](colorsyncprofileiteratecallback.md)
  A callback that the framework invokes for each installed profile during iteration.
### Installing profiles
- [func ColorSyncProfileInstall(ColorSyncProfile!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileinstall(_:_:_:_:).md)
  Installs a profile in the specified domain.
- [func ColorSyncProfileUninstall(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileuninstall(_:_:).md)
  Uninstalls a profile.
- [func ColorSyncIterateInstalledProfilesWithOptions(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:).md)
  Iterates over the installed profiles, using the given options.
- [var COLORSYNC_PROFILE_INSTALL_ENTITLEMENT: String](colorsync_profile_install_entitlement.md)
- [var kColorSyncProfileComputerDomain: Unmanaged<CFString>!](kcolorsyncprofilecomputerdomain.md)
  The profile domain for profiles shared by all users of the computer.
- [var kColorSyncProfileUserDomain: Unmanaged<CFString>!](kcolorsyncprofileuserdomain.md)
  The profile domain for the current user’s profiles.
### Accessing profile properties
- [var kColorSyncProfileClass: Unmanaged<CFString>!](kcolorsyncprofileclass.md)
  A key for the profile’s class.
- [var kColorSyncProfileColorSpace: Unmanaged<CFString>!](kcolorsyncprofilecolorspace.md)
  A key for the profile’s color space.
- [var kColorSyncProfileDescription: Unmanaged<CFString>!](kcolorsyncprofiledescription.md)
  A key for the profile’s localized description.
- [var kColorSyncProfileHeader: Unmanaged<CFString>!](kcolorsyncprofileheader.md)
  A key for the profile’s header data.
- [var kColorSyncProfileIsValid: Unmanaged<CFString>!](kcolorsyncprofileisvalid.md)
  A key indicating whether the profile is valid.
- [var kColorSyncProfilePCS: Unmanaged<CFString>!](kcolorsyncprofilepcs.md)
  A key for the profile’s connection space (PCS).
- [var kColorSyncProfileURL: Unmanaged<CFString>!](kcolorsyncprofileurl.md)
  A key for the profile’s URL.
### Computing profile digests
- [func ColorSyncProfileGetMD5(ColorSyncProfile!) -> ColorSyncMD5](colorsyncprofilegetmd5(_:).md)
  Returns the MD5 digest for a profile.
- [struct ColorSyncMD5](colorsyncmd5.md)
  An MD5 digest that uniquely identifies a profile, as defined by the ICC specification.
- [var COLORSYNC_MD5_LENGTH: Int32](colorsync_md5_length.md)
- [var kColorSyncProfileMD5Digest: Unmanaged<CFString>!](kcolorsyncprofilemd5digest.md)
  A key for the profile’s MD5 digest.
### Tracking changes and cache
- [var kColorSyncProfileRepositoryChangeNotification: Unmanaged<CFString>!](kcolorsyncprofilerepositorychangenotification.md)
  A notification that ColorSync posts when the profile repository changes.
- [var kColorSyncProfileCacheSeed: Unmanaged<CFString>!](kcolorsyncprofilecacheseed.md)
  The current profile-cache seed (uint32_t), sent with [`kColorSyncProfileRepositoryChangeNotification`](kcolorsyncprofilerepositorychangenotification.md).
- [var kColorSyncWaitForCacheReply: Unmanaged<CFString>!](kcolorsyncwaitforcachereply.md)
  An iteration option that waits for the profile cache to finish updating before returning.

## See Also

- [Headroom Adaptive Gain Curve](headroom-adaptive-gain-curve.md)
  Work with SMPTE ST 2094-50 tone-mapping metadata shared between HDR stills and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/color-profiles)*