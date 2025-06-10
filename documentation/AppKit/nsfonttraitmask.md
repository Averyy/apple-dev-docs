# NSFontTraitMask

**Framework**: AppKit  
**Kind**: struct

Constants for isolating specific traits of a font.

**Availability**:
- macOS ?+

## Declaration

```swift
struct NSFontTraitMask
```

#### Overview

[`NSFontManager`](nsfontmanager.md) categorizes fonts according to a small set of traits. You can convert fonts by adding and removing individual traits, and you can get a font with a specific combination of traits.

These pairs of traits are mutually exclusive:

- [`condensedFontMask`](nsfonttraitmask/condensedfontmask.md) and  [`expandedFontMask`](nsfonttraitmask/expandedfontmask.md)
- [`boldFontMask`](nsfonttraitmask/boldfontmask.md) and  [`unboldFontMask`](nsfonttraitmask/unboldfontmask.md)
- [`italicFontMask`](nsfonttraitmask/italicfontmask.md) and  [`unitalicFontMask`](nsfonttraitmask/unitalicfontmask.md)

## Topics

### Trait Masks
- [static var boldFontMask: NSFontTraitMask](nsfonttraitmask/boldfontmask.md)
  A mask that specifies a bold font.
- [static var compressedFontMask: NSFontTraitMask](nsfonttraitmask/compressedfontmask.md)
  A mask that specifies a compressed font.
- [static var condensedFontMask: NSFontTraitMask](nsfonttraitmask/condensedfontmask.md)
  A mask that specifies a condensed font.
- [static var expandedFontMask: NSFontTraitMask](nsfonttraitmask/expandedfontmask.md)
  A mask that specifies an expanded font.
- [static var fixedPitchFontMask: NSFontTraitMask](nsfonttraitmask/fixedpitchfontmask.md)
  A mask that specifies a fixed pitch font.
- [static var italicFontMask: NSFontTraitMask](nsfonttraitmask/italicfontmask.md)
  A mask that specifies an italic font.
- [static var narrowFontMask: NSFontTraitMask](nsfonttraitmask/narrowfontmask.md)
  A mask that specifies a narrow font.
- [static var nonStandardCharacterSetFontMask: NSFontTraitMask](nsfonttraitmask/nonstandardcharactersetfontmask.md)
  A mask that specifies a font containing a non-standard character set.
- [static var posterFontMask: NSFontTraitMask](nsfonttraitmask/posterfontmask.md)
  A mask that specifies a poster-style font.
- [static var smallCapsFontMask: NSFontTraitMask](nsfonttraitmask/smallcapsfontmask.md)
  A mask that specifies a small-caps font.
- [static var unboldFontMask: NSFontTraitMask](nsfonttraitmask/unboldfontmask.md)
  A mask that specifies a font that is not bold.
- [static var unitalicFontMask: NSFontTraitMask](nsfonttraitmask/unitalicfontmask.md)
  A mask that specifies a font that is not italic.
### Initializers
- [init(rawValue: UInt)](nsfonttraitmask/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class NSFont](nsfont.md)
  The representation of a font in an app.
- [class NSFontDescriptor](nsfontdescriptor.md)
  A dictionary of attributes that describe a font.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [class NSFontAssetRequest](nsfontassetrequest.md)
- [typealias NSFontSymbolicTraits](nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfonttraitmask)*