# NSFontDescriptor.TraitKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that can be used as keys to retrieve information about a font descriptor from its trait dictionary.

**Availability**:
- macOS

## Declaration

```swift
struct TraitKey
```

```c
typedef NSString * NSFontDescriptorTraitKey;
```

## Discussion

These keys are used with [`traits`](./attributename/traits.md).

## Topics

### Trait Keys
- [static let symbolic: NSFontDescriptor.TraitKey](./traitkey/symbolic.md)
  The symbolic traits value as a number object.
- [static let weight: NSFontDescriptor.TraitKey](./traitkey/weight.md)
  The normalized weight value as a number object.
- [static let width: NSFontDescriptor.TraitKey](./traitkey/width.md)
  The relative inter-glyph spacing value as a number object.
- [static let slant: NSFontDescriptor.TraitKey](./traitkey/slant.md)
  The relative slant angle value as a number object.
### Initializers
- [init(rawValue: String)](./traitkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Font Traits
- [var symbolicTraits: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.property.md)
  A bit mask that describes the traits of the receiver.
- [typealias NSFontSymbolicTraits](../nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/traitkey)*