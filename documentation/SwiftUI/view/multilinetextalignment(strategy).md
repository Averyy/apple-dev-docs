# multilineTextAlignment(strategy:)

**Framework**: SwiftUI  
**Kind**: method

A modifier for the default text alignment strategy in the view hierarchy.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func multilineTextAlignment(strategy: Text.AlignmentStrategy) -> some View
```

#### Discussion

To control the alignment explicitly at a view level, choose the [`layoutBased`](text/alignmentstrategy/layoutbased.md) mode and set the [`multilineTextAlignment`](environmentvalues/multilinetextalignment.md) to the appropriate value.

## See Also

- [func lineLimit(_:)](view/linelimit(_:).md)
  Sets to a closed range the number of lines that text can occupy in this view.
- [func lineLimit(Int, reservesSpace: Bool) -> some View](view/linelimit(_:reservesspace:).md)
  Sets a limit for the number of lines text can occupy in this view.
- [func lineSpacing(CGFloat) -> some View](view/linespacing(_:).md)
  Sets the amount of space between lines of text in this view.
- [func multilineTextAlignment(TextAlignment) -> some View](view/multilinetextalignment(_:).md)
  Sets the alignment of a text view that contains multiple lines of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/multilinetextalignment(strategy:))*