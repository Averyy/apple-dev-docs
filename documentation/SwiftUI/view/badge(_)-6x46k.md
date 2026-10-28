# badge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Generates a badge for the view from a string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func badge<S>(_ label: S?) -> some View where S : StringProtocol
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func badge(_ resource: LocalizedStringResource?) -> some View
```

```swift
nonisolated
func badge(_ count: Int) -> some View
```

```swift
nonisolated
func badge(_ key: LocalizedStringKey?) -> some View
```

```swift
nonisolated
func badge(_ label: Text?) -> some View
```

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

This modifier creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:)`](../text/init%28_%29-9d1g4.md). The following example shows a list with a “Default” badge on one of its rows.

```swift
NavigationView {
    List(servers) { server in
        Text(server.name)
            .badge(server.defaultString())
    }
    .navigationTitle("Servers")
}
```

![A table with the navigation title Servers and four rows: North 1,](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-badge-3@2x.png)

## Parameters

- `label`: An optional string to display as a badge. Set the value to `nil` to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/badge(_:)-6x46k)*