# contentToolbar(for:content:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Populates the toolbar of the specified content view type with the views you provide.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
nonisolated
func contentToolbar<Content>(for placement: ContentToolbarPlacement, @ToolbarContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
```

#### Discussion

Use this modifier to add toolbar content that remains consistent regardless of the content view. Use a `toolbar` modifier within the content view if the toolbar content is dependent the content view is showing.

Unlike the toolbar modifier, which configures the toolbar of the modified view’s container, the `contentToolbar` modifier configures the toolbar within the modified view’s content instead. This means that the `contentToolbar` modifier should generally be applied directly to a container view, instead of to the content within a container view. For example, to configure the toolbar of tab view’s sidebar, apply the `contentToolbar` modifier to the `TabView` itself, not to any of the tabs within the `TabView`.

The content toolbar modifier expects a collection of toolbar items that you can provide by either supplying a collection of views with each view wrapped in a `ToolbarItem`, or by providing a collection of views as a `ToolbarItemGroup`. The example below adds an account summary to the bottom of the tab view sidebar and a button to the tab view sidebar overflow menu.

```None
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }

    TabSection("Categories") {
        Tab("Climate", systemImage: "fan") {
            ClimateView()
        }

        Tab("Lights", systemImage: "lightbulb") {
            LightsView()
        }
    }
}
.tabViewStyle(.sidebarAdaptable)
.contentToolbar(for: .tabViewSidebar) {
    ToolbarItem(placement: .automatic) {
        DisconnectDevicesButton()
    }
    ToolbarItem(placement: .bottomBar) {
        AccountSummaryView()
    }
}
```

## Parameters

- `content`: The views representing the content of the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/contenttoolbar(for:content:)-q1dy)*