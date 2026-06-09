# tabViewBottomAccessory(isEnabled:content:)

**Framework**: SwiftUI  
**Kind**: method

Places a view as the bottom accessory of the tab view. Use this modifier to dynamically show and hide the accessory view.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+

## Declaration

```swift
nonisolated
func tabViewBottomAccessory<Content>(isEnabled: Bool, @ContentBuilder content: () -> Content) -> some View where Content : View
```

#### Discussion

On iPhone, the placement of the bottom accessory depends on the tab bar size: when the tab bar is normal size, the accessory appears above it; when the tab bar is collapsed, the accessory displays inline. Use the [`tabViewBottomAccessoryPlacement`](environmentvalues/tabviewbottomaccessoryplacement.md) environment value to adjust the accessory’s content based on its placement.

The following example shows a status view in the `TabView` bottom accessory when there’s a status update.

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
.tabViewBottomAccessory(isEnabled: hasStatusUpdate) {
    HomeStatusView()
}
```

## Parameters

- `isEnabled`: If true, the bottom accessory is shown; otherwise, the bottom accessory is hidden.
- `content`: The content view of the tab view accessory.

## See Also

- [func defaultAdaptableTabBarPlacement(AdaptableTabBarPlacement) -> some View](view/defaultadaptabletabbarplacement(_:).md)
  Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [func defaultTabBarPlacement(AdaptableTabBarPlacement) -> some View](view/defaulttabbarplacement(_:).md)
  Specifies the preferred placement for the tabs of a [`TabView`](tabview.md) in the [`sidebarAdaptable`](tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown.
- [func sectionActions<Content>(content: () -> Content) -> some View](view/sectionactions(content:).md)
  Adds custom actions to a section.
- [func tabBarMinimizeBehavior(TabBarMinimizeBehavior) -> some View](view/tabbarminimizebehavior(_:).md)
  Sets the behavior for tab bar minimization.
- [func tabViewBottomAccessory<Content>(content: () -> Content) -> some View](view/tabviewbottomaccessory(content:).md)
  Places a view as the bottom accessory of the tab view.
- [func tabViewCustomization(Binding<TabViewCustomization>?) -> some View](view/tabviewcustomization(_:).md)
  Specifies the customizations to apply to the sidebar representation of the tab view.
- [func tabViewSearchActivation(TabSearchActivation) -> some View](view/tabviewsearchactivation(_:).md)
  Configures the activation and deactivation behavior of search in the search tab.
- [func tabViewSidebarHeader<Content>(content: () -> Content) -> some View](view/tabviewsidebarheader(content:).md)
  Adds a custom header to the sidebar of a tab view.
- [func tabViewSidebarFooter<Content>(content: () -> Content) -> some View](view/tabviewsidebarfooter(content:).md)
  Adds a custom footer to the sidebar of a tab view.
- [func tabViewSidebarBottomBar<Content>(content: () -> Content) -> some View](view/tabviewsidebarbottombar(content:).md)
  Adds a custom bottom bar to the sidebar of a tab view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabviewbottomaccessory(isenabled:content:))*