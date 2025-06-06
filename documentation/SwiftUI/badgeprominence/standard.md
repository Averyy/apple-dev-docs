# standard

**Framework**: SwiftUI  
**Kind**: property

The standard level of prominence for a badge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let standard: BadgeProminence
```

#### Discussion

This level of prominence should be used for badges that display a value that suggests user action, such as a count of unread messages or new invitations.

In lists on macOS, this results in a badge label on a grayscale platter; and in lists on iOS, this prominence of badge has no platter.

```swift
List(mailboxes) { mailbox in
    Text(mailbox.name)
        .badge(mailbox.numberOfUnreadMessages)
}
.badgeProminence(.standard)
```

## See Also

- [static let increased: BadgeProminence](badgeprominence/increased.md)
  The highest level of prominence for a badge.
- [static let decreased: BadgeProminence](badgeprominence/decreased.md)
  The lowest level of prominence for a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/badgeprominence/standard)*