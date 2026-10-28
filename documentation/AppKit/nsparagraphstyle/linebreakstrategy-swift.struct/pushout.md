# pushOut

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var pushOut: NSParagraphStyle.LineBreakStrategy { get }
```

```c
NSLineBreakStrategyPushOut
```

## Discussion

To avoid an orphan word on the last line of a paragraph before a page break, the text system may extend individual lines by one or more words. Typically, the text system only pushes out the last line by one word.

## See Also

### Getting the line-break styles
- [static var hangulWordPriority: NSParagraphStyle.LineBreakStrategy](./hangulwordpriority.md)
  The text system prohibits breaking between Hangul characters.
- [static var standard: NSParagraphStyle.LineBreakStrategy](./standard.md)
  The text system uses the same configuration of line-break strategies that it uses for standard UI labels.
- [NSLineBreakStrategyNone](../../nslinebreakstrategy/nslinebreakstrategynone.md)
  The text system doesn’t use any line-break strategies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/linebreakstrategy-swift.struct/pushout)*