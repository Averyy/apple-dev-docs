# defaultAdaptableTabBarPlacement(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
nonisolated
func defaultAdaptableTabBarPlacement(_ defaultPlacement: AdaptableTabBarPlacement = .automatic) -> some View
```

#### Discussion

This modifier is only effective on iPadOS in the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style. In any other configuration, the system ignores it.

The following example shows a [`TabView`](tabview.md) with three tabs, where the tab view displays the sidebar representation when the app initially launches.

```swift
TabView(selection: $selection) {
    Tab("Home", systemImage: "house", value: MyTab.home) {
        MyHomeView()
    }

    Tab("Downloads", systemImage: "square.and.arrow.down.fill",
        value: MyTab.downloads
    ) {
        MyDownloadsView()
    }

    Tab("Browse", systemImage: "list.bullet", value: MyTab.browse) {
        MyBrowseView()
    }
}
.tabViewStyle(.sidebarAdaptable)
.defaultAdaptableTabBarPlacement(.sidebar)
```

## Parameters

- `defaultPlacement`: The default arrangement for the tab view.

## See Also

- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](view/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
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
- [struct TabBarMinimizeBehavior](tabbarminimizebehavior.md)
- [enum TabViewBottomAccessoryPlacement](tabviewbottomaccessoryplacement.md)
  A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/defaultadaptabletabbarplacement(_:))*