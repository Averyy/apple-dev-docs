# enumerateTextSegments(in:type:options:using:)

**Framework**: UIKit  
**Kind**: method

Enumerates text segments of a specific type and in the text range you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateTextSegments(in textRange: NSTextRange, type: NSTextLayoutManager.SegmentType, options: NSTextLayoutManager.SegmentOptions = [], using block: (NSTextRange?, CGRect, CGFloat, NSTextContainer) -> Bool)
```

#### Discussion

A text segment is a logically and visually contiguous portion of the text content inside a line fragment that you specify with a single text range. The framework enumerates the segments visually from left to right. Returning `false` breaks out of the enumeration.

## Parameters

- `textRange`: The range as an  .
- `type`: One of the available   values.
- `options`: One or more of the   options.
- `block`: A closure you provide to determine if the enumeration finishes early.

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
- [func replace(NSTextContentManager)](nstextlayoutmanager/replace(_:).md)
  Replaces the current text content manager with a new one you provide.
- [func replaceContents(in: NSTextRange, with: NSAttributedString)](nstextlayoutmanager/replacecontents(in:with:)-2elb.md)
  Replaces content at the location you specify with an attributed string you provide.
- [func replaceContents(in: NSTextRange, with: [NSTextElement])](nstextlayoutmanager/replacecontents(in:with:)-80j0b.md)
  Replaces content at the location you specify with the text elements string you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanager/enumeratetextsegments(in:type:options:using:))*