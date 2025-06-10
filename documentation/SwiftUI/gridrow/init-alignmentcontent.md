# init(alignment:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a horizontal row of child views in a grid.

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
init(alignment: VerticalAlignment? = nil, @ViewBuilder content: () -> Content)
```

#### Discussion

Use this initializer to create a [`GridRow`](gridrow.md) inside of a [`Grid`](grid.md). Provide a content closure that defines the cells of the row, and optionally customize the vertical alignment of content within each cell. The following example customizes the vertical alignment of the cells in the first and third rows:

```swift
Grid(alignment: .trailing) {
    GridRow(alignment: .top) { // Use top vertical alignment.
        Text("Top")
        Color.red.frame(width: 1, height: 50)
        Color.blue.frame(width: 50, height: 1)
    }
    GridRow { // Use the default (center) alignment.
        Text("Center")
        Color.red.frame(width: 1, height: 50)
        Color.blue.frame(width: 50, height: 1)
    }
    GridRow(alignment: .bottom) { // Use bottom vertical alignment.
        Text("Bottom")
        Color.red.frame(width: 1, height: 50)
        Color.blue.frame(width: 50, height: 1)
    }
}
```

The example above specifies [`trailing`](alignment/trailing.md) alignment for the grid, which is composed of [`center`](verticalalignment/center.md) vertical alignment and [`trailing`](horizontalalignment/trailing.md) horizontal alignment. The middle row relies on the center vertical alignment, but the other two rows specify custom vertical alignments:

![A grid with three rows and three columns. Scanning from top to bottom,](https://docs-assets.developer.apple.com/published/09f1e686a052f81a8774eb3266637e3f/GridRow-init-1-iOS%402x.png)

> ❗ **Important**: A grid row behaves like a [`Group`](group.md) if you create it outside of a grid.

To override column alignment, use [`gridColumnAlignment(_:)`](view/gridcolumnalignment(_:).md). To override alignment for a single cell, use [`gridCellAnchor(_:)`](view/gridcellanchor(_:).md).

## Parameters

- `alignment`: An optional   for the row. If you   don’t specify a value, the row uses the vertical alignment component   of the   parameter that you specify in the grid’s     initializer, which is   by default.
- `content`: The builder closure that contains the child views. Each   view in the closure implicitly maps to a cell in the grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gridrow/init(alignment:content:))*