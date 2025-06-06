# secondaryItemIdentifiers

**Framework**: UIKit  
**Kind**: property

A set of identifiers corresponding to each item other than the primary item in a multiple-item interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var secondaryItemIdentifiers: Set<AnyHashable> { get set }
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Discussion

When the context menu acts on multiple items, you can use this property to include the identifiers of the secondary items in the configuration. You don’t need to set this property when you create a configuration that originates from a multiple-item interaction in a collection view, such as in [`collectionView(_:contextMenuConfigurationForItemsAt:point:)`](uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemsat:point:).md).

## See Also

- [var badgeCount: Int](uicontextmenuconfiguration/badgecount.md)
  The number of items in a multiple-item interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/secondaryitemidentifiers)*