# listSectionSeparatorTint(_:edges:)

**Framework**: FamilyControls  
**Kind**: method

Sets the tint color associated with a section.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+

## Declaration

```swift
nonisolated
func listSectionSeparatorTint(_ color: Color?, edges: VerticalEdge.Set = .all) -> some View
```

#### Discussion

Separators can be presented above and below a section. You can specify to which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style is the final arbiter for the separator tint.

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

To change the visibility and tint color for a row separator, use `View/listRowSeparator(_:edges:)` and `View/listRowSeparatorTint(_:edges:)`. To hide a section separator, use `View/listSectionSeparator(_:edges:)`.

## Parameters

- `color`: The color to use to tint the section separators, or   to   use the default color for the current list style.
- `edges`: The set of row edges for which the tint applies.   The list style might decide to not display certain separators,   typically the top edge. The default is  .

## See Also

- [func tint(Color?) -> some View](familyactivitypicker/tint(_:).md)
  Sets the tint color within this view.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listItemTint(ListItemTint?) -> some View](familyactivitypicker/listitemtint(_:)-9guaj.md)
  Sets the tint effect for content in a list.
- [func listItemTint(Color?) -> some View](familyactivitypicker/listitemtint(_:)-9hrk.md)
  Sets a fixed tint color for content in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/listsectionseparatortint(_:edges:))*