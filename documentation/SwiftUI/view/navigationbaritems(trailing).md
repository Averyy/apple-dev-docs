# navigationBarItems(trailing:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the navigation bar items for this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`toolbar(content:)`](./toolbar%28content%29-5w0tj.md) with [`topBarTrailing`](../toolbaritemplacement/topbartrailing.md) placement.

## Declaration

```swift
nonisolated
func navigationBarItems<T>(trailing: T) -> some View where T : View
```

## Discussion

Use `navigationBarItems(trailing:)` to add navigation bar items to the trailing edge of the navigation bar for this view. This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](../navigationview.md).

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

### Auxiliary view modifiers
- [func navigationBarTitle(_:)](./navigationbartitle%28_%29.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(_:displayMode:)](./navigationbartitle%28_,displaymode%29.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](./navigationbaritems%28leading%29.md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](./navigationbaritems%28leading,trailing%29.md)
  Sets the navigation bar items for this view.
- [func navigationBarHidden(Bool) -> some View](./navigationbarhidden%28_%29.md)
  Hides the navigation bar for this view.
- [func statusBar(hidden: Bool) -> some View](./statusbar%28hidden%29.md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](./contextmenu%28_%29.md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbaritems(trailing:))*