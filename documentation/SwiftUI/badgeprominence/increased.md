# increased

**Framework**: SwiftUI  
**Kind**: property

The highest level of prominence for a badge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let increased: BadgeProminence
```

#### Discussion

This level of prominence should be used for badges that display a value that requires user action, such as number of updates or account errors.

In lists on iOS and macOS, this results in badge labels being displayed on a red platter.

```swift
ForEach(accounts) { account in
    Text(account.userName)
        .badge(account.setupErrors)
        .badgeProminence(.increased)
}
```

## See Also

- [static let standard: BadgeProminence](badgeprominence/standard.md)
  The standard level of prominence for a badge.
- [static let decreased: BadgeProminence](badgeprominence/decreased.md)
  The lowest level of prominence for a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/badgeprominence/increased)*