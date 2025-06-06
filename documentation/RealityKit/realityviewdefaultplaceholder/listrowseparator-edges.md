# listRowSeparator(_:edges:)

**Framework**: RealityKit  
**Kind**: method

Sets the display mode for the separator associated with this specific row.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func listRowSeparator(_ visibility: Visibility, edges: VerticalEdge.Set = .all) -> some View
```

#### Discussion

Separators can be presented above and below a row. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose row separators are hidden:

```None
List {
    ForEach(garage.cars) { car in
        Text(car.model)
            .listRowSeparator(.hidden)
    }
}
.listStyle(.grouped)
```

To change the color of a row separators, use `View/listRowSeparatorTint(_:edges:)`. To hide or change the tint color for a section separators, use `View/listSectionSeparator(_:edges:)` and `View/listSectionSeparatorTint(_:edges:)`.

## Parameters

- `visibility`: The visibility of this row’s separators.
- `edges`: The set of row edges for which this preference applies.   The list style might already decide to not display separators for   some edges, typically the top edge. The default is   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/listrowseparator(_:edges:))*