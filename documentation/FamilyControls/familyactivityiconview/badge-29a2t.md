# badge(_:)

**Framework**: FamilyControls  
**Kind**: method

Generates a badge for the view from a string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
nonisolated
func badge<S>(_ label: S?) -> some View where S : StringProtocol
```

#### Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized key similar to `Text/init(_:)-9d1g4`. The following example shows a list with a “Default” badge on one of its rows.

```swift
NavigationView {
    List(servers) { server in
        Text(server.name)
            .badge(server.defaultString())
    }
    .navigationTitle("Servers")
}
```

## Parameters

- `label`: An optional string to display as a badge.   Set the value to   to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/badge(_:)-29a2t)*