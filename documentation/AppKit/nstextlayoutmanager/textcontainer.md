# textContainer

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text container object that provides geometric information for the layout destination.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var textContainer: NSTextContainer? { get set }
```

```objc
@property (strong, readwrite, nullable) NSTextContainer * textContainer;
```

## See Also

### Accessing the text storage
- [var textContentManager: NSTextContentManager?](./textcontentmanager.md)
  Returns the text content manager associated with this text layout manager.
- [var textSelectionNavigation: NSTextSelectionNavigation](./textselectionnavigation.md)
  Returns a text selection manager configured to have the text layout manager as its data source.
- [var textSelections: [NSTextSelection]](./textselections.md)
  An array of text selections associated by the text layout manager.
- [var usageBoundsForTextContainer: CGRect](./usageboundsfortextcontainer.md)
  Returns the usage bounds for the text container.
- [func enumerateTextSegments(in: NSTextRange, type: NSTextLayoutManager.SegmentType, options: NSTextLayoutManager.SegmentOptions, using: (NSTextRange?, CGRect, CGFloat, NSTextContainer) -> Bool)](./enumeratetextsegments%28in,type,options,using%29.md)
  Enumerates text segments of a specific type and in the text range you provide.
- [func replace(NSTextContentManager)](./replace%28_%29.md)
  Replaces the current text content manager with a new one you provide.
- [func replaceContents(in: NSTextRange, with: NSAttributedString)](./replacecontents%28in,with%29-2elb.md)
  Replaces content at the location you specify with an attributed string you provide.
- [func replaceContents(in: NSTextRange, with: [NSTextElement])](./replacecontents%28in,with%29-80j0b.md)
  Replaces content at the location you specify with the text elements string you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/textcontainer)*