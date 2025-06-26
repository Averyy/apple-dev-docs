# navigationBarItems(leading:trailing:)

**Framework**: FamilyControls  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func navigationBarItems<L, T>(leading: L, trailing: T) -> some View where L : View, T : View
```

## See Also

- [func navigationBarTitle<S>(S) -> some View](familyactivitypicker/navigationbartitle(_:)-5rx0t.md)
  Sets the title of this view’s navigation bar with a string.
- [func navigationBarTitle(LocalizedStringKey) -> some View](familyactivitypicker/navigationbartitle(_:)-808tn.md)
  Sets the title of this view’s navigation bar with a localized string.
- [func navigationBarTitle(Text) -> some View](familyactivitypicker/navigationbartitle(_:)-9xbmw.md)
  Sets the title in the navigation bar for this view.
- [func navigationBarTitle(Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitle(_:displaymode:)-22lni.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle<S>(S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitle(_:displaymode:)-30k3d.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarTitle(LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View](familyactivitypicker/navigationbartitle(_:displaymode:)-9ps22.md)
  Sets the title and display mode in the navigation bar for this view.
- [func navigationBarItems<L>(leading: L) -> some View](familyactivitypicker/navigationbaritems(leading:).md)
- [func navigationBarItems<T>(trailing: T) -> some View](familyactivitypicker/navigationbaritems(trailing:).md)
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](familyactivitypicker/contextmenu(_:).md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/navigationbaritems(leading:trailing:))*