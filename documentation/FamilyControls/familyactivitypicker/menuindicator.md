# menuIndicator(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the menu indicator visibility for controls within this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
nonisolated
func menuIndicator(_ visibility: Visibility) -> some View
```

#### Discussion

Use this modifier to override the default menu indicator visibility for controls in this view. For example, the code below creates a menu without an indicator:

```swift
Menu {
    ForEach(history , id: \.self) { historyItem in
        Button(historyItem.title) {
            self.openURL(historyItem.url)
        }
    }
} label: {
    Label("Back", systemImage: "chevron.backward")
        .labelStyle(.iconOnly)
} primaryAction: {
    if let last = history.last {
        self.openURL(last.url)
    }
}
.menuIndicator(.hidden)
```

> **Note**: On tvOS, the standard button styles do not include a menu indicator, so this modifier will have no effect when using a built-in button style. You can implement an indicator in your own `ButtonStyle` implementation by checking the value of the `menuIndicatorVisibility` environment value.

## Parameters

- `visibility`: The menu indicator visibility to apply.

## See Also

- [func hidden() -> some View](familyactivitypicker/hidden.md)
  Hides this view unconditionally.
- [func labelsHidden() -> some View](familyactivitypicker/labelshidden.md)
  Hides the labels of any controls contained within this view.
- [func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listrowseparator(_:edges:).md)
  Sets the display mode for the separator associated with this specific row.
- [func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View](familyactivitypicker/listsectionseparator(_:edges:).md)
  Sets whether to hide the separator associated with a list section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/menuindicator(_:))*