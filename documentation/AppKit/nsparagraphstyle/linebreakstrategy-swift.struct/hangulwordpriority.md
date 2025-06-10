# hangulWordPriority

**Framework**: AppKit  
**Kind**: property

The text system prohibits breaking between Hangul characters.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static var hangulWordPriority: NSParagraphStyle.LineBreakStrategy { get }
```

#### Discussion

To avoid breaking between Hangul characters, this strategy is preferred for typesetting modern Korean documents that display UI strings.

## See Also

- [static var pushOut: NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.struct/pushout.md)
  The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.
- [static var standard: NSParagraphStyle.LineBreakStrategy](nsparagraphstyle/linebreakstrategy-swift.struct/standard.md)
  The text system uses the same configuration of line-break strategies that it uses for standard UI labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/linebreakstrategy-swift.struct/hangulwordpriority)*