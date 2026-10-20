# NSFontDescriptor.SymbolicTraits

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A symbolic description of the stylistic aspects of a font.

**Availability**:
- macOS

## Declaration

```swift
struct SymbolicTraits
```

```c
enum NSFontDescriptorSymbolicTraits : uint32_t;
```

## Topics

### Symbolic Traits
- [static var italic: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/italic.md)
  The font’s style is italic.
- [static var bold: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/bold.md)
  The font’s style is boldface.
- [static var expanded: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/expanded.md)
  The font’s characters have an expanded width.
- [static var condensed: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/condensed.md)
  The font’s characters have a condensed width.
- [static var monoSpace: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/monospace.md)
  The font’s characters all have the same width.
- [static var vertical: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/vertical.md)
  The font uses vertical glyph variants and metrics.
- [static var UIOptimized: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/uioptimized.md)
  The font synthesizes appropriate attributes for user interface rendering, such as in control titles, if necessary.
- [static var tightLeading: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/tightleading.md)
  The font uses a leading value that’s less than the default.
- [static var looseLeading: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/looseleading.md)
  The font uses a leading value that’s greater than the default.
- [static var classMask: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classmask.md)
  The font family class mask that you use to access font descriptor values.
- [static var classOldStyleSerifs: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classoldstyleserifs.md)
  The font’s characters include serifs, and reflect the Latin printing style of the 15th to 17th centuries.
- [static var classTransitionalSerifs: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classtransitionalserifs.md)
  The font’s characters include serifs, and reflect the Latin printing style of the 18th to 19th centuries.
- [static var classModernSerifs: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classmodernserifs.md)
  The font’s characters include serifs, and reflect the Latin printing style of the 20th century.
- [static var classClarendonSerifs: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classclarendonserifs.md)
  The font’s characters include variations of old style and transitional serifs.
- [static var classSlabSerifs: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classslabserifs.md)
  The font’s characters use square transitions, without brackets, between strokes and serifs.
- [static var classFreeformSerifs: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classfreeformserifs.md)
  The font’s characters include serifs, and don’t generally fit within other serif design classifications.
- [static var classSansSerif: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classsansserif.md)
  The font’s characters don’t have serifs.
- [static var classOrnamentals: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classornamentals.md)
  The font’s characters use highly decorated or stylized character shapes.
- [static var classScripts: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classscripts.md)
  The font’s characters simulate handwriting.
- [static var classSymbolic: NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct/classsymbolic.md)
  The font’s characters consist mainly of symbols rather than letters and numbers.
### Initializers
- [init(rawValue: UInt32)](./symbolictraits-swift.struct/init%28rawvalue%29.md)

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

### Related Documentation
- [UIFontDescriptor.SymbolicTraits](../../UIKit/uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
### Font Data
- [class NSFont](../nsfont.md)
  The representation of a font in an app.
- [class NSFontDescriptor](../nsfontdescriptor.md)
  A dictionary of attributes that describe a font.
- [struct NSFontTraitMask](../nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [typealias NSFontFamilyClass](../nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [class NSFontAssetRequest](../nsfontassetrequest.md)
- [typealias NSFontSymbolicTraits](../nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/symbolictraits-swift.struct)*