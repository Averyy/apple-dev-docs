# contentToolbar(for:content:)

**Framework**: SwiftUI  
**Kind**: method

Populates the toolbar of the specified content view type with the views you provide.

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
nonisolated
func contentToolbar<Content>(for placement: ContentToolbarPlacement, @ContentBuilder content: () -> Content) -> some View where Content : View
```

#### Discussion

Use this modifier to add toolbar content that remains consistent regardless of the content view.

Unlike the toolbar modifier, which configures the toolbar of the modified view’s container, the `contentToolbar` modifier configures the toolbar within the modified view’s content instead. This means that the `contentToolbar` modifier should generally be applied directly to a container view, instead of to the content within a container view. For example, to configure the toolbar of tab view’s sidebar, apply the `contentToolbar` modifier to the `TabView` itself, not to any of the tabs within the `TabView`.

The example below adds a button to the tab view sidebar.

```swift
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
    DisconnectDevicesButton()
}
```

## Parameters

- `content`: The views representing the content of the toolbar.

## See Also

- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](view/toolbar(id:content:).md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbar(Visibility, for: ToolbarPlacement...) -> some View](view/toolbar(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](view/toolbar(removing:).md)
  Remove a toolbar item present by default
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarvisibility(_:for:).md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarBackground(_:for:)](view/toolbarbackground(_:for:).md)
  Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](view/toolbarbackgroundvisibility(_:for:).md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarItemHidden(Bool) -> some View](view/toolbaritemhidden(_:).md)
  Hides an individual view within a control group toolbar item.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](view/toolbarforegroundstyle(_:for:).md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](view/toolbarcolorscheme(_:for:).md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarOverflowMenu<C>(content: () -> C) -> some View](view/toolbaroverflowmenu(content:).md)
  Configures the overflow menu of a toolbar.
- [func toolbarRole(ToolbarRole) -> some View](view/toolbarrole(_:).md)
  Configures the semantic role for the content populating the toolbar.
- [func toolbarMinimizationSafeAreaAdjustment(ToolbarMinimizationSafeAreaAdjustment, for: ToolbarPlacement...) -> some View](view/toolbarminimizationsafeareaadjustment(_:for:).md)
  Sets the safe area adjustment for the specified bars during minimization.
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](view/toolbartitlemenu(content:).md)
  Configure the title menu of a toolbar.
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](view/toolbartitledisplaymode(_:).md)
  Configures the toolbar title display mode for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contenttoolbar(for:content:))*