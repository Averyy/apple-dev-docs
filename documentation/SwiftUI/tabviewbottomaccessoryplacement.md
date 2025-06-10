# TabViewBottomAccessoryPlacement

**Framework**: SwiftUI  
**Kind**: enum

A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
enum TabViewBottomAccessoryPlacement
```

#### Overview

The following example shows playback controls when the view is inline, and an expanded slider player view when the view is expanded.

```swift
struct MusicPlaybackView: View {
    @Environment(\.tabViewBottomAccessoryPlacement) var placement

    var body: some View {
        switch placement {
        case .inline:
            ControlsPlaybackView()
        case .expanded:
            SliderPlaybackView()
    }
}
```

You can set the `TabView` bottom accessory using [`tabViewBottomAccessory(content:)`](view/tabviewbottomaccessory(content:).md)

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
.tabViewBottomAccessory {
    HomeStatusView()
}
```

## Topics

### Enumeration Cases
- [TabViewBottomAccessoryPlacement.expanded](tabviewbottomaccessoryplacement/expanded.md)
  The bar is expanded on top of the bottom tab bar, if there is a bottom tab bar, or at the bottom of the tab’s content view.
- [TabViewBottomAccessoryPlacement.inline](tabviewbottomaccessoryplacement/inline.md)
  The view is displayed in line with the bottom tab bar.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabviewbottomaccessoryplacement)*