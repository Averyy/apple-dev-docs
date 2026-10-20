# NSMultibyteGlyphPacking

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

A constant for glyph packing.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```swift
enum NSMultibyteGlyphPacking
```

```c
enum NSMultibyteGlyphPacking : NSUInteger;
```

#### Overview

Cocoa stores all text data as Unicode. The text system converts Unicode into glyph IDs and places them in 1-, 2-, or 4-byte storage depending on the context. To render text, you must convert the storage into a format the text engine understands. The following constants describe the glyph packing schemes the text rendering engine can use. They are used to extract glyphs from a font for making a multibyte (or single-byte) array of glyphs for passing to an interpreter, such as the window server, which expects a big-endian multibyte stream (that is, “packed glyphs”) instead of a pure `NSGlyph` stream. They’re used by `glyphPacking`. With Quartz, the engine always expects the format to be in 2-byte short array, so `NSNativeShortGlyphPacking` is the only format currently in use.

## Topics

### Packing Options
- [NSMultibyteGlyphPacking.nativeShortGlyphPacking](./nsmultibyteglyphpacking/nativeshortglyphpacking.md)
  The native format for macOS.
### Initializers
- [init?(rawValue: UInt)](./nsmultibyteglyphpacking/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated enumerations
- [Glyph Attributes](./glyph-attributes.md)
  Attributes that are used only inside the glyph generation machinery, but must also be shared between components.
- [enum NSOpenGLGlobalOption](./nsopenglglobaloption.md)
  Constants that specify OpenGL options.
- [Data Entry Types](./data-entry-types.md)
  These constants specify how a cell formats numeric data.
- [Anonymous](./nsbuttontypes-anonymous.md)
- [Additional Writing Directions](./additional-writing-directions.md)
  Constants that specify additional options when setting the writing direction of attributed strings.
- [Return values for modal operations](./return-values-for-modal-operations.md)
  Historical return values for [`runModal(for:)`](./nsapplication/runmodal%28for%29.md) and [`runModalSession(_:)`](./nsapplication/runmodalsession%28_%29.md).
- [Tags of Views in the FontPanel](./tags-of-views-in-the-fontpanel.md)
  These constants are obsolete and should not be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmultibyteglyphpacking)*