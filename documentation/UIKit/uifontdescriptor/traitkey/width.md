# width

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The inter-glyph spacing of the font.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let width: UIFontDescriptor.TraitKey
```

```c
extern UIFontDescriptorTraitKey const UIFontWidthTrait;
```

## Discussion

The value of this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object. The valid value range is from `-1.0` to `1.0`. The value of `0.0` corresponds to the regular glyph spacing.

## See Also

### Font traits
- [static let slant: UIFontDescriptor.TraitKey](./slant.md)
  The relative slant angle of the font.
- [static let symbolic: UIFontDescriptor.TraitKey](./symbolic.md)
  The symbolic font traits.
- [static let weight: UIFontDescriptor.TraitKey](./weight.md)
  The numerical value that corresponds to a font face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey/width)*