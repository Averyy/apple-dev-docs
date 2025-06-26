# tint(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the tint color within this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func tint(_ tint: Color?) -> some View
```

#### Discussion

Use this method to override the default accent color for this view. Unlike an app’s accent color, which can be overridden by user preference, the tint color is always respected and should be used as a way to provide additional meaning to the control.

This example shows Answer and Decline buttons with `ShapeStyle/green` and `ShapeStyle/red` tint colors, respectively.

```swift
struct ControlTint: View {
    var body: some View {
        HStack {
            Button {
                // Answer the call
            } label: {
                Label("Answer", systemImage: "phone")
            }
            .tint(.green)
            Button {
                // Decline the call
            } label: {
                Label("Decline", systemImage: "phone.down")
            }
            .tint(.red)
        }
        .buttonStyle(.borderedProminent)
        .padding()
    }
}
```

Some controls adapt to the tint color differently based on their style, the current platform, and the surrounding context. For example, in macOS, a button with the `PrimitiveButtonStyle/bordered` style doesn’t tint its background, but one with the `PrimitiveButtonStyle/borderedProminent` style does. In macOS, neither of these button styles tint their label, but they do in other platforms.

## Parameters

- `tint`: The tint   to apply.

## See Also

- [func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listrowseparatortint(_:edges:).md)
  Sets the tint color associated with a row.
- [func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listsectionseparatortint(_:edges:).md)
  Sets the tint color associated with a section.
- [func listItemTint(ListItemTint?) -> some View](familyactivitypicker/listitemtint(_:)-9guaj.md)
  Sets the tint effect for content in a list.
- [func listItemTint(Color?) -> some View](familyactivitypicker/listitemtint(_:)-9hrk.md)
  Sets a fixed tint color for content in a list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/tint(_:))*