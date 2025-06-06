# navigationBarItems(trailing:)

**Framework**: SwiftUI  
**Kind**: method

Configures the navigation bar items for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func navigationBarItems<T>(trailing: T) -> some View where T : View
```

#### Discussion

Use `navigationBarItems(trailing:)` to add navigation bar items to the trailing edge of the navigation bar for this view. This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](navigationview.md).

The example below adds buttons to the trailing edge of the button area of the navigation view:

```swift
struct FlavorView: View {
    var body: some View {
        NavigationView {
            List {
                Text("Chocolate")
                Text("Vanilla")
                Text("Strawberry")
            }
            .navigationBarTitle(Text("Today‘s Flavors"))
            .navigationBarItems(trailing:
                HStack {
                    Button("Hours") {
                        print("Hours tapped!")
                    }

                    Button("Help") {
                        print("Help tapped!")
                    }
                }
            )
        }
    }
}
```

## Parameters

- `trailing`: A view shown on the trailing edge of the title.

## See Also

- [func navigationBarTitle(_:)](view/navigationbartitle(_:).md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(_:displayMode:)](view/navigationbartitle(_:displaymode:).md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](view/navigationbaritems(leading:).md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](view/navigationbaritems(leading:trailing:).md)
  Sets the navigation bar items for this view.
- [func navigationBarHidden(Bool) -> some View](view/navigationbarhidden(_:).md)
  Hides the navigation bar for this view.
- [func statusBar(hidden: Bool) -> some View](view/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](view/contextmenu(_:).md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbaritems(trailing:))*