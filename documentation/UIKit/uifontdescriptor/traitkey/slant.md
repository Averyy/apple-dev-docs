# slant

**Framework**: UIKit  
**Kind**: property

The relative slant angle of the font.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let slant: UIFontDescriptor.TraitKey
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object. The valid value range is from `-1.0` to `1.0`. The value of `0.0` corresponds to `0` degree clockwise rotation from the vertical and `1.0` corresponds to `30` degrees clockwise rotation.

## See Also

- [static let symbolic: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/symbolic.md)
  The symbolic font traits.
- [static let weight: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/weight.md)
  The numerical value that corresponds to a font face.
- [static let width: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/width.md)
  The inter-glyph spacing of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey/slant)*