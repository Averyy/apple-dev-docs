# badge(_:)

**Framework**: SwiftUI  
**Kind**: method

Generates a badge for the view from a localized string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated func badge(_ resource: LocalizedStringResource?) -> some View
```

#### Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

This modifier creates a [`Text`](text.md) view on your behalf. For more information about localizing strings, see [`Text`](text.md). The following example shows a list with a “Default” badge on one of its rows.

```swift
NavigationView {
    List(servers) { server in
        Text(server.name)
            .badge(server.isDefault ? "Default" : nil)
    }
    .navigationTitle("Servers")
}
```

![A table with the navigation title Servers and four rows: North 1,](/images/com.apple.SwiftUI/View-badge-3@2x.png)

## Parameters

- `resource`: An optional string resource to display as a badge. Set the value to `nil` to hide the badge.

## See Also

- [func badgeProminence(BadgeProminence) -> some View](view/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [var badgeProminence: BadgeProminence](environmentvalues/badgeprominence.md)
  The prominence to apply to badges associated with this environment.
- [struct BadgeProminence](badgeprominence.md)
  The visual prominence of a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/badge(_:))*