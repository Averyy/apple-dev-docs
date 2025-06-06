# gridCellUnsizedAxes(_:)

**Framework**: SwiftUI  
**Kind**: method

Asks grid layouts not to offer the view extra size in the specified axes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func gridCellUnsizedAxes(_ axes: Axis.Set) -> some View
```

#### Return Value

A view that doesn’t ask an enclosing grid for extra size in one or more axes.

#### Discussion

Use this modifier to prevent a flexible view from taking more space on the specified axes than the other cells in a row or column require. For example, consider the following [`Grid`](grid.md) that places a [`Divider`](divider.md) between two rows of content:

```swift
Grid {
    GridRow {
        Text("Hello")
        Image(systemName: "globe")
    }
    Divider()
    GridRow {
        Image(systemName: "hand.wave")
        Text("World")
    }
}
```

The text and images all have ideal widths for their content. However, because a divider takes as much space as its parent offers, the grid fills the width of the display, expanding all the other cells to match:

![A screenshot of items arranged in a grid. The upper-left](https://docs-assets.developer.apple.com/published/9d53482162b4c1faf9ae7a965e68dde7/View-gridCellUnsizedAxes-1-iOS%402x.png)

You can prevent the grid from giving the divider more width than the other cells require by adding the modifier with the [`Axis.horizontal`](axis/horizontal.md) parameter:

```swift
Divider()
    .gridCellUnsizedAxes(.horizontal)
```

This restores the grid to the width that it would have without the divider:

![A screenshot of items arranged in a grid. The upper-left](https://docs-assets.developer.apple.com/published/c84de76b8879483c74c13957261c3438/View-gridCellUnsizedAxes-2-iOS%402x.png)

## Parameters

- `axes`: The dimensions in which the grid shouldn’t offer the view a   share of any available space. This prevents a flexible view like a   ,  , or   from defining the size of   a row or column.

## See Also

- [struct Grid](grid.md)
  A container view that arranges other views in a two dimensional layout.
- [struct GridRow](gridrow.md)
  A horizontal row in a two dimensional grid container.
- [func gridCellColumns(Int) -> some View](view/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellAnchor(UnitPoint) -> some View](view/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridColumnAlignment(HorizontalAlignment) -> some View](view/gridcolumnalignment(_:).md)
  Overrides the default horizontal alignment of the grid column that the view appears in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/gridcellunsizedaxes(_:))*