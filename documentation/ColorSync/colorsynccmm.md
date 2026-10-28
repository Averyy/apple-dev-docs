# ColorSyncCMM

**Framework**: ColorSync  
**Kind**: class  
**Role**: Class

A reference to a Color Management Module (CMM).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
class ColorSyncCMM
```

```c
typedef struct ColorSyncCMM * ColorSyncCMMRef;
```

## Overview

This type is a lightweight wrapper around a Core Foundation bundle.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Working with CMMs
- [func ColorSyncCMMCreate(CFBundle!) -> Unmanaged<ColorSyncCMM>?](./colorsynccmmcreate%28_%29.md)
  Creates a CMM object from a CMM bundle.
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

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynccmm)*