# secondaryItemIdentifiers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A set of identifiers corresponding to each item other than the primary item in a multiple-item interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var secondaryItemIdentifiers: Set<AnyHashable> { get set }
```

```objc
@property (nonatomic, copy) NSSet<id<NSCopying>> * secondaryItemIdentifiers;
```

## Mentions

- [Building a desktop-class iPad app](../building-a-desktop-class-ipad-app.md)

## Discussion

When the context menu acts on multiple items, you can use this property to include the identifiers of the secondary items in the configuration. You don’t need to set this property when you create a configuration that originates from a multiple-item interaction in a collection view, such as in [`collectionView(_:contextMenuConfigurationForItemsAt:point:)`](../uicollectionviewdelegate/collectionview%28_,contextmenuconfigurationforitemsat,point%29.md).

## See Also

### Handling multiple-item interactions
- [var badgeCount: Int](./badgecount.md)
  The number of items in a multiple-item interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/secondaryitemidentifiers)*