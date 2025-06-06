# gridColumnAlignment(_:)

**Framework**: RealityKit  
**Kind**: method

Overrides the default horizontal alignment of the grid column that the view appears in.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func gridColumnAlignment(_ guide: HorizontalAlignment) -> some View
```

#### Return Value

A view that uses the specified horizontal alignment, and that causes all cells in the same column of a grid to use the same alignment.

#### Discussion

You set a default alignment for the cells in a grid in both vertical and horizontal dimensions when you create the grid with the `Grid/init(alignment:horizontalSpacing:verticalSpacing:content:)` initializer. However, you can use the `gridColumnAlignment(_:)` modifier to override the horizontal alignment of a column within the grid. The following example sets a grid’s alignment to `Alignment/leadingFirstTextBaseline`, and then sets the first column to use `HorizontalAlignment/trailing` alignment:

```None
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

Add the modifier to only one cell in a column. The grid automatically aligns all cells in that column the same way. You get undefined behavior if you apply different alignments to different cells in the same column.

To override row alignment, see `GridRow/init(alignment:content:)`. To override alignment for a single cell, see `View/gridCellAnchor(_:)`.

## Parameters

- `guide`: The   guide to use for the grid   column that the view appears in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/gridcolumnalignment(_:))*