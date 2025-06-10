# BadgeProminence

**Framework**: SwiftUI  
**Kind**: struct

The visual prominence of a badge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct BadgeProminence
```

#### Overview

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

## Topics

### Getting background prominence
- [static let standard: BadgeProminence](badgeprominence/standard.md)
  The standard level of prominence for a badge.
- [static let increased: BadgeProminence](badgeprominence/increased.md)
  The highest level of prominence for a badge.
- [static let decreased: BadgeProminence](badgeprominence/decreased.md)
  The lowest level of prominence for a badge.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func badge(_:)](view/badge(_:).md)
  Generates a badge for the view from an integer value.
- [func badgeProminence(BadgeProminence) -> some View](view/badgeprominence(_:).md)
  Specifies the prominence of badges created by this view.
- [var badgeProminence: BadgeProminence](environmentvalues/badgeprominence.md)
  The prominence to apply to badges associated with this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/badgeprominence)*