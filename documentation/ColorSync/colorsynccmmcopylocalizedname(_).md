# ColorSyncCMMCopyLocalizedName(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Copies the localized name of a CMM.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncCMMCopyLocalizedName(_: ColorSyncCMM!) -> Unmanaged<CFString>?
```

```c
extern CFStringRefColorSyncCMMCopyLocalizedName(ColorSyncCMMRef );
```

#### Return Value

The localized name of the CMM.

#### Discussion

Use this function to get the name of the built-in CMM.

## See Also

### Working with CMMs
- [class ColorSyncCMM](./colorsynccmm.md)
  A reference to a Color Management Module (CMM).
- [func ColorSyncCMMCreate(CFBundle!) -> Unmanaged<ColorSyncCMM>?](./colorsynccmmcreate%28_%29.md)
  Creates a CMM object from a CMM bundle.
- [func ColorSyncCMMCopyCMMIdentifier(ColorSyncCMM!) -> Unmanaged<CFString>?](./colorsynccmmcopycmmidentifier%28_%29.md)
  Copies the identifier of a CMM.
- [func ColorSyncCMMGetBundle(ColorSyncCMM!) -> Unmanaged<CFBundle>?](./colorsynccmmgetbundle%28_%29.md)
  Returns the bundle associated with a CMM.
- [func ColorSyncCMMGetTypeID() -> CFTypeID](./colorsynccmmgettypeid%28%29.md)
  Returns the `CFTypeID` for `ColorSyncCMM`s.
- [func ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback!, UnsafeMutableRawPointer?)](./colorsynciterateinstalledcmms%28_,_%29.md)
  Iterates over the installed CMMs, invoking a callback for each one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynccmmcopylocalizedname(_:))*