# badge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Generates a badge for the view from a localized string key.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func badge(_ key: LocalizedStringKey?) -> some View
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
func badge(_ label: Text?) -> some View
```

```swift
nonisolated
func badge<S>(_ label: S?) -> some View where S : StringProtocol
```

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

This modifier creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). For more information about localizing strings, see [`Text`](../text.md). The following example shows a list with a “Default” badge on one of its rows.

```swift
NavigationView {
    List(servers) { server in
        Text(server.name)
            .badge(server.isDefault ? "Default" : nil)
    }
    .navigationTitle("Servers")
}
```

![A table with the navigation title Servers and four rows: North 1,](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-badge-3@2x.png)

## Parameters

- `key`: An optional string key to display as a badge. Set the value to `nil` to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/badge(_:)-84e43)*