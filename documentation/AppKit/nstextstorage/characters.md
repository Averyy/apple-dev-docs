# characters

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text storage contents as an array of characters.

**Availability**:
- macOS

## Declaration

```swift
var characters: [NSTextStorage] { get set }
```

```objc
@property (copy) NSArray<NSTextStorage *> * characters;
```

#### Discussion

Unless you’re dealing with scriptability, you shouldn’t use or modify this property directly. For indexed access to characters, use `NSAttributedString`’s [`length`](../../Foundation/nsattributedstring/length.md) method to access the string, and `NSString`’s [`character(at:)`](../../Foundation/nsstring/character%28at%29.md) method to access the individual characters.

## See Also

### Accessing scriptable properties
- [var attributeRuns: [NSTextStorage]](./attributeruns.md)
  The text storage contents as an array of attribute runs.
- [var paragraphs: [NSTextStorage]](./paragraphs.md)
  The text storage contents as an array of paragraphs.
- [var words: [NSTextStorage]](./words.md)
  The text storage contents as an array of words.
- [var font: NSFont?](./font.md)
  The font for the text storage.
- [var foregroundColor: NSColor?](./foregroundcolor.md)
  The color for the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/characters)*