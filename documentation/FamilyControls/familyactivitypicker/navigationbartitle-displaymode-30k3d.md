# navigationBarTitle(_:displayMode:)

**Framework**: FamilyControls  
**Kind**: method

Sets the title and display mode in the navigation bar for this view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func navigationBarTitle<S>(_ title: S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View where S : StringProtocol
```

#### Discussion

Use `navigationBarTitle(_:displayMode:)` to set the title of the navigation bar for this view and specify a display mode for the title from one of the `NavigationBarItem.Title.DisplayMode` styles. This modifier only takes effect when this view is inside of and visible within a `NavigationView`.

In the example below, `navigationBarTitle(_:displayMode:)` uses a string to provide a title for the navigation bar. Setting the title’s `displayMode` to `.inline` places the navigation bar title within the bounds of the navigation bar.

In the example below, text for the navigation bar title is provided using a string. The navigation bar title’s `displayMode` is set to `.inline` which places the navigation bar title in the bounds of the navigation bar.

```swift
struct FlavorView: View {
    let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                 "Pistachio"]
    let title = "Today's Flavors"
    var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle(title, displayMode: .inline)
        }
    }
}
```

![A screenshot of a navigation bar, showing the title within the bounds of the navigation bar] (SwiftUI-navigationBarTitle-stringProtocol.png)

## Parameters

- `title`: A title for this view to display in the navigation bar.
- `displayMode`: The way to display the title.

## See Also

- [func navigationBarTitle<S>(S) -> some View](familyactivitypicker/navigationbartitle(_:)-5rx0t.md)
  Sets the title of this view’s navigation bar with a string.
- [func navigationBarTitle(LocalizedStringKey) -> some View](familyactivitypicker/navigationbartitle(_:)-808tn.md)
  Sets the title of this view’s navigation bar with a localized string.
- [func navigationBarTitle(Text) -> some View](familyactivitypicker/navigationbartitle(_:)-9xbmw.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitle(_:displaymode:)-22lni.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitle(_:displaymode:)-9ps22.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](familyactivitypicker/navigationbaritems(leading:).md)
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](familyactivitypicker/navigationbaritems(leading:trailing:).md)
- [func navigationBarItems<T>(trailing: T) -> some View](familyactivitypicker/navigationbaritems(trailing:).md)
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](familyactivitypicker/contextmenu(_:).md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/navigationbartitle(_:displaymode:)-30k3d)*