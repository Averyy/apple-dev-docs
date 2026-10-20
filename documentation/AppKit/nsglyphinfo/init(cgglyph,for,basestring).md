# init(cgGlyph:for:baseString:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a glyph info object from the specified glyph identifier and font informaton.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init?(cgGlyph glyph: CGGlyph, for font: NSFont, baseString string: String)
```

```objc
+ (NSGlyphInfo *) glyphInfoWithCGGlyph:(CGGlyph) glyph forFont:(NSFont *) font baseString:(NSString *) string;
```

#### Return Value

A glyph info object for the specified glyph or `nil` if the glyph information is not available.

## Parameters

- `glyph`: The requested [`CGGlyph`](../../CoreGraphics/cgglyph.md) object.
- `font`: The font containing the glyph.
- `string`: A string containing the character represented by the glyph.

## See Also

### Creating a glyph info object
- [init?(CGGlyph: CGGlyph, forFont: NSFont, baseString: String)](./init%28cgglyph,forfont,basestring%29.md)
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [init?(glyph: NSGlyph, for: NSFont, baseString: String)](./init%28glyph,for,basestring%29.md)
- [init?(glyphName: String, for: NSFont, baseString: String)](./init%28glyphname,for,basestring%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/init(cgglyph:for:basestring:))*