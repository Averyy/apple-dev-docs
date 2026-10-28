# paragraphs

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text storage contents as an array of paragraphs.

**Availability**:
- macOS

## Declaration

```swift
var paragraphs: [NSTextStorage] { get set }
```

```objc
@property (copy) NSArray<NSTextStorage *> * paragraphs;
```

## Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly.

## See Also

### Accessing scriptable properties
- [var attributeRuns: [NSTextStorage]](./attributeruns.md)
  The text storage contents as an array of attribute runs.
- [var words: [NSTextStorage]](./words.md)
  The text storage contents as an array of words.
- [var characters: [NSTextStorage]](./characters.md)
  The text storage contents as an array of characters.
- [var font: NSFont?](./font.md)
  The font for the text storage.
- [var foregroundColor: NSColor?](./foregroundcolor.md)
  The color for the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/paragraphs)*