# defaultAdaptableTabBarPlacement(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.

**Availability**:
- iOS 18.0+

## Declaration

```swift
nonisolated
func defaultAdaptableTabBarPlacement(_ defaultPlacement: AdaptableTabBarPlacement = .automatic) -> some View
```

#### Discussion

This modifier is only effective on iPadOS in the `TabViewStyle/sidebarAdaptable` style. In any other configuration, the system ignores it.

The following example shows a `TabView` with three tabs, where the tab view displays the sidebar representation when the app initially launches.

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/defaultadaptabletabbarplacement(_:))*