# UIFontDescriptor.FeatureKey

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Keys for retrieving feature settings.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 4.0+

## Declaration

```swift
struct FeatureKey
```

```c
typedef NSString * UIFontDescriptorFeatureKey;
```

## Overview

Use these keys when retrieving information from one of the dictionaries associated with the [`featureSettings`](./attributename/featuresettings.md) key.

## Topics

### Keys
- [static let type: UIFontDescriptor.FeatureKey](./featurekey/type.md)
  A key for identifying the font feature type.
- [static let selector: UIFontDescriptor.FeatureKey](./featurekey/selector.md)
  A key for identifying the font feature selector.
- [static let featureIdentifier: UIFontDescriptor.FeatureKey](./featurekey/featureidentifier.md)
  A key for identifying a font feature type.
- [static let typeIdentifier: UIFontDescriptor.FeatureKey](./featurekey/typeidentifier.md)
  A key for identifying the font feature selector.
### Initializers
- [init(String)](./featurekey/init%28_%29.md)
  Creates a font feature key.
- [init(rawValue: String)](./featurekey/init%28rawvalue%29.md)
  Creates a font feature key with the specified raw value.

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
- [UIFontDescriptor.TraitKey](./traitkey.md)
  Keys for retrieving the font descriptor’s trait information.
- [UIFont.Weight](../uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](../uifont/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/featurekey)*