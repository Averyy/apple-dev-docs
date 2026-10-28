# badge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Generates a badge for a tab from an integer value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func badge(_ count: Int) -> some TabContent<Self.TabValue>
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func badge(_ resource: LocalizedStringResource) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func badge(_ key: LocalizedStringKey) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func badge(_ label: Text?) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func badge<S>(_ label: S) -> some TabContent<Self.TabValue> where S : StringProtocol
```

## Discussion

Use a badge to convey optional, supplementary information about a view. The number provided will appear as a numerical indicator on the given tab.

The following example shows a [`TabView`](../tabview.md) with the value of `alerts.count` displayed as a badge on the alerts tab.

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }
    .badge(alerts.count)
}
```

## Parameters

- `count`: An integer value to display in the badge. Set the value to zero to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/badge(_:)-8bxge)*