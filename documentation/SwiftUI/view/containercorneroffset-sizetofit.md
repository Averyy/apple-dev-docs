# containerCornerOffset(_:sizeToFit:)

**Framework**: SwiftUI  
**Kind**: method

Adjusts the view’s layout to avoid the container view’s corner insets for the specified edges.

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
func containerCornerOffset(_ edges: Edge.Set, sizeToFit: Bool = false) -> some View
```

#### Discussion

Use this modifier when you would like the view’s layout to adapt to avoid the container view’s corner insets for a set of edges. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations. When a specific edge is provided the view is positioned to avoid insets from only the corners of that edge. When multiple corner edges overlap in the same axis the view will be positioned off the larger overlapping inset.

```swift
DrawingCanvasView(canvas: $canvas)
    .ignoresSafeArea()
    .overlay(alignment: .topLeading) {
        DrawingToolPaletteView(tool: $selectedTool)
            .containerCornerOffset(.horizontal)
    }
```

The modifier provides a `sizeToFit` parameter to indicate how the view should be sized when it has been offset from a corner inset. By default, `false` is provided, and the content’s size will be unchanged, only the position of the view’s content will be offset. When `true`, the content will attempt to size itself with a proposal using the remaining size of the original view subtracted from the overlapping corner insets.

## Parameters

- `edges`: The set of edges which the container view should add corner   insets from.
- `sizeToFit`: A flag indicating when this view is offset off a   corner inset whether its size should attempt to fit into its   remaining space of the view or fill its original size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/containercorneroffset(_:sizetofit:))*