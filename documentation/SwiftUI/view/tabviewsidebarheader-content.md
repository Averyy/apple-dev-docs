# tabViewSidebarHeader(content:)

**Framework**: SwiftUI  
**Kind**: method

Adds a custom header to the sidebar of a tab view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func tabViewSidebarHeader<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
```

#### Discussion

The header appears at the top of the sidebar before any tab labels and can scroll with the content. The header is only visible when the [`TabView`](tabview.md) is displaying the sidebar.

The following example adds a welcome message to the top of the sidebar:

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }

    Tab("Browse", systemImage: "list.bullet") {
        MyBrowseView()
    }
}
.tabViewStyle(.sidebarAdaptable)
.tabViewSidebarHeader {
    WelcomeHeaderView()
}
```

> **Note**: To have a sidebar, a[`TabView`](tabview.md) needs the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style.

To have a sidebar, a[`TabView`](tabview.md) needs the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style.

## See Also

- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](view/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](view/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [struct AdaptableTabBarPlacement](adaptabletabbarplacement.md)
  A placement for tabs in a tab view using the adaptable sidebar style.
- [var tabBarPlacement: TabBarPlacement?](environmentvalues/tabbarplacement.md)
  The current placement of the tab bar.
- [struct TabBarPlacement](tabbarplacement.md)
  A placement for tabs in a tab view.
- [var isTabBarShowingSections: Bool](environmentvalues/istabbarshowingsections.md)
  A Boolean value that determines whether a tab view shows the expanded contents of a tab section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabviewsidebarheader(content:))*