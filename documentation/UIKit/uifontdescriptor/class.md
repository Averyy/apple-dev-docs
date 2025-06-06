# UIFontDescriptor.Class

**Framework**: UIKit  
**Kind**: typealias

Constants that classify certain stylistic qualities of the font.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
typealias Class = Int
```

#### Discussion

These values correspond closely to the font class values in the OpenType OS/2 table. The class values are bundled in the upper four bits of the [`UIFontDescriptor.SymbolicTraits`](uifontdescriptor/symbolictraits-swift.struct.md) and can be accessed through [`classMask`](uifontdescriptor/symbolictraits-swift.struct/classmask.md). For additional information about the specific meaning of each identifier, refer to the OpenType specification.

## See Also

- [UIFont.TextStyle](uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
- [UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign.md)
  Constants that describe the system-defined typeface designs.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [UIFontDescriptor.AttributeName](uifontdescriptor/attributename.md)
  Constants that describe font attributes.
- [UIFontDescriptor.FeatureKey](uifontdescriptor/featurekey.md)
  Keys for retrieving feature settings.
- [UIFontDescriptor.TraitKey](uifontdescriptor/traitkey.md)
  Keys for retrieving the font descriptor’s trait information.
- [UIFont.Weight](uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](uifont/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/class)*