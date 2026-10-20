# ColorSyncCMMCopyCMMIdentifier(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Copies the identifier of a CMM.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncCMMCopyCMMIdentifier(_: ColorSyncCMM!) -> Unmanaged<CFString>?
```

```c
extern CFStringRefColorSyncCMMCopyCMMIdentifier(ColorSyncCMMRef );
```

#### Return Value

The identifier of the CMM.

#### Discussion

Use this function to get the identifier of the built-in CMM.

## See Also

### Working with CMMs
- [class ColorSyncCMM](./colorsynccmm.md)
  A reference to a Color Management Module (CMM).
- [func ColorSyncCMMCreate(CFBundle!) -> Unmanaged<ColorSyncCMM>?](./colorsynccmmcreate%28_%29.md)
  Creates a CMM object from a CMM bundle.
- [func ColorSyncCMMCopyLocalizedName(ColorSyncCMM!) -> Unmanaged<CFString>?](./colorsynccmmcopylocalizedname%28_%29.md)
  Copies the localized name of a CMM.
- [func ColorSyncCMMGetBundle(ColorSyncCMM!) -> Unmanaged<CFBundle>?](./colorsynccmmgetbundle%28_%29.md)
  Returns the bundle associated with a CMM.
- [func ColorSyncCMMGetTypeID() -> CFTypeID](./colorsynccmmgettypeid%28%29.md)
  Returns the `CFTypeID` for `ColorSyncCMM`s.
- [func ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback!, UnsafeMutableRawPointer?)](./colorsynciterateinstalledcmms%28_,_%29.md)
  Iterates over the installed CMMs, invoking a callback for each one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynccmmcopycmmidentifier(_:))*