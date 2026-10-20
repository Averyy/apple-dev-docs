# textView(_:writingToolsIgnoredRangesInEnclosingRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 15.0+

## Declaration

```swift
@MainActor
optional func textView(_ textView: NSTextView, writingToolsIgnoredRangesInEnclosingRange enclosingRange: NSRange) -> [NSValue]
```

```objc
- (NSArray<NSValue *> *) textView:(NSTextView *) textView writingToolsIgnoredRangesInEnclosingRange:(NSRange) enclosingRange;
```

## Mentions

- [Customizing Writing Tools behavior for AppKit views](../customizing-writing-tools-behavior-for-system-views.md)

## See Also

### Responding to writing tools interactions
- [func textViewWritingToolsWillBegin(NSTextView)](./textviewwritingtoolswillbegin%28_%29.md)
- [func textViewWritingToolsDidEnd(NSTextView)](./textviewwritingtoolsdidend%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewdelegate/textview(_:writingtoolsignoredrangesinenclosingrange:))*