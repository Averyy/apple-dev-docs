# badgeProminence(_:)

**Framework**: Assignables  
**Kind**: method

Specifies the prominence of badges created by this view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func badgeProminence(_ prominence: BadgeProminence) -> some View
```

#### Discussion

Badges can be used for different kinds of information, from the passive number of items in a container to the number of required actions. The prominence of badges in Lists can be adjusted to reflect this and be made to draw more or less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a `List` displaying a list of folders with an informational badge with lower prominence, showing the number of items in the folder.

```None
List(folders) { folder in
    Text(folder.name)
        .badge(folder.numberOfItems)
}
.badgeProminence(.decreased)
```

## Parameters

- `prominence`: The prominence to apply to badges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/badgeprominence(_:))*