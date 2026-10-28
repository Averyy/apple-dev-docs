# navigationBarItems(leading:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the navigation bar items for this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`toolbar(content:)`](./toolbar%28content%29-5w0tj.md) with [`navigationBarLeading`](../toolbaritemplacement/navigationbarleading.md) placement.

## Declaration

```swift
nonisolated
func navigationBarItems<L>(leading: L) -> some View where L : View
```

## Discussion

Use `navigationBarItems(leading:)` to add navigation bar items to the leading edge of the navigation bar for this view.

This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](../navigationview.md).

On iOS 14 and later, the leading item supplements a visible back button, instead of replacing it, by default. To hide the back button, use [`navigationBarBackButtonHidden(_:)`](./navigationbarbackbuttonhidden%28_%29.md).

The example below adds buttons to the leading edge of the button area of the navigation view:

```swift
struct FlavorView: View {
    var body: some View {
        NavigationView {
            List {
                Text("Chocolate")
                Text("Vanilla")
                Text("Strawberry")
            }
            .navigationBarTitle(Text("Today's Flavors"))
            .navigationBarItems(leading:
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

- `leading`: A view that appears on the leading edge of the title.

## See Also

### Auxiliary view modifiers
- [func navigationBarTitle(_:)](./navigationbartitle%28_%29.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(_:displayMode:)](./navigationbartitle%28_,displaymode%29.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](./navigationbaritems%28leading,trailing%29.md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<T>(trailing: T) -> some View](./navigationbaritems%28trailing%29.md)
  Configures the navigation bar items for this view.
- [func navigationBarHidden(Bool) -> some View](./navigationbarhidden%28_%29.md)
  Hides the navigation bar for this view.
- [func statusBar(hidden: Bool) -> some View](./statusbar%28hidden%29.md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](./contextmenu%28_%29.md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbaritems(leading:))*