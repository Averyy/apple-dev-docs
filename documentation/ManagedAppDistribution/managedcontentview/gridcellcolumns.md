# gridCellColumns(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Tells a view that acts as a cell in a grid to span the specified number of columns.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func gridCellColumns(_ count: Int) -> some View
```

#### Return Value

A view that occupies the specified number of columns in a grid row.

#### Discussion

By default, each view that you put into the content closure of a `GridRow` corresponds to exactly one column of the grid. Apply the `gridCellColumns(_:)` modifier to a view that you want to span more than one column, as in the following example of a typical macOS configuration view:

```None
Grid(alignment: .leadingFirstTextBaseline) {
    GridRow {
        Text("Regular font:")
            .gridColumnAlignment(.trailing)
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
            .gridCellColumns(2) // Span two columns.
    }
}
```

The `Toggle` in the example above spans the column that contains the font names and the column that contains the buttons:

> ❗ **Important**: When you tell a cell to span multiple columns, the grid changes the merged cell to use anchor alignment, rather than the usual alignment guides. For information about the behavior of anchor alignment, see `View/gridCellAnchor(_:)`.

When you tell a cell to span multiple columns, the grid changes the merged cell to use anchor alignment, rather than the usual alignment guides. For information about the behavior of anchor alignment, see `View/gridCellAnchor(_:)`.

As a convenience you can cause a view to span all of the `Grid` columns by placing the view directly in the content closure of the `Grid`, outside of a `GridRow`, and omitting the modifier. To do the opposite and include more than one view in a cell, group the views using an appropriate layout container, like an `HStack`, so that they act as a single view.

## Parameters

- `count`: The number of columns that the view should consume   when placed in a grid row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/gridcellcolumns(_:))*