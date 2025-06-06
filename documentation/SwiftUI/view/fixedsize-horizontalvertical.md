# fixedSize(horizontal:vertical:)

**Framework**: SwiftUI  
**Kind**: method

Fixes this view at its ideal size in the specified dimensions.

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
nonisolated
func fixedSize(horizontal: Bool, vertical: Bool) -> some View
```

#### Return Value

A view that fixes this view at its ideal size in the dimensions specified by `horizontal` and `vertical`.

#### Discussion

This function behaves like [`fixedSize()`](view/fixedsize().md), except with `fixedSize(horizontal:vertical:)` the fixing of the axes can be optionally specified in one or both dimensions. For example, if you horizontally fix a text view before wrapping it in the frame view, you’re telling the text view to maintain its ideal . The view calculates this to be the space needed to represent the entire string.

```swift
Text("A single line of text, too long to fit in a box.")
    .fixedSize(horizontal: true, vertical: false)
    .frame(width: 200, height: 200)
    .border(Color.gray)
```

This can result in the view exceeding the parent’s bounds, which may or may not be the effect you want.

![A screenshot showing a text view exceeding the bounds of its](https://docs-assets.developer.apple.com/published/39fd04b5cd61b452f33e4b492d96759c/SwiftUI-View-fixedSize-3%402x.png)

## Parameters

- `horizontal`: A Boolean value that indicates whether to fix the width   of the view.
- `vertical`: A Boolean value that indicates whether to fix the height   of the view.

## See Also

- [func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some View](view/frame(width:height:alignment:).md)
  Positions this view within an invisible frame with the specified size.
- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](view/frame(depth:alignment:).md)
  Positions this view within an invisible frame with the specified depth.
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
- [func layoutPriority(Double) -> some View](view/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fixedsize(horizontal:vertical:))*