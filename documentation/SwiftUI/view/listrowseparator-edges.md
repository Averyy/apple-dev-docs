# listRowSeparator(_:edges:)

**Framework**: SwiftUI  
**Kind**: method

Sets the display mode for the separator associated with this specific row.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func listRowSeparator(_ visibility: Visibility, edges: VerticalEdge.Set = .all) -> some View
```

#### Discussion

Separators can be presented above and below a row. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing [`List`](list.md). The list style is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose row separators are hidden:

```swift
List {
    ForEach(garage.cars) { car in
        Text(car.model)
            .listRowSeparator(.hidden)
    }
}
.listStyle(.grouped)
```

To change the color of a row separators, use [`listRowSeparatorTint(_:edges:)`](view/listrowseparatortint(_:edges:).md). To hide or change the tint color for a section separators, use [`listSectionSeparator(_:edges:)`](view/listsectionseparator(_:edges:).md) and [`listSectionSeparatorTint(_:edges:)`](view/listsectionseparatortint(_:edges:).md).

## Parameters

- `visibility`: The visibility of this row’s separators.
- `edges`: The set of row edges for which this preference applies.   The list style might already decide to not display separators for   some edges, typically the top edge. The default is   .

## See Also

- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listrowseparator(_:edges:))*