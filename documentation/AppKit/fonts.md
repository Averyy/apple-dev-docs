# Fonts

**Framework**: AppKit

Manage the fonts used to display text.

#### Overview

The [`NSFont`](nsfont.md) and [`NSFontManager`](nsfontmanager.md) classes encapsulate and manage font families, sizes, and variations. The [`NSFont`](nsfont.md) class defines a single object for each distinct font; for efficiency, these objects, which can be rather large, are shared by all the objects in your app. The [`NSFontPanel`](nsfontpanel.md) class defines the font specification panel that’s presented to the user.

## Topics

### Font Data
- [class NSFont](nsfont.md)
  The representation of a font in an app.
- [class NSFontDescriptor](nsfontdescriptor.md)
  A dictionary of attributes that describe a font.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [class NSFontAssetRequest](nsfontassetrequest.md)
- [typealias NSFontSymbolicTraits](nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.
### Management
- [class NSFontManager](nsfontmanager.md)
  The center of activity for the font-conversion system.
- [class NSFontCollection](nsfontcollection.md)
  A font collection, which is a group of font descriptors taken together as a single object.
- [class NSMutableFontCollection](nsmutablefontcollection.md)
  A mutable collection of font descriptors taken together as a single object.
- [struct NSFontCollectionOptions](nsfontcollectionoptions.md)
  Constants that support font collection management.

## See Also

- [Text Display](text-display.md)
  Display text and check spelling.
- [TextKit](textkit.md)
  Manage text storage and perform custom layout of text-based content in your app’s views.
- [Writing Tools](writing-tools.md)
  Add support for Writing Tools to your app’s text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/fonts)*