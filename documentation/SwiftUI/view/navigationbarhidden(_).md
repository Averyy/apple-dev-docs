# navigationBarHidden(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Hides the navigation bar for this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`toolbar(_:for:)`](./toolbar%28_,for%29.md) with the [`Visibility.hidden`](../visibility/hidden.md) visibility and the [`navigationBar`](../toolbarplacement/navigationbar.md) placement instead.

## Declaration

```swift
nonisolated
func navigationBarHidden(_ hidden: Bool) -> some View
```

#### Discussion

Use this method to hide the navigation bar. This modifier only takes effect when the modified view is inside of and visible within a [`NavigationView`](../navigationview.md).

## Parameters

- `hidden`: A Boolean value that indicates whether to hide the navigation bar.

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
- [func navigationBarItems<T>(trailing: T) -> some View](./navigationbaritems%28trailing%29.md)
  Configures the navigation bar items for this view.
- [func statusBar(hidden: Bool) -> some View](./statusbar%28hidden%29.md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](./contextmenu%28_%29.md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbarhidden(_:))*