# ColorSyncIterateInstalledCMMs(_:_:)

**Framework**: ColorSync  
**Kind**: func

Iterates over the installed CMMs, invoking a callback for each one.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncIterateInstalledCMMs(_ callBack: ColorSyncCMMIterateCallback!, _ userInfo: UnsafeMutableRawPointer?)
```

## Parameters

- `callBack`: A pointer to a client-provided function.
- `userInfo`: A pointer to the user info that the framework passes to the callback. Optional.

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
- [func ColorSyncCMMGetTypeID() -> CFTypeID](colorsynccmmgettypeid().md)
  Returns the `CFTypeID` for `ColorSyncCMM`s.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynciterateinstalledcmms(_:_:))*