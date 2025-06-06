# sectionActions(content:)

**Framework**: SwiftUI  
**Kind**: method

Adds custom actions to a tab section.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func sectionActions<Content>(@ViewBuilder content: () -> Content) -> some TabContent<Self.TabValue> where Content : View
```

#### Discussion

On iOS, the actions are displayed after the other tabs in the section. On macOS, the actions are displayed when a user hovers over the section.

Applying this modifier to a single [`Tab`](tab.md) has no effect.

The following example adds an ‘Add’ button to the ‘Categories’ section.

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
    .sectionActions {
        Button("Add Category", systemImage: "plus") { }
    }
}
.tabViewStyle(.sidebarAdaptable)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/sectionactions(content:))*