# Color management modules

**Framework**: ColorSync

Work with the Color Management Modules that perform color conversions.

#### Overview

A Color Management Module (CMM) performs the calculations for a color conversion. ColorSync includes a default CMM and can load additional CMMs packaged as bundles. Most apps never work with a CMM directly, because ColorSync selects one automatically. You can also enumerate the installed CMMs, choose a preferred CMM for a transform with [`kColorSyncPreferredCMM`](kcolorsyncpreferredcmm.md), or implement your own by exporting the required entry-point functions from a bundle.

## Topics

### Working with CMMs
- [class ColorSyncCMM](colorsynccmm.md)
- [func ColorSyncCMMCreate(CFBundle!) -> Unmanaged<ColorSyncCMM>?](colorsynccmmcreate(_:).md)
- [func ColorSyncCMMCopyCMMIdentifier(ColorSyncCMM!) -> Unmanaged<CFString>?](colorsynccmmcopycmmidentifier(_:).md)
- [func ColorSyncCMMCopyLocalizedName(ColorSyncCMM!) -> Unmanaged<CFString>?](colorsynccmmcopylocalizedname(_:).md)
- [func ColorSyncCMMGetBundle(ColorSyncCMM!) -> Unmanaged<CFBundle>?](colorsynccmmgetbundle(_:).md)
- [func ColorSyncCMMGetTypeID() -> CFTypeID](colorsynccmmgettypeid().md)
- [func ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback!, UnsafeMutableRawPointer?)](colorsynciterateinstalledcmms(_:_:).md)
### Implementing CMM callbacks
- [typealias ColorSyncCMMIterateCallback](colorsynccmmiteratecallback.md)
- [typealias CMMApplyTransformProc](cmmapplytransformproc.md)
- [typealias CMMCreateTransformPropertyProc](cmmcreatetransformpropertyproc.md)
- [typealias CMMInitializeLinkProfileProc](cmminitializelinkprofileproc.md)
- [typealias CMMInitializeTransformProc](cmminitializetransformproc.md)
### Registering plug-in entry points
- [var kCMMApplyTransformProcName: Unmanaged<CFString>!](kcmmapplytransformprocname.md)
- [var kCMMCreateTransformPropertyProcName: Unmanaged<CFString>!](kcmmcreatetransformpropertyprocname.md)
- [var kCMMInitializeLinkProfileProcName: Unmanaged<CFString>!](kcmminitializelinkprofileprocname.md)
- [var kCMMInitializeTransformProcName: Unmanaged<CFString>!](kcmminitializetransformprocname.md)

## See Also

- [Color devices](color-devices.md)
  Manage the color profiles assigned to displays, printers, scanners, and cameras.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/color-management-modules)*