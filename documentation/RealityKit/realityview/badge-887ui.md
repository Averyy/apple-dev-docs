# badge(_:)

**Framework**: RealityKit  
**Kind**: method

Generates a badge for the view from an integer value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func badge(_ count: Int) -> some View
```

#### Discussion

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear only in list rows, tab bars, and menus.

The following example shows a `List` with the value of `recentItems.count` represented by a badge on one of the rows:

```None
List {
    Text("Recents")
        .badge(recentItems.count)
    Text("Favorites")
}
```

## Parameters

- `count`: An integer value to display in the badge.   Set the value to zero to hide the badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/badge(_:)-887ui)*