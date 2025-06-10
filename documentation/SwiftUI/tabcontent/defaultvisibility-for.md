# defaultVisibility(_:for:)

**Framework**: SwiftUI  
**Kind**: method

Configures the default visibility of a tab in customizable contexts.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func defaultVisibility(_ visibility: Visibility, for placements: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>
```

#### Discussion

The [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style supports customization of the tab bar and sidebar on iPad. To enable customization, attach a [`TabViewCustomization`](tabviewcustomization.md) to the [`TabView`](tabview.md) using [`tabViewCustomization(_:)`](view/tabviewcustomization(_:).md).

This modifier has no effect on other platforms or on a [`TabViewStyle`](tabviewstyle.md) that doesn’t support customization.

> **Note**: Tabs in the sidebar represent all of the of tabs in [`TabView`](tabview.md). A tab that’s hidden from the sidebar is also hidden from the top bar.

The following example shows a `TabView` with three tabs, one of which is hidden by default in the sidebar.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView(selection: $selection) {
    Tab("Home", systemImage: "house", value: MyTab.home) {
        MyHomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Reports", systemImage: "chart.bar", value: MyTab.reports) {
        MyReportsView()
    }
    .customizationID("com.myApp.reports")

    Tab("Browse", systemImage: "list.bullet", value: MyTab.browse) {
        MyBrowseView()
    }
    .customizationID("com.myApp.browse")
    .defaultVisibility(.hidden, for: .sidebar)
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

## Parameters

- `visibility`: The tab’s visibility.
- `placements`: The locations to apply the visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/defaultvisibility(_:for:))*