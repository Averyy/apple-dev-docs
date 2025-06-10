# characters

**Framework**: AppKit  
**Kind**: property

The text storage contents as an array of characters.

**Availability**:
- macOS ?+

## Declaration

```swift
var characters: [NSTextStorage] { get set }
```

#### Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly. For indexed access to characters, use `NSAttributedString`’s [`length`](https://developer.apple.com/documentation/Foundation/NSAttributedString/length) method to access the string, and `NSString`’s [`character(at:)`](https://developer.apple.com/documentation/Foundation/NSString/character(at:)) method to access the individual characters.

## See Also

- [var attributeRuns: [NSTextStorage]](nstextstorage/attributeruns.md)
  The text storage contents as an array of attribute runs.
- [var paragraphs: [NSTextStorage]](nstextstorage/paragraphs.md)
  The text storage contents as an array of paragraphs.
- [var words: [NSTextStorage]](nstextstorage/words.md)
  The text storage contents as an array of words.
- [var font: NSFont?](nstextstorage/font.md)
  The font for the text storage.
- [var foregroundColor: NSColor?](nstextstorage/foregroundcolor.md)
  The color for the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/characters)*