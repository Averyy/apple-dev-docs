# badge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Generates a badge for the tab from a localized string key.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func badge(_ key: LocalizedStringKey) -> some TabContent<Self.TabValue>
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func badge(_ resource: LocalizedStringResource) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func badge(_ count: Int) -> some TabContent<Self.TabValue>
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

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. The string provided will appear as an indicator on the given tab.

This modifier creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). For more information about localizing strings, see [`Text`](../text.md). The following example shows a tab that has a “New Alerts” badge when there are new alerts.

```swift
var body: some View {
    TabView {
        Tab("Home", systemImage: "house") {
            HomeView()
        }
        Tab("Alerts", systemImage: "bell") {
            AlertsView()
        }
        .badge("New Alerts")
    }
}
```

## Parameters

- `key`: A string key to display as a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/badge(_:)-7ggm4)*