# badge(_:)

**Framework**: App Intents  
**Kind**: method

Generates a badge for the view from an integer value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func badge(_ count: Int) -> some View
```

#### Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear only in list rows, tab bars, and menus.

The following example shows a `List` with the value of `recentItems.count` represented by a badge on one of the rows:

```swift
List {
    Text("Recents")
        .badge(recentItems.count)
    Text("Favorites")
}
```

## Parameters

- `count`: An integer value to display in the badge.   Set the value to zero to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/badge(_:)-5hnb)*