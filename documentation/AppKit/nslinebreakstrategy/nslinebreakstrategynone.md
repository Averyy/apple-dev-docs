# NSLineBreakStrategyNone

**Framework**: AppKit  
**Kind**: case  
**Role**: Enumeration Case

The text system doesn’t use any line-break strategies.

**Availability**:
- macOS 10.11+

## Declaration

```c
NSLineBreakStrategyNone
```

## See Also

### Getting the line-break styles
- [static var pushOut: NSParagraphStyle.LineBreakStrategy](../nsparagraphstyle/linebreakstrategy-swift.struct/pushout.md)
  The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.
- [static var hangulWordPriority: NSParagraphStyle.LineBreakStrategy](../nsparagraphstyle/linebreakstrategy-swift.struct/hangulwordpriority.md)
  The text system prohibits breaking between Hangul characters.
- [static var standard: NSParagraphStyle.LineBreakStrategy](../nsparagraphstyle/linebreakstrategy-swift.struct/standard.md)
  The text system uses the same configuration of line-break strategies that it uses for standard UI labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslinebreakstrategy/nslinebreakstrategynone)*