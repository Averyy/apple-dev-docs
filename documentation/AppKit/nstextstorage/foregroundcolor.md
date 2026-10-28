# foregroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color for the text.

**Availability**:
- macOS

## Declaration

```swift
var foregroundColor: NSColor? { get set }
```

```objc
@property (strong, nullable) NSColor * foregroundColor;
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
- [var font: NSFont?](./font.md)
  The font for the text storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/foregroundcolor)*