# statusBar(hidden:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the visibility of the status bar.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: statusBarHidden(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: statusBarHidden(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: statusBarHidden(_:))
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`statusBarHidden(_:)`](./statusbarhidden%28_%29.md) instead.

## Declaration

```swift
nonisolated
func statusBar(hidden: Bool) -> some View
```

#### Discussion

Use this method to show or hide the status bar.

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
- [func navigationBarHidden(Bool) -> some View](./navigationbarhidden%28_%29.md)
  Hides the navigation bar for this view.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](./contextmenu%28_%29.md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/statusbar(hidden:))*