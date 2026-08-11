# ColorSyncCMMGetTypeID()

**Framework**: ColorSync  
**Kind**: func

Returns the `CFTypeID` for `ColorSyncCMM`s.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncCMMGetTypeID() -> CFTypeID
```

## See Also

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
- [func ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback!, UnsafeMutableRawPointer?)](colorsynciterateinstalledcmms(_:_:).md)
  Iterates over the installed CMMs, invoking a callback for each one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynccmmgettypeid())*