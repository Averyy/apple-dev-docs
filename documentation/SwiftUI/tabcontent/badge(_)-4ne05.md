# badge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Generates a badge for the tab from a string.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func badge<S>(_ label: S) -> some TabContent<Self.TabValue> where S : StringProtocol
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
func badge(_ key: LocalizedStringKey) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func badge(_ label: Text?) -> some TabContent<Self.TabValue>
```

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. The string provided will appear as an indicator on the given tab.

This modifier creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:)`](../text/init%28_%29.md). The following example shows tabs that have the server name as their badge.

```swift
TabView {
    ForEach(servers) { server in
        Tab(server.name, image: server.icon) {
            ServerDetailView(for: server)
        }
        .badge(server.defaultString())
    }
}
```

## Parameters

- `label`: A string to display as a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/badge(_:)-4ne05)*