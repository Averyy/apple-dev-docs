# containerCornerOffset(_:sizeToFit:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

## Discussion

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

- `edges`: The set of edges which the container view should add corner insets from.
- `sizeToFit`: A flag indicating when this view is offset off a corner inset whether its size should attempt to fit into its remaining space of the view or fill its original size.

## See Also

### Size
- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](./frame%28width,height,alignment%29.md)
  Positions this view within an invisible frame with the specified size.
- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](./frame%28depth,alignment%29.md)
  Positions this view within an invisible frame with the specified depth.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](./frame%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight,alignment%29.md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](./frame%28mindepth,idealdepth,maxdepth,alignment%29.md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](./containerrelativeframe%28_,alignment%29.md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](./containerrelativeframe%28_,alignment,_%29.md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](./containerrelativeframe%28_,count,span,spacing,alignment%29.md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func fixedSize() -> some View](./fixedsize%28%29.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](./fixedsize%28horizontal,vertical%29.md)
  Fixes this view at its ideal size in the specified dimensions.
- [func layoutPriority(Double) -> some View](./layoutpriority%28_%29.md)
  Sets the priority by which a parent layout should apportion space to this child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/containercorneroffset(_:sizetofit:))*