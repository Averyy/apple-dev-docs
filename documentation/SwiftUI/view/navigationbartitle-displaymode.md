# navigationBarTitle(_:displayMode:)

**Framework**: SwiftUI  
**Kind**: method

Sets the title and display mode in the navigation bar for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func navigationBarTitle(_ title: Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View
```

#### Discussion

Use `navigationBarTitle(_:displayMode:)` to set the title of the navigation bar for this view and specify a display mode for the title from one of the [`NavigationBarItem.TitleDisplayMode`](navigationbaritem/titledisplaymode.md) styles. This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](navigationview.md).

In the example below, text for the navigation bar title is provided using a [`Text`](text.md) view. The navigation bar title’s [`NavigationBarItem.TitleDisplayMode`](navigationbaritem/titledisplaymode.md) is set to `.inline` which places the navigation bar title in the bounds of the navigation bar.

```swift
struct FlavorView: View {
   let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                "Pistachio"]
   var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle(Text("Today's Flavors", displayMode: .inline))
        }
    }
}
```

## Parameters

- `title`: A title for this view to display in the navigation bar.
- `displayMode`: The style to use for displaying the navigation bar title.

## See Also

- [func navigationBarTitle(_:)](view/navigationbartitle(_:).md)
  Sets the title in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](view/navigationbaritems(leading:).md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](view/navigationbaritems(leading:trailing:).md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<T>(trailing: T) -> some View](view/navigationbaritems(trailing:).md)
  Configures the navigation bar items for this view.
- [func navigationBarHidden(Bool) -> some View](view/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func statusBar(hidden: Bool) -> some View](view/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](view/contextmenu(_:).md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbartitle(_:displaymode:))*