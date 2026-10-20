# words

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text storage contents as an array of words.

**Availability**:
- macOS

## Declaration

```swift
var words: [NSTextStorage] { get set }
```

```objc
@property (copy) NSArray<NSTextStorage *> * words;
```

#### Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly.

## See Also

### Accessing scriptable properties
- [var attributeRuns: [NSTextStorage]](./attributeruns.md)
  The text storage contents as an array of attribute runs.
- [var paragraphs: [NSTextStorage]](./paragraphs.md)
  The text storage contents as an array of paragraphs.
- [var characters: [NSTextStorage]](./characters.md)
  The text storage contents as an array of characters.
- [var font: NSFont?](./font.md)
  The font for the text storage.
- [var foregroundColor: NSColor?](./foregroundcolor.md)
  The color for the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/words)*