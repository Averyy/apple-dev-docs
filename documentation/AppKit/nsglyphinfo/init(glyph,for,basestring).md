# init(glyph:for:baseString:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS

## Declaration

```swift
init?(glyph: NSGlyph, for font: NSFont, baseString string: String)
```

```objc
+ (NSGlyphInfo *) glyphInfoWithGlyph:(NSGlyph) glyph forFont:(NSFont *) font baseString:(NSString *) string;
```

## See Also

### Creating a glyph info object
- [init?(cgGlyph: CGGlyph, for: NSFont, baseString: String)](./init%28cgglyph,for,basestring%29.md)
  Creates a glyph info object from the specified glyph identifier and font informaton.
- [init?(CGGlyph: CGGlyph, forFont: NSFont, baseString: String)](./init%28cgglyph,forfont,basestring%29.md)
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [init?(glyphName: String, for: NSFont, baseString: String)](./init%28glyphname,for,basestring%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/init(glyph:for:basestring:))*