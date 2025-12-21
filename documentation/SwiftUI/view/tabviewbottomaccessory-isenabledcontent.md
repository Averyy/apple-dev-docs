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
func tabViewBottomAccessory<Content>(isEnabled: Bool, @ViewBuilder content: () -> Content) -> some View where Content : View
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

- `isEnabled`: If true, the bottom accessory is shown; otherwise,   the bottom accessory is hidden.
- `content`: The content view of the tab view accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabviewbottomaccessory(isenabled:content:))*