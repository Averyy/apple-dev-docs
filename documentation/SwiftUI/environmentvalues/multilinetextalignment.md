# multilineTextAlignment

**Framework**: Swiftui  
**Kind**: property

An environment value that indicates how a text view aligns its lines when the content wraps or contains newlines.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var multilineTextAlignment: TextAlignment { get set }
```

#### Discussion

Set this value for a view hierarchy by applying the [`multilineTextAlignment(_:)`](view/multilinetextalignment(_:).md) view modifier. Views in the hierarchy that display text, like [`Text`](text.md) or [`TextEditor`](texteditor.md), read the value from the environment and adjust their text alignment accordingly.

This value has no effect on a [`Text`](text.md) view that contains only one line of text, because a text view has a width that exactly matches the width of its widest line. If you want to align an entire text view rather than its contents, set the aligment of its container, like a [`VStack`](vstack.md) or a frame that you create with the [`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`](view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md) modifier.

> **Note**: You can use this value to control the alignment of a [`Text`](text.md) view that you create with the [`init(_:style:)`](text/init(_:style:).md) initializer to display localized dates and times, including when the view uses only a single line, but only when that view appears in a widget.

## See Also

- [func lineSpacing(CGFloat) -> some View](view/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [var lineSpacing: CGFloat](environmentvalues/linespacing.md)
  The distance in points between the bottom of one line fragment and the top of the next.
- [func multilineTextAlignment(TextAlignment) -> some View](view/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftUI/environmentvalues/multilinetextalignment)*