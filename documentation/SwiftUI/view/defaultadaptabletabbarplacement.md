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

- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](view/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](view/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](view/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](view/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.
- [func sectionActions<Content>(content: () -> Content) -> some View](view/sectionactions(content:).md)
  Adds custom actions to a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/defaultadaptabletabbarplacement(_:))*