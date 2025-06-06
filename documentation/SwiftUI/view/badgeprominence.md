# badgeProminence(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies the prominence of badges created by this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func badgeProminence(_ prominence: BadgeProminence) -> some View
```

#### Discussion

Badges can be used for different kinds of information, from the passive number of items in a container to the number of required actions. The prominence of badges in Lists can be adjusted to reflect this and be made to draw more or less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a [`List`](list.md) displaying a list of folders with an informational badge with lower prominence, showing the number of items in the folder.

```swift
List(folders) { folder in
    Text(folder.name)
        .badge(folder.numberOfItems)
}
.badgeProminence(.decreased)
```

## Parameters

- `prominence`: The prominence to apply to badges.

## See Also

- [func badge(_:)](view/badge(_:).md)
  Generates a badge for the view from an integer value.
- [var badgeProminence: BadgeProminence](environmentvalues/badgeprominence.md)
  The prominence to apply to badges associated with this environment.
- [struct BadgeProminence](badgeprominence.md)
  The visual prominence of a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/badgeprominence(_:))*