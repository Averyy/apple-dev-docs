# badge(_:)

**Framework**: SwiftUI  
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

Use a badge to convey optional, supplementary information about a view. Keep the contents of the badge as short as possible. Badges appear in list rows, tab bars, toolbar items, and menus.

The following example shows a [`List`](list.md) with the value of `recentItems.count` represented by a badge on one of the rows:

```swift
List {
    Text("Recents")
        .badge(recentItems.count)
    Text("Favorites")
}
```

![A table with two rows, titled Recents and Favorites. The first row](https://docs-assets.developer.apple.com/published/03aa91169bc0d258ef5a38938b3dea5e/View-badge-1%402x.png)

## Parameters

- `count`: An integer value to display in the badge.   Set the value to zero to hide the badge.

## See Also

- [func badgeProminence(BadgeProminence) -> some View](view/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [var badgeProminence: BadgeProminence](environmentvalues/badgeprominence.md)
  The prominence to apply to badges associated with this environment.
- [struct BadgeProminence](badgeprominence.md)
  The visual prominence of a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/badge(_:))*