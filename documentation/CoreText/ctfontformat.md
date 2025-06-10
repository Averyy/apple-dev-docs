# CTFontFormat

**Framework**: Core Text  
**Kind**: enum

The recognized format of the font.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CTFontFormat
```

#### Overview

Use the values of this enumeration for [`kCTFontFormatAttribute`](kctfontformatattribute.md).

## Topics

### Font Formats
- [CTFontFormat.unrecognized](ctfontformat/unrecognized.md)
  The font is not a recognized format.
- [CTFontFormat.openTypePostScript](ctfontformat/opentypepostscript.md)
  The font is an OpenType format containing PostScript data.
- [CTFontFormat.openTypeTrueType](ctfontformat/opentypetruetype.md)
  The font is an OpenType format containing TrueType data.
- [CTFontFormat.trueType](ctfontformat/truetype.md)
  The font is a recognized TrueType format.
- [CTFontFormat.postScript](ctfontformat/postscript.md)
  The font is a recognized PostScript format.
- [CTFontFormat.bitmap](ctfontformat/bitmap.md)
  The font is a bitmap-only format.
### Initializers
- [init?(rawValue: UInt32)](ctfontformat/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let kCTFontFormatAttribute: CFString](kctfontformatattribute.md)
  The recognized format of the font.
- [Font Attributes](font-attributes.md)
  The keys for accessing font attributes from a font descriptor.
- [enum CTFontOrientation](ctfontorientation.md)
  The intended rendering orientation of the font for obtaining glyph metrics.
- [typealias CTFontPriority](ctfontpriority.md)
  The priority of font descriptors when resolving duplicates and sorting match results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontformat)*