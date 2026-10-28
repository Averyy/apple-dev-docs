# UIFontDescriptor.SystemDesign

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that describe the system-defined typeface designs.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 5.2+

## Declaration

```swift
struct SystemDesign
```

```c
typedef NSString * UIFontDescriptorSystemDesign;
```

## Overview

Use these constants to specify a system-provided typeface design, such as:

- SF Pro in iOS or SF Compact in watchOS ([`default`](./systemdesign/default.md))
- SF Pro Rounded in iOS or SF Compact Rounded in watchOS ([`rounded`](./systemdesign/rounded.md))
- SF Mono ([`monospaced`](./systemdesign/monospaced.md))
- New York ([`serif`](./systemdesign/serif.md))

## Topics

### Typeface designs
- [static let `default`: UIFontDescriptor.SystemDesign](./systemdesign/default.md)
  The default typeface for an app’s user interface.
- [static let rounded: UIFontDescriptor.SystemDesign](./systemdesign/rounded.md)
  The rounded variant of the default typeface.
- [static let monospaced: UIFontDescriptor.SystemDesign](./systemdesign/monospaced.md)
  The monospace variant of the default typeface.
- [static let serif: UIFontDescriptor.SystemDesign](./systemdesign/serif.md)
  The serif variant of the default typeface.
### Initializers
- [init(rawValue: String)](./systemdesign/init%28rawvalue%29.md)
  Creates a typeface design constant with the specified raw value.

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
- [UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [UIFontDescriptor.Class](./class.md)
  Constants that classify certain stylistic qualities of the font.
- [UIFontDescriptor.AttributeName](./attributename.md)
  Constants that describe font attributes.
- [UIFontDescriptor.FeatureKey](./featurekey.md)
  Keys for retrieving feature settings.
- [UIFontDescriptor.TraitKey](./traitkey.md)
  Keys for retrieving the font descriptor’s trait information.
- [UIFont.Weight](../uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](../uifont/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/systemdesign)*