# weight

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The normalized weight value as a number object.

**Availability**:
- macOS

## Declaration

```swift
static let weight: NSFontDescriptor.TraitKey
```

```c
extern NSFontDescriptorTraitKey NSFontWeightTrait;
```

## Discussion

The value of this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object. The valid value range is from `-1.0` to `1.0`. The value of `0.0` corresponds to the regular or medium font weight.

## See Also

### Trait Keys
- [static let symbolic: NSFontDescriptor.TraitKey](./symbolic.md)
  The symbolic traits value as a number object.
- [static let width: NSFontDescriptor.TraitKey](./width.md)
  The relative inter-glyph spacing value as a number object.
- [static let slant: NSFontDescriptor.TraitKey](./slant.md)
  The relative slant angle value as a number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/traitkey/weight)*