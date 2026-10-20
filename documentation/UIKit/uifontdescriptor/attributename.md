# UIFontDescriptor.AttributeName

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that describe font attributes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 4.0+

## Declaration

```swift
struct AttributeName
```

```c
typedef NSString * UIFontDescriptorAttributeName;
```

## Topics

### Constants
- [static let cascadeList: UIFontDescriptor.AttributeName](./attributename/cascadelist.md)
  The cascading list attribute.
- [static let characterSet: UIFontDescriptor.AttributeName](./attributename/characterset.md)
  The character set attribute.
- [static let face: UIFontDescriptor.AttributeName](./attributename/face.md)
  The font face attribute.
- [static let family: UIFontDescriptor.AttributeName](./attributename/family.md)
  The font family attribute.
- [static let featureSettings: UIFontDescriptor.AttributeName](./attributename/featuresettings.md)
  The font feature settings attribute.
- [static let fixedAdvance: UIFontDescriptor.AttributeName](./attributename/fixedadvance.md)
  The glyph advancement attribute.
- [static let matrix: UIFontDescriptor.AttributeName](./attributename/matrix.md)
  The font’s transformation matrix attribute.
- [static let name: UIFontDescriptor.AttributeName](./attributename/name.md)
  The font name attribute.
- [static let size: UIFontDescriptor.AttributeName](./attributename/size.md)
  The font size attribute.
- [static let textStyle: UIFontDescriptor.AttributeName](./attributename/textstyle.md)
  The text style attribute.
- [static let traits: UIFontDescriptor.AttributeName](./attributename/traits.md)
  The font traits dictionary attribute.
- [static let visibleName: UIFontDescriptor.AttributeName](./attributename/visiblename.md)
  The font’s visible name attribute.
### Initializers
- [init(rawValue: String)](./attributename/init%28rawvalue%29.md)
  Creates an attribute name with the specified raw value.

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
- [UIFontDescriptor.FeatureKey](./featurekey.md)
  Keys for retrieving feature settings.
- [UIFontDescriptor.TraitKey](./traitkey.md)
  Keys for retrieving the font descriptor’s trait information.
- [UIFont.Weight](../uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](../uifont/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/attributename)*