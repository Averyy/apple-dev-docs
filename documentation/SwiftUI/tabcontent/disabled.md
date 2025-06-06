# disabled(_:)

**Framework**: SwiftUI  
**Kind**: method

Controls whether users can interact with this tab.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
func disabled(_ disabled: Bool) -> some TabContent<Self.TabValue>
```

#### Discussion

The following example shows a [`TabView`](tabview.md) with one tab that is not selectable.

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }
    .disabled(alertsDisabled)
}
```

## Parameters

- `disabled`: A Boolean value that determines whether users can   interact with this tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/disabled(_:))*