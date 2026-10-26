# UIFontDescriptor.SymbolicTraits

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that describe the stylistic aspects of a font.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct SymbolicTraits
```

```c
enum UIFontDescriptorSymbolicTraits : uint32_t;
```

#### Overview

The lower 16 bits represent the typeface, and the upper 16 bits describe appearance of the font. The font appearance information represented by the upper 16 bits of [`NSFontSymbolicTraits`](../../AppKit/nsfontsymbolictraits.md) can be used for stylistic font matching. [`UIFontDescriptor.Class`](./class.md) constants classify certain stylistic qualities of the font.

## Topics

### Font traits
- [static var traitItalic: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traititalic.md)
  The font’s style is italic.
- [static var traitBold: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traitbold.md)
  The font’s style is boldface.
- [static var traitExpanded: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traitexpanded.md)
  The font’s characters have an expanded width.
- [static var traitCondensed: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traitcondensed.md)
  The font’s characters have a condensed width.
- [static var traitMonoSpace: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traitmonospace.md)
  The font’s characters all have the same width.
- [static var traitVertical: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traitvertical.md)
  The font uses vertical glyph variants and metrics.
- [static var traitUIOptimized: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traituioptimized.md)
  The font synthesizes appropriate attributes for user interface rendering, such as in control titles, if necessary.
- [static var traitTightLeading: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traittightleading.md)
  The font uses a leading value that’s less than the default.
- [static var traitLooseLeading: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/traitlooseleading.md)
  The font uses a leading value that’s greater than the default.
- [static var classMask: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classmask.md)
  The font family class mask that you use to access font descriptor values.
- [static var classOldStyleSerifs: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classoldstyleserifs.md)
  The font’s characters include serifs, and reflect the Latin printing style of the 15th to 17th centuries.
- [static var classTransitionalSerifs: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classtransitionalserifs.md)
  The font’s characters include serifs, and reflect the Latin printing style of the 18th to 19th centuries.
- [static var classModernSerifs: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classmodernserifs.md)
  The font’s characters include serifs, and reflect the Latin printing style of the 20th century.
- [static var classClarendonSerifs: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classclarendonserifs.md)
  The font’s characters include variations of old style and transitional serifs.
- [static var classSlabSerifs: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classslabserifs.md)
  The font’s characters use square transitions, without brackets, between strokes and serifs.
- [static var classFreeformSerifs: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classfreeformserifs.md)
  The font’s characters include serifs, and don’t generally fit within other serif design classifications.
- [static var classSansSerif: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classsansserif.md)
  The font’s characters don’t have serifs.
- [static var classOrnamentals: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classornamentals.md)
  The font’s characters use highly decorated or stylized character shapes.
- [static var classScripts: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classscripts.md)
  The font’s characters simulate handwriting.
- [static var classSymbolic: UIFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classsymbolic.md)
  The font’s characters consist mainly of symbols rather than letters and numbers.
### Initializer
- [init(rawValue: UInt32)](./symbolictraits-swift.struct/init%28rawvalue%29.md)
  Creates a symbol traits structure with the specified raw value.
### Enumeration Cases
- [UIFontDescriptorClassUnknown](../uifontdescriptorsymbolictraits/uifontdescriptorclassunknown.md)
  The font has no design classification.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Fonts
- [Scaling fonts automatically](../scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Adding a custom font to your app](../adding-a-custom-font-to-your-app.md)
  Add a custom font to your app and use it in your app’s interface.
- [class UIFont](../uifont.md)
  An object that provides access to the font’s characteristics.
- [class UIFontDescriptor](../uifontdescriptor.md)
  A collection of attributes that describes a font.
- [class UIFontMetrics](../uifontmetrics.md)
  A utility object for obtaining custom fonts that scale to support Dynamic Type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/symbolictraits-swift.struct)*