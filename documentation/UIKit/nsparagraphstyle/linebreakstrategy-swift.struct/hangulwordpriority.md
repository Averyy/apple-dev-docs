# hangulWordPriority

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The text system prohibits breaking between Hangul characters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var hangulWordPriority: NSParagraphStyle.LineBreakStrategy { get }
```

```c
NSLineBreakStrategyHangulWordPriority
```

#### Discussion

To avoid breaking between Hangul characters, this strategy is preferred for typesetting modern Korean documents that display UI strings.

## See Also

### Getting the line-break styles
- [static var pushOut: NSParagraphStyle.LineBreakStrategy](./pushout.md)
  The text system pushes out individual lines to avoid an orphan word on the last line of the paragraph.
- [static var standard: NSParagraphStyle.LineBreakStrategy](./standard.md)
  The text system uses the same configuration of line-break strategies that it uses for standard UI labels.
- [NSLineBreakStrategyNone](../../nslinebreakstrategy/nslinebreakstrategynone.md)
  The text system doesn’t use any line-break strategies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsparagraphstyle/linebreakstrategy-swift.struct/hangulwordpriority)*