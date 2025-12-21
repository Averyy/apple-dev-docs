# tabViewBottomAccessory(content:)

**Framework**: SwiftUI  
**Kind**: method

Places a view as the bottom accessory of the tab view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
nonisolated
func tabViewBottomAccessory<Content>(@ViewBuilder content: () -> Content) -> some View where Content : View
```

#### Discussion

On iPhone, the placement of the bottom accessory depends on the tab bar size: when the tab bar is normal size, the accessory appears above it; when the tab bar is collapsed, the accessory displays inline. Use the [`tabViewBottomAccessoryPlacement`](environmentvalues/tabviewbottomaccessoryplacement.md) environment value to adjust the accessory’s content based on its placement.

The following example sets a status view as the `TabView` bottom accessory.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/tabviewbottomaccessory(content:))*