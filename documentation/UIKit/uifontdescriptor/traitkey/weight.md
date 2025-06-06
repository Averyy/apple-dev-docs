# weight

**Framework**: UIKit  
**Kind**: property

The numerical value that corresponds to a font face.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let weight: UIFontDescriptor.TraitKey
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object. The valid value range is from `-1.0` to `1.0`, where `0.0` corresponds to the [`regular`](https://developer.apple.com/documentation/SwiftUI/Font/Weight/regular) weight constant. The negative side of the value range indicates that the font is light or thin; the positive side means the font is heavier or bolder. For example, the font face [`ultraLight`](uifont/weight/ultralight.md) has the approximate value of `-0.8`, and [`black`](https://developer.apple.com/documentation/AppKit/NSFont/Weight/black) has the approximate value of `0.62`. When providing a weight that doesn’t precisely match a font face in the family, the system locates an available face that represents the closest match.

You can use a font face constant to specify a weight; for a list of constants, see [`UIFont.Weight`](uifont/weight.md).

To access the weight of a font, first retrieve the font’s [`traits`](uifontdescriptor/attributename/traits.md) dictionary information:

```swift
let font = UIFont.systemFont(ofSize: 21, weight: .bold)
if let traits = font.fontDescriptor.object(forKey: .traits) as? [UIFontDescriptor.TraitKey: Any]{
    let weightValue = traits[.weight]
}
```

## See Also

- [static let slant: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/slant.md)
  The relative slant angle of the font.
- [static let symbolic: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/symbolic.md)
  The symbolic font traits.
- [static let width: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/width.md)
  The inter-glyph spacing of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey/weight)*