# listSectionSeparator(_:edges:)

**Framework**: SwiftUI  
**Kind**: method

Sets whether to hide the separator associated with a list section.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func listSectionSeparator(_ visibility: Visibility, edges: VerticalEdge.Set = .all) -> some View
```

#### Discussion

Separators can be presented above and below a section. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing [`List`](list.md). The list style is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose bottom sections separator are hidden:

```swift
List {
    ForEach(garage) { garage in
        Section(header: Text(garage.location)) {
            ForEach(garage.cars) { car in
                Text(car.model)
                    .listRowSeparatorTint(car.brandColor)
            }
        }
        .listSectionSeparator(.hidden, edges: .bottom)
    }
}
.listStyle(.grouped)
```

To change the visibility and tint color for a row separator, use [`listRowSeparator(_:edges:)`](view/listrowseparator(_:edges:).md) and [`listRowSeparatorTint(_:edges:)`](view/listrowseparatortint(_:edges:).md). To set the tint color for a section separator, use [`listSectionSeparatorTint(_:edges:)`](view/listsectionseparatortint(_:edges:).md).

## Parameters

- `visibility`: The visibility of this section’s separators.
- `edges`: The set of row edges for which the preference applies.   The list style might already decide to not display separators for   some edges. The default is  .

## See Also

- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listsectionseparator(_:edges:))*