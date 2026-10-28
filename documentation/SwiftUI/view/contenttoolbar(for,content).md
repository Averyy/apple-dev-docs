# contentToolbar(for:content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
nonisolated
func contentToolbar<Content>(for placement: ContentToolbarPlacement, @ToolbarContentBuilder content: () -> Content) -> some View where Content : ToolbarContent
```

## Discussion

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

### Toolbars
- [func toolbar(content:)](./toolbar%28content%29.md)
  Populates the toolbar or navigation bar with the specified items.
- [func toolbar<Content>(id: String, content: () -> Content) -> some View](./toolbar%28id,content%29.md)
  Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [func toolbar(removing: ToolbarDefaultItemKind?) -> some View](./toolbar%28removing%29.md)
  Remove a toolbar item present by default
- [func toolbarVisibility(Visibility, for: ToolbarPlacement...) -> some View](./toolbarvisibility%28_,for%29.md)
  Specifies the visibility of a bar managed by SwiftUI.
- [func toolbarBackgroundVisibility(Visibility, for: ToolbarPlacement...) -> some View](./toolbarbackgroundvisibility%28_,for%29.md)
  Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [func toolbarItemHidden(Bool) -> some View](./toolbaritemhidden%28_%29.md)
  Hides an individual view within a control group toolbar item.
- [func toolbarForegroundStyle<S>(S, for: ToolbarPlacement...) -> some View](./toolbarforegroundstyle%28_,for%29.md)
  Specifies the preferred foreground style of bars managed by SwiftUI.
- [func toolbarColorScheme(ColorScheme?, for: ToolbarPlacement...) -> some View](./toolbarcolorscheme%28_,for%29.md)
  Specifies the preferred color scheme of a bar managed by SwiftUI.
- [func toolbarOverflowMenu<C>(content: () -> C) -> some View](./toolbaroverflowmenu%28content%29.md)
  Configures the overflow menu of a toolbar.
- [func toolbarRole(ToolbarRole) -> some View](./toolbarrole%28_%29.md)
  Configures the semantic role for the content populating the toolbar.
- [func toolbarMinimizationBehavior(ToolbarMinimizationBehavior, for: ToolbarPlacement...) -> some View](./toolbarminimizationbehavior%28_,for%29.md)
  Sets the minimize behavior for the specified bars.
- [func toolbarMinimizationRestoration(ToolbarMinimizationRestoration, for: ToolbarPlacement...) -> some View](./toolbarminimizationrestoration%28_,for%29.md)
  Sets the restoration behavior for the specified bars during minimization.
- [func toolbarMinimizationSafeAreaAdjustment(ToolbarMinimizationSafeAreaAdjustment, for: ToolbarPlacement...) -> some View](./toolbarminimizationsafeareaadjustment%28_,for%29.md)
  Sets the safe area adjustment for the specified bars during minimization.
- [func toolbarTitleMenu<C>(content: () -> C) -> some View](./toolbartitlemenu%28content%29.md)
  Configure the title menu of a toolbar.
- [func toolbarTitleDisplayMode(ToolbarTitleDisplayMode) -> some View](./toolbartitledisplaymode%28_%29.md)
  Configures the toolbar title display mode for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contenttoolbar(for:content:))*