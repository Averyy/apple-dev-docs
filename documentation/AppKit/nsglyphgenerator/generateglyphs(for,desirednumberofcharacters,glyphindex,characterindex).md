# generateGlyphs(for:desiredNumberOfCharacters:glyphIndex:characterIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Generates glyphs for the specified glyph storage object (`NSLayoutManager` by default).

**Availability**:
- macOS

## Declaration

```swift
func generateGlyphs(for glyphStorage: any NSGlyphStorage, desiredNumberOfCharacters nChars: Int, glyphIndex: UnsafeMutablePointer<Int>?, characterIndex charIndex: UnsafeMutablePointer<Int>?)
```

```objc
- (void) generateGlyphsForGlyphStorage:(id<NSGlyphStorage>) glyphStorage desiredNumberOfCharacters:(NSUInteger) nChars glyphIndex:(NSUInteger *) glyphIndex characterIndex:(NSUInteger *) charIndex;
```

#### Discussion

Generates glyphs for the glyph storage object specified by `glyphStorage`, beginning with the character at `charIndex` and continuing for `nChars` characters. The `glyphIndex` specifies the index of the first glyph generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsglyphgenerator/generateglyphs(for:desirednumberofcharacters:glyphindex:characterindex:))*