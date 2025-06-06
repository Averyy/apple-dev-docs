# navigationBarHidden(_:)

**Framework**: SwiftUI  
**Kind**: method

Hides the navigation bar for this view.

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
func navigationBarHidden(_ hidden: Bool) -> some View
```

#### Discussion

Use this method to hide the navigation bar. This modifier only takes effect when the modified view is inside of and visible within a [`NavigationView`](navigationview.md).

## Parameters

- `hidden`: A Boolean value that indicates whether to hide the   navigation bar.

## See Also

- [func navigationBarTitle(_:)](view/navigationbartitle(_:).md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(_:displayMode:)](view/navigationbartitle(_:displaymode:).md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](view/navigationbaritems(leading:).md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<L, T>(leading: L, trailing: T) -> some View](view/navigationbaritems(leading:trailing:).md)
  Sets the navigation bar items for this view.
- [func navigationBarItems<T>(trailing: T) -> some View](view/navigationbaritems(trailing:).md)
  Configures the navigation bar items for this view.
- [func statusBar(hidden: Bool) -> some View](view/statusbar(hidden:).md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](view/contextmenu(_:).md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbarhidden(_:))*