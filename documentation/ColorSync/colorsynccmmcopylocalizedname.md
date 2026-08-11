# ColorSyncCMMCopyLocalizedName(_:)

**Framework**: ColorSync  
**Kind**: func

Copies the localized name of a CMM.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncCMMCopyLocalizedName(_: ColorSyncCMM!) -> Unmanaged<CFString>?
```

#### Return Value

The localized name of the CMM.

#### Discussion

Use this function to get the name of the built-in CMM.

## See Also

- [class ColorSyncCMM](colorsynccmm.md)
  A reference to a Color Management Module (CMM).
- [func ColorSyncCMMCreate(CFBundle!) -> Unmanaged<ColorSyncCMM>?](colorsynccmmcreate(_:).md)
  Creates a CMM object from a CMM bundle.
- [func ColorSyncCMMCopyCMMIdentifier(ColorSyncCMM!) -> Unmanaged<CFString>?](colorsynccmmcopycmmidentifier(_:).md)
  Copies the identifier of a CMM.
- [func ColorSyncCMMGetBundle(ColorSyncCMM!) -> Unmanaged<CFBundle>?](colorsynccmmgetbundle(_:).md)
  Returns the bundle associated with a CMM.
- [func ColorSyncCMMGetTypeID() -> CFTypeID](colorsynccmmgettypeid().md)
  Returns the `CFTypeID` for `ColorSyncCMM`s.
- [func ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback!, UnsafeMutableRawPointer?)](colorsynciterateinstalledcmms(_:_:).md)
  Iterates over the installed CMMs, invoking a callback for each one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynccmmcopylocalizedname(_:))*