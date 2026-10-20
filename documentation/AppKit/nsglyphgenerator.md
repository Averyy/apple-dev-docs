# NSGlyphGenerator

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that performs the initial, nominal glyph generation phase in the layout process.

**Availability**:
- macOS

## Declaration

```swift
class NSGlyphGenerator
```

```objc
@interface NSGlyphGenerator : NSObject
```

#### Overview

The nominal glyph generation pass essentially generates one glyph per character; the typesetter may later make substitutions in the glyph stream, for example, changing an acute accent glyph followed by an “e” glyph into a single acute-accented “é” glyph.

[`NSGlyphGenerator`](./nsglyphgenerator.md) communicates via the [`NSGlyphStorage`](./nsglyphstorage.md) protocol. An example of a class that conforms to the protocol is [`NSLayoutManager`](./nslayoutmanager.md).

## Topics

### Obtaining a glyph generator
- [class var shared: NSGlyphGenerator](./nsglyphgenerator/shared.md)
  Returns a shared instance of `NSGlyphGenerator`.
### Generating glyphs
- [func generateGlyphs(for: any NSGlyphStorage, desiredNumberOfCharacters: Int, glyphIndex: UnsafeMutablePointer<Int>?, characterIndex: UnsafeMutablePointer<Int>?)](./nsglyphgenerator/generateglyphs%28for,desirednumberofcharacters,glyphindex,characterindex%29.md)
  Generates glyphs for the specified glyph storage object (`NSLayoutManager` by default).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Glyphs
- [typealias NSGlyph](./nsglyph.md)
  The type used to specify glyphs.
- [protocol NSGlyphStorage](./nsglyphstorage.md)
  A set of methods that a glyph storage object must implement to interact properly with [`NSGlyphGenerator`](./nsglyphgenerator.md).
- [class NSGlyphInfo](./nsglyphinfo.md)
  A glyph attribute in an attributed string.
- [Reserved Glyph Codes](./reserved-glyph-codes.md)
  These constants define reserved glyph codes.
- [enum NSFontRenderingMode](./nsfontrenderingmode.md)
  The font rendering mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphgenerator)*