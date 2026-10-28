# UIFontDescriptor.TraitKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Keys for retrieving the font descriptor’s trait information.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 4.0+

## Declaration

```swift
struct TraitKey
```

```c
typedef NSString * UIFontDescriptorTraitKey;
```

## Overview

Use these keys to fetch values from the dictionary associated with the [`traits`](./attributename/traits.md) key.

## Topics

### Font traits
- [static let slant: UIFontDescriptor.TraitKey](./traitkey/slant.md)
  The relative slant angle of the font.
- [static let symbolic: UIFontDescriptor.TraitKey](./traitkey/symbolic.md)
  The symbolic font traits.
- [static let weight: UIFontDescriptor.TraitKey](./traitkey/weight.md)
  The numerical value that corresponds to a font face.
- [static let width: UIFontDescriptor.TraitKey](./traitkey/width.md)
  The inter-glyph spacing of the font.
### Initializer
- [init(rawValue: String)](./traitkey/init%28rawvalue%29.md)
  Creates a font trait key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIFont.TextStyle](../uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
- [UIFontDescriptor.SystemDesign](./systemdesign.md)
  Constants that describe the system-defined typeface designs.
- [UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [UIFontDescriptor.Class](./class.md)
  Constants that classify certain stylistic qualities of the font.
- [UIFontDescriptor.AttributeName](./attributename.md)
  Constants that describe font attributes.
- [UIFontDescriptor.FeatureKey](./featurekey.md)
  Keys for retrieving feature settings.
- [UIFont.Weight](../uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](../uifont/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey)*