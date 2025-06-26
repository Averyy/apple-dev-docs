# badge(_:)

**Framework**: FamilyControls  
**Kind**: method

Generates a badge for the view from a localized string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Declaration

```swift
nonisolated
func badge(_ resource: LocalizedStringResource?) -> some View
```

#### Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

This modifier creates a `Text` view on your behalf. For more information about localizing strings, see `Text`. The following example shows a list with a “Default” badge on one of its rows.

```swift
NavigationView {
    List(servers) { server in
        Text(server.name)
            .badge(server.isDefault ? "Default" : nil)
    }
    .navigationTitle("Servers")
}
```

## Parameters

- `key`: An optional string resource to display as a badge.   Set the value to   to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitytitleview/badge(_:)-5bs8w)*