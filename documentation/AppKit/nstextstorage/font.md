# font

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The font for the text storage.

**Availability**:
- macOS

## Declaration

```swift
var font: NSFont? { get set }
```

```objc
@property (strong, nullable) NSFont * font;
```

## Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly.

## See Also

### Accessing scriptable properties
- [var attributeRuns: [NSTextStorage]](./attributeruns.md)
  The text storage contents as an array of attribute runs.
- [var paragraphs: [NSTextStorage]](./paragraphs.md)
  The text storage contents as an array of paragraphs.
- [var words: [NSTextStorage]](./words.md)
  The text storage contents as an array of words.
- [var characters: [NSTextStorage]](./characters.md)
  The text storage contents as an array of characters.
- [var foregroundColor: NSColor?](./foregroundcolor.md)
  The color for the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/font)*