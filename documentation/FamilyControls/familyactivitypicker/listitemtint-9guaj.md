# listItemTint(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the tint effect for content in a list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func listItemTint(_ tint: ListItemTint?) -> some View
```

#### Discussion

The containing list’s style applies the tint as appropriate. For example, watchOS uses the tint color for its background platter appearance. Sidebars on iOS and macOS apply the tint color to their `Label` icons, which otherwise use the accent color by default.

## Parameters

- `tint`: The tint effect to use. Use   to avoid  overriding   the inherited tint.

## See Also

- [func tint(Color?) -> some View](familyactivitypicker/tint(_:).md)
  Sets the tint color within this view.
- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listItemTint(Color?) -> some View](familyactivitypicker/listitemtint(_:)-9hrk.md)
  Sets a fixed tint color for content in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/listitemtint(_:)-9guaj)*