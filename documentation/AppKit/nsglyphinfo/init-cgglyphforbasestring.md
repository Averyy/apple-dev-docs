# init(cgGlyph:for:baseString:)

**Framework**: AppKit  
**Kind**: init

Creates a glyph info object from the specified glyph identifier and font informaton.

**Availability**:
- macOS 10.13+

## Declaration

```swift
init?(cgGlyph glyph: CGGlyph, for font: NSFont, baseString string: String)
```

#### Return Value

A glyph info object for the specified glyph or `nil` if the glyph information is not available.

## Parameters

- `glyph`: The requested   object.
- `font`: The font containing the glyph.
- `string`: A string containing the character represented by the glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphinfo/init(cgglyph:for:basestring:))*