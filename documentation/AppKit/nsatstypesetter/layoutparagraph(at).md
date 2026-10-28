# layoutParagraph(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Lays out glyphs in the current glyph range until the next paragraph separator is reached.

**Availability**:
- macOS

## Declaration

```swift
func layoutParagraph(at lineFragmentOrigin: UnsafeMutablePointer<NSPoint>) -> Int
```

```objc
- (NSUInteger) layoutParagraphAtPoint:(NSPoint *) lineFragmentOrigin;
```

## Discussion

The `lineFragmentOrigin` specifies the upper-left corner of line fragment rectangle. On return, `lineFragmentOrigin` contains the next origin. This method returns the next glyph index. Usually it’s the index right after the paragraph separator, but it can be inside the paragraph range if, for example, the end of the text container is reached before the paragraph separator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter/layoutparagraph(at:))*