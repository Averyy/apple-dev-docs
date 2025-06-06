# menuStyle(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the style for menus within this view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+

## Declaration

```swift
nonisolated
func menuStyle<S>(_ style: S) -> some View where S : MenuStyle
```

#### Discussion

To set a specific style for all menu instances within a view, use the `menuStyle(_:)` modifier:

```swift
Menu("PDF") {
    Button("Open in Preview", action: openInPreview)
    Button("Save as PDF", action: saveAsPDF)
}
.menuStyle(ButtonMenuStyle())
```

## See Also

- [func buttonStyle<S>(S) -> some View](familyactivitypicker/buttonstyle(_:)-5jlha.md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonStyle<S>(S) -> some View](familyactivitypicker/buttonstyle(_:)-9kz36.md)
  Sets the style for buttons within this view to a button style with a custom appearance and custom interaction behavior.
- [func controlGroupStyle<S>(S) -> some View](familyactivitypicker/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [func datePickerStyle<S>(S) -> some View](familyactivitypicker/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [func groupBoxStyle<S>(S) -> some View](familyactivitypicker/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [func indexViewStyle<S>(S) -> some View](familyactivitypicker/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [func labelStyle<S>(S) -> some View](familyactivitypicker/labelstyle(_:).md)
  Sets the style for labels within this view.
- [func listStyle<S>(S) -> some View](familyactivitypicker/liststyle(_:).md)
  Sets the style for lists within this view.
- [func navigationViewStyle<S>(S) -> some View](familyactivitypicker/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
- [func pickerStyle<S>(S) -> some View](familyactivitypicker/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func progressViewStyle<S>(S) -> some View](familyactivitypicker/progressviewstyle(_:).md)
  Sets the style for progress views in this view.
- [func textFieldStyle<S>(S) -> some View](familyactivitypicker/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [func toggleStyle<S>(S) -> some View](familyactivitypicker/togglestyle(_:).md)
  Sets the style for toggles in a view hierarchy.
- [func tabViewStyle<S>(S) -> some View](familyactivitypicker/tabviewstyle(_:).md)
  Sets the style for the tab view within the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/menustyle(_:))*