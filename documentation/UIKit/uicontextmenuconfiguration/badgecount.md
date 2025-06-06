# badgeCount

**Framework**: UIKit  
**Kind**: property

The number of items in a multiple-item interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var badgeCount: Int { get set }
```

#### Discussion

The system uses this value to generate a badge for the stack of selected items to indicate how many items the menu is acting on. A value below `2` hides the badge. If you don’t set this value, the system determines it automatically.

## See Also

- [var secondaryItemIdentifiers: Set<AnyHashable>](uicontextmenuconfiguration/secondaryitemidentifiers.md)
  A set of identifiers corresponding to each item other than the primary item in a multiple-item interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/badgecount)*