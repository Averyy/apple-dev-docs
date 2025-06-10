# width

**Framework**: AppKit  
**Kind**: property

The relative inter-glyph spacing value as a number object.

**Availability**:
- macOS ?+

## Declaration

```swift
static let width: NSFontDescriptor.TraitKey
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object. The valid value range is from `-1.0` to `1.0`. The value of `0.0` corresponds to the regular glyph spacing.

## See Also

- [static let symbolic: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/symbolic.md)
  The symbolic traits value as a number object.
- [static let weight: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/weight.md)
  The normalized weight value as a number object.
- [static let slant: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/slant.md)
  The relative slant angle value as a number object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/traitkey/width)*