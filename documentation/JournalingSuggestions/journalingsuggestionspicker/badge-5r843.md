# badge(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Generates a badge for the view from a localized string key.

**Availability**:
- iOS 15.0+
- macOS 12.0+

## Declaration

```swift
nonisolated
func badge(_ key: LocalizedStringKey?) -> some View
```

#### Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear only in list rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized key similar to `Text/init(_:tableName:bundle:comment:)`. For more information about localizing strings, see `Text`. The following example shows a list with a “Default” badge on one of its rows.

```None
NavigationView {
    List(servers) { server in
        Text(server.name)
            .badge(server.isDefault ? "Default" : nil)
    }
    .navigationTitle("Servers")
}
```

## Parameters

- `key`: An optional string key to display as a badge.   Set the value to   to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/badge(_:)-5r843)*