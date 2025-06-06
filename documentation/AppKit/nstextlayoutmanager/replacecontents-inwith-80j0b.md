# replaceContents(in:with:)

**Framework**: AppKit  
**Kind**: method

Replaces content at the location you specify with the text elements string you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func replaceContents(in range: NSTextRange, with textElements: [NSTextElement])
```

## Parameters

- `range`: The range of the content to replace.
- `textElements`: An array of text elements.

## See Also

- [var textContentManager: NSTextContentManager?](nstextlayoutmanager/textcontentmanager.md)
  Returns the text content manager associated with this text layout manager.
- [var textContainer: NSTextContainer?](nstextlayoutmanager/textcontainer.md)
  The text container object that provides geometric information for the layout destination.
- [var textSelectionNavigation: NSTextSelectionNavigation](nstextlayoutmanager/textselectionnavigation.md)
  Returns a text selection manager configured to have the text layout manager as its data source.
- [var textSelections: [NSTextSelection]](nstextlayoutmanager/textselections.md)
  An array of text selections associated by the text layout manager.
- [var usageBoundsForTextContainer: CGRect](nstextlayoutmanager/usageboundsfortextcontainer.md)
  Returns the usage bounds for the text container.
- [func enumerateTextSegments(in: NSTextRange, type: NSTextLayoutManager.SegmentType, options: NSTextLayoutManager.SegmentOptions, using: (NSTextRange?, CGRect, CGFloat, NSTextContainer) -> Bool)](nstextlayoutmanager/enumeratetextsegments(in:type:options:using:).md)
  Enumerates text segments of a specific type and in the text range you provide.
- [func replace(NSTextContentManager)](nstextlayoutmanager/replace(_:).md)
  Replaces the current text content manager with a new one you provide.
- [func replaceContents(in: NSTextRange, with: NSAttributedString)](nstextlayoutmanager/replacecontents(in:with:)-2elb.md)
  Replaces content at the location you specify with an attributed string you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/replacecontents(in:with:)-80j0b)*