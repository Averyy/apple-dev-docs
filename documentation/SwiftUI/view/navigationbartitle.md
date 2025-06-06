# navigationBarTitle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the title in the navigation bar for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func navigationBarTitle(_ title: Text) -> some View
```

#### Discussion

Use `navigationBarTitle(_:)` to set the title of the navigation bar. This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](navigationview.md).

The example below shows setting the title of the navigation bar using a [`Text`](text.md) view:

```swift
struct FlavorView: View {
    let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                 "Pistachio"]
    var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle(Text("Today's Flavors"))
        }
    }
}
```

![A screenshot showing the title of a navigation bar configured using a text view.](https://docs-assets.developer.apple.com/published/e979a74714a538aace4065738249084b/SwiftUI-navigationBarTitle-Text%402x.png)

## Parameters

- `title`: A description of this view to display in the   navigation bar.

## See Also

- [func navigationBarTitle(_:displayMode:)](view/navigationbartitle(_:displaymode:).md)
  Sets the title and display mode in the navigation bar for this view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbartitle(_:))*