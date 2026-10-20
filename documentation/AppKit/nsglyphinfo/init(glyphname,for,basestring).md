# init(glyphName:for:baseString:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS

## Declaration

```swift
init?(glyphName: String, for font: NSFont, baseString string: String)
```

```objc
+ (NSGlyphInfo *) glyphInfoWithGlyphName:(NSString *) glyphName forFont:(NSFont *) font baseString:(NSString *) string;
```

## See Also

### Creating a glyph info object
- [init?(cgGlyph: CGGlyph, for: NSFont, baseString: String)](./init%28cgglyph,for,basestring%29.md)
  Creates a glyph info object from the specified glyph identifier and font informaton.
- [init?(CGGlyph: CGGlyph, forFont: NSFont, baseString: String)](./init%28cgglyph,forfont,basestring%29.md)
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [init?(glyph: NSGlyph, for: NSFont, baseString: String)](./init%28glyph,for,basestring%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/init(glyphname:for:basestring:))*