# frame(depth:alignment:)

**Framework**: SwiftUI  
**Kind**: method

Positions this view within an invisible frame with the specified depth.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func frame(depth: CGFloat?, alignment: DepthAlignment = .center) -> some View
```

#### Return Value

A view with a fixed dimension of `depth` if non-`nil`.

#### Discussion

Use this method to specify a fixed size for a view’s depth. If you don’t specify a dimension, the resulting view assumes this view’s sizing behavior in depth.

## Parameters

- `depth`: A fixed depth for the resulting view. If   is  ,   the resulting view assumes this view’s sizing behavior.
- `alignment`: The alignment of this view inside the resulting view.    applies if this view is smaller than the size given by   the resulting frame.

## See Also

- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](view/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](view/frame(mindepth:idealdepth:maxdepth:alignment:).md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](view/containerrelativeframe(_:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](view/containerrelativeframe(_:alignment:_:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](view/containerrelativeframe(_:count:span:spacing:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func fixedSize() -> some View](view/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](view/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func layoutPriority(Double) -> some View](view/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/frame(depth:alignment:))*