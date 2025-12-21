# safeAreaBar(edge:alignment:spacing:content:)

**Framework**: SwiftUI  
**Kind**: method

Shows the specified content as a custom bar beside the modified view.

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
func safeAreaBar(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> some View) -> some View
```

#### Return Value

A new view that displays `content` beside the modified view, making space for the `content` view by horizontally insetting the modified view, adjusting the safe area and scroll edge effects to match.

#### Discussion

Similar to the [`safeAreaInset(edge:alignment:spacing:content:)`](view/safeareainset(edge:alignment:spacing:content:)-6gwby.md) modifier, the `content` view is anchored to the specified horizontal edge of the parent view and its width insets the safe area.

Additionally, it extends the edge effect of any scroll views affected by the inset safe area.

## Parameters

- `edge`: The horizontal edge of the view on which   is placed.
- `alignment`: The alignment guide used to position    vertically.
- `spacing`: Extra distance placed between the two views, or   nil to use the default amount of spacing.
- `content`: A view builder function providing the view to display as a   custom bar.

## See Also

- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](view/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollEdgeEffectHidden(Bool, for: Edge.Set) -> some View](view/scrolledgeeffecthidden(_:for:).md)
  Hides any scroll edge effects for scroll views within this hierarchy.
- [struct ScrollEdgeEffectStyle](scrolledgeeffectstyle.md)
  A structure that defines the style of pocket a scroll view will have.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/safeareabar(edge:alignment:spacing:content:))*