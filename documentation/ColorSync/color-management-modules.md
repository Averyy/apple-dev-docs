# Color management modules

**Framework**: ColorSync

Work with the Color Management Modules that perform color conversions.

#### Overview

A Color Management Module (CMM) performs the calculations for a color conversion. ColorSync includes a default CMM and can load additional CMMs packaged as bundles. Most apps never work with a CMM directly, because ColorSync selects one automatically. You can also enumerate the installed CMMs, choose a preferred CMM for a transform with [`kColorSyncPreferredCMM`](kcolorsyncpreferredcmm.md), or implement your own by exporting the required entry-point functions from a bundle.

## Topics

### Working with CMMs
- [class ColorSyncCMM](colorsynccmm.md)
  A reference to a Color Management Module (CMM).
- [func ColorSyncCMMCreate(CFBundle!) -> Unmanaged<ColorSyncCMM>?](colorsynccmmcreate(_:).md)
  Creates a CMM object from a CMM bundle.
- [func ColorSyncCMMCopyCMMIdentifier(ColorSyncCMM!) -> Unmanaged<CFString>?](colorsynccmmcopycmmidentifier(_:).md)
  Copies the identifier of a CMM.
- [func ColorSyncCMMCopyLocalizedName(ColorSyncCMM!) -> Unmanaged<CFString>?](colorsynccmmcopylocalizedname(_:).md)
  Copies the localized name of a CMM.
- [func ColorSyncCMMGetBundle(ColorSyncCMM!) -> Unmanaged<CFBundle>?](colorsynccmmgetbundle(_:).md)
  Returns the bundle associated with a CMM.
- [func ColorSyncCMMGetTypeID() -> CFTypeID](colorsynccmmgettypeid().md)
  Returns the `CFTypeID` for `ColorSyncCMM`s.
- [func ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback!, UnsafeMutableRawPointer?)](colorsynciterateinstalledcmms(_:_:).md)
  Iterates over the installed CMMs, invoking a callback for each one.
### Implementing CMM callbacks
- [typealias ColorSyncCMMIterateCallback](colorsynccmmiteratecallback.md)
  A callback that the framework invokes for each installed CMM during iteration.
- [typealias CMMApplyTransformProc](cmmapplytransformproc.md)
  A function a CMM provider implements to apply a color transform to image data.
- [typealias CMMCreateTransformPropertyProc](cmmcreatetransformpropertyproc.md)
  A function a CMM provider implements to create a transform property for a given key.
- [typealias CMMInitializeLinkProfileProc](cmminitializelinkprofileproc.md)
  A function a CMM provider implements to initialize a device-link profile.
- [typealias CMMInitializeTransformProc](cmminitializetransformproc.md)
  A function a CMM provider implements to initialize a color transform.
### Registering plug-in entry points
- [var kCMMApplyTransformProcName: Unmanaged<CFString>!](kcmmapplytransformprocname.md)
  The CMM bundle info-dictionary key whose value is the name of the function that applies a color transform.
- [var kCMMCreateTransformPropertyProcName: Unmanaged<CFString>!](kcmmcreatetransformpropertyprocname.md)
  The CMM bundle info-dictionary key whose value is the name of the function that creates a transform property.
- [var kCMMInitializeLinkProfileProcName: Unmanaged<CFString>!](kcmminitializelinkprofileprocname.md)
  The CMM bundle info-dictionary key whose value is the name of the function that initializes a device-link profile.
- [var kCMMInitializeTransformProcName: Unmanaged<CFString>!](kcmminitializetransformprocname.md)
  The CMM bundle info-dictionary key whose value is the name of the function that initializes a color transform.

## See Also

- [Color devices](color-devices.md)
  Manage the color profiles assigned to displays, printers, scanners, and cameras.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/color-management-modules)*