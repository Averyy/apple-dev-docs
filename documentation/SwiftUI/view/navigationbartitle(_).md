# navigationBarTitle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the title in the navigation bar for this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: navigationTitle(_:))

> **Deprecated**: Use [`navigationTitle(_:)`](./navigationtitle%28_%29-5di1u.md) instead.

## Declaration

```swift
nonisolated
func navigationBarTitle(_ title: Text) -> some View
```

**Other overloads**:

```swift
nonisolated
func navigationBarTitle(_ titleKey: LocalizedStringKey) -> some View
```

```swift
nonisolated
func navigationBarTitle<S>(_ title: S) -> some View where S : StringProtocol
```

#### Discussion

Use `navigationBarTitle(_:)` to set the title of the navigation bar. This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](../navigationview.md).

The example below shows setting the title of the navigation bar using a [`Text`](../text.md) view:

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

![A screenshot showing the title of a navigation bar configured using a text view.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-navigationBarTitle-Text@2x.png)

## Parameters

- `title`: A description of this view to display in the navigation bar.

## See Also

### Auxiliary view modifiers
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
- [func statusBar(hidden: Bool) -> some View](./statusbar%28hidden%29.md)
  Sets the visibility of the status bar.
- [func contextMenu<MenuItems>(ContextMenu<MenuItems>?) -> some View](./contextmenu%28_%29.md)
  Adds a context menu to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbartitle(_:))*