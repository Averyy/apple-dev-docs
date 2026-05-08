# decreased

**Framework**: SwiftUI  
**Kind**: property

The lowest level of prominence for a badge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let decreased: BadgeProminence
```

#### Discussion

This level or prominence should be used for badges that display a value of passive information that requires no user action, such as total number of messages or content.

In lists on iOS and macOS, this results in badge labels being displayed without any extra decoration. On iOS, this looks the same as `.standard`.

```swift
List(folders) { folder in
    Text(folder.name)
        .badge(folder.numberOfItems)
}
.badgeProminence(.decreased)
```

## See Also

- [static let standard: BadgeProminence](badgeprominence/standard.md)
  The standard level of prominence for a badge.
- [static let increased: BadgeProminence](badgeprominence/increased.md)
  The highest level of prominence for a badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/badgeprominence/decreased)*