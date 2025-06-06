# listSectionSeparatorTint(_:edges:)

**Framework**: SwiftUI  
**Kind**: method

Sets the tint color associated with a section.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func listSectionSeparatorTint(_ color: Color?, edges: VerticalEdge.Set = .all) -> some View
```

#### Discussion

Separators can be presented above and below a section. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing [`List`](list.md). The list style is the final arbiter for the separator tint.

The following example shows a simple grouped list whose section separators are tinted based on section-specific data:

```swift
List {
    ForEach(garage) { garage in
        Section(header: Text(garage.location)) {
            ForEach(garage.cars) { car in
                Text(car.model)
                    .listRowSeparatorTint(car.brandColor)
            }
        }
        .listSectionSeparatorTint(
            garage.cars.last?.brandColor, edges: .bottom)
    }
}
.listStyle(.grouped)
```

To change the visibility and tint color for a row separator, use [`listRowSeparator(_:edges:)`](view/listrowseparator(_:edges:).md) and [`listRowSeparatorTint(_:edges:)`](view/listrowseparatortint(_:edges:).md). To hide a section separator, use [`listSectionSeparator(_:edges:)`](view/listsectionseparator(_:edges:).md).

## Parameters

- `color`: The color to use to tint the section separators, or   to   use the default color for the current list style.
- `edges`: The set of row edges for which the tint applies.   The list style might decide to not display certain separators,   typically the top edge. The default is  .

## See Also

- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](view/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](view/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listsectionseparatortint(_:edges:))*