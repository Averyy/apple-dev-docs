# standard

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The text system uses the same configuration of line-break strategies that it uses for standard UI labels.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static var standard: NSParagraphStyle.LineBreakStrategy { get }
```

```c
NSLineBreakStrategyStandard
```

#### Discussion

This strategy optimizes for displaying shorter strings that are common in UI labels. This strategy may be unsuitable for large amounts of text.

## See Also

### Getting the line-break styles
- [static var pushOut: NSParagraphStyle.LineBreakStrategy](./pushout.md)
  The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.
- [static var hangulWordPriority: NSParagraphStyle.LineBreakStrategy](./hangulwordpriority.md)
  The text system prohibits breaking between Hangul characters.
- [NSLineBreakStrategyNone](../../nslinebreakstrategy/nslinebreakstrategynone.md)
  The text system doesn’t use any line-break strategies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/linebreakstrategy-swift.struct/standard)*