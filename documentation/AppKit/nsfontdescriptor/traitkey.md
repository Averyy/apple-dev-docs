# NSFontDescriptor.TraitKey

**Framework**: AppKit  
**Kind**: struct

Constants that can be used as keys to retrieve information about a font descriptor from its trait dictionary.

**Availability**:
- macOS ?+

## Declaration

```swift
struct TraitKey
```

#### Discussion

These keys are used with [`traits`](nsfontdescriptor/attributename/traits.md).

## Topics

### Trait Keys
- [static let symbolic: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/symbolic.md)
  The symbolic traits value as a number object.
- [static let weight: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/weight.md)
  The normalized weight value as a number object.
- [static let width: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/width.md)
  The relative inter-glyph spacing value as a number object.
- [static let slant: NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey/slant.md)
  The relative slant angle value as a number object.
### Initializers
- [init(rawValue: String)](nsfontdescriptor/traitkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var symbolicTraits: NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.property.md)
  A bit mask that describes the traits of the receiver.
- [typealias NSFontSymbolicTraits](nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/traitkey)*