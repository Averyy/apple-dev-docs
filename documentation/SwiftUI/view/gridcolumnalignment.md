# gridColumnAlignment(_:)

**Framework**: SwiftUI  
**Kind**: method

Overrides the default horizontal alignment of the grid column that the view appears in.

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
func gridColumnAlignment(_ guide: HorizontalAlignment) -> some View
```

#### Return Value

A view that uses the specified horizontal alignment, and that causes all cells in the same column of a grid to use the same alignment.

#### Discussion

You set a default alignment for the cells in a grid in both vertical and horizontal dimensions when you create the grid with the [`init(alignment:horizontalSpacing:verticalSpacing:content:)`](grid/init(alignment:horizontalspacing:verticalspacing:content:).md) initializer. However, you can use the `gridColumnAlignment(_:)` modifier to override the horizontal alignment of a column within the grid. The following example sets a grid’s alignment to [`leadingFirstTextBaseline`](alignment/leadingfirsttextbaseline.md), and then sets the first column to use [`trailing`](horizontalalignment/trailing.md) alignment:

```swift
Grid(alignment: .leadingFirstTextBaseline) {
    GridRow {
        Text("Regular font:")
            .gridColumnAlignment(.trailing) // Align the entire first column.
        Text("Helvetica 12")
        Button("Select...") { }
    }
    GridRow {
        Text("Fixed-width font:")
        Text("Menlo Regular 11")
        Button("Select...") { }
    }
    GridRow {
        Color.clear
            .gridCellUnsizedAxes([.vertical, .horizontal])
        Toggle("Use fixed-width font for new documents", isOn: $isOn)
            .gridCellColumns(2)
    }
}
```

This creates the layout of a typical macOS configuration view, with the trailing edge of the first column flush with the leading edge of the second column:

![A screenshot of a configuration view, arranged in a grid. The grid](https://docs-assets.developer.apple.com/published/4f5b4b93d67b82887d0e3b515f084470/View-gridColumnAlignment-1-macOS%402x.png)

Add the modifier to only one cell in a column. The grid automatically aligns all cells in that column the same way. You get undefined behavior if you apply different alignments to different cells in the same column.

To override row alignment, see [`init(alignment:content:)`](gridrow/init(alignment:content:).md). To override alignment for a single cell, see [`gridCellAnchor(_:)`](view/gridcellanchor(_:).md).

## Parameters

- `guide`: The   guide to use for the grid   column that the view appears in.

## See Also

- [struct Grid](grid.md)
  A container view that arranges other views in a two dimensional layout.
- [struct GridRow](gridrow.md)
  A horizontal row in a two dimensional grid container.
- [func gridCellColumns(Int) -> some View](view/gridcellcolumns(_:).md)
  Tells a view that acts as a cell in a grid to span the specified number of columns.
- [func gridCellAnchor(UnitPoint) -> some View](view/gridcellanchor(_:).md)
  Specifies a custom alignment anchor for a view that acts as a grid cell.
- [func gridCellUnsizedAxes(Axis.Set) -> some View](view/gridcellunsizedaxes(_:).md)
  Asks grid layouts not to offer the view extra size in the specified axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/gridcolumnalignment(_:))*