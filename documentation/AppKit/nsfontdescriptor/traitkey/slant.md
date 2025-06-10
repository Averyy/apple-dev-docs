# slant

**Framework**: AppKit  
**Kind**: property

The relative slant angle value as a number object.

**Availability**:
- macOS ?+

## Declaration

```swift
static let slant: NSFontDescriptor.TraitKey
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object. The valid value range is from `-1.0` to `1.0`. The value of `0.0` corresponds to `0` degree clockwise rotation from the vertical and `1.0` corresponds to `30` degrees clockwise rotation.

## See Also

- [static let symbolic: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/symbolic.md)
  The symbolic traits value as a number object.
- [static let weight: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/weight.md)
  The normalized weight value as a number object.
- [static let width: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/width.md)
  The relative inter-glyph spacing value as a number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/traitkey/slant)*