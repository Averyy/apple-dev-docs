# ColorSyncCMMCreate(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Creates a CMM object from a CMM bundle.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncCMMCreate(_ cmmBundle: CFBundle!) -> Unmanaged<ColorSyncCMM>?
```

```c
extern ColorSyncCMMRefColorSyncCMMCreate(CFBundleRef cmmBundle);
```

#### Return Value

A new [`ColorSyncCMM`](./colorsynccmm.md), or `NULL` in case of failure.

## Parameters

- `cmmBundle`: The bundle containing the CMM.

## See Also

### Working with CMMs
- [class ColorSyncCMM](./colorsynccmm.md)
  A reference to a Color Management Module (CMM).
- [func ColorSyncCMMCopyCMMIdentifier(ColorSyncCMM!) -> Unmanaged<CFString>?](./colorsynccmmcopycmmidentifier%28_%29.md)
  Copies the identifier of a CMM.
- [func ColorSyncCMMCopyLocalizedName(ColorSyncCMM!) -> Unmanaged<CFString>?](./colorsynccmmcopylocalizedname%28_%29.md)
  Copies the localized name of a CMM.
- [func ColorSyncCMMGetBundle(ColorSyncCMM!) -> Unmanaged<CFBundle>?](./colorsynccmmgetbundle%28_%29.md)
  Returns the bundle associated with a CMM.
- [func ColorSyncCMMGetTypeID() -> CFTypeID](./colorsynccmmgettypeid%28%29.md)
  Returns the `CFTypeID` for `ColorSyncCMM`s.
- [func ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback!, UnsafeMutableRawPointer?)](./colorsynciterateinstalledcmms%28_,_%29.md)
  Iterates over the installed CMMs, invoking a callback for each one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynccmmcreate(_:))*