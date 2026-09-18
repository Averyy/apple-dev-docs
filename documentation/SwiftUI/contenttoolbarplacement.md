# ContentToolbarPlacement

**Framework**: SwiftUI  
**Kind**: struct

A region of the interface that hosts its own toolbar content.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct ContentToolbarPlacement
```

#### Overview

Some containers draw a bar that belongs to the container as a whole rather than to the view currently on screen, such as the sidebar of a [`TabView`](tabview.md) that uses the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style. Pass a value of this type to [`contentToolbar(for:content:)`](view/contenttoolbar(for:content:).md) to put items in one of those bars.

The following example adds a button to the sidebar of a tab view, where it stays put as someone moves between tabs:

```swift
TabView {
    Tab("Lights", systemImage: "lightbulb") {
        LightsView()
    }

    Tab("Locks", systemImage: "lock") {
        LocksView()
    }
}
.tabViewStyle(.sidebarAdaptable)
.contentToolbar(for: .tabViewSidebar) {
    ToolbarItem {
        DisconnectDevicesButton()
    }
}
```

Each placement accepts only some [`ToolbarItemPlacement`](toolbaritemplacement.md) values. Check the documentation of the placement you use before you rely on a position.

## Topics

### Type Properties
- [static let tabViewSidebar: ContentToolbarPlacement](contenttoolbarplacement/tabviewsidebar.md)
  The tab view sidebar. This is present on certain platforms when using the `.sidebarAdaptable` tab view style.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](view/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [struct ToolbarPlacement](toolbarplacement.md)
  The placement of a toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contenttoolbarplacement)*