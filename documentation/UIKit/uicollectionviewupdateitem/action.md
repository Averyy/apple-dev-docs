# UICollectionViewUpdateItem.Action

**Framework**: UIKit  
**Kind**: enum

Constants indicating the type of action being performed on an item.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Action
```

## Topics

### Constants
- [UICollectionViewUpdateItem.Action.none](uicollectionviewupdateitem/action/none.md)
- [UICollectionViewUpdateItem.Action.insert](uicollectionviewupdateitem/action/insert.md)
- [UICollectionViewUpdateItem.Action.delete](uicollectionviewupdateitem/action/delete.md)
- [UICollectionViewUpdateItem.Action.reload](uicollectionviewupdateitem/action/reload.md)
- [UICollectionViewUpdateItem.Action.move](uicollectionviewupdateitem/action/move.md)
### Initializers
- [init?(rawValue: Int)](uicollectionviewupdateitem/action/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var indexPathBeforeUpdate: IndexPath?](uicollectionviewupdateitem/indexpathbeforeupdate.md)
  The index path of the item before the update.
- [var indexPathAfterUpdate: IndexPath?](uicollectionviewupdateitem/indexpathafterupdate.md)
  The index path of the item after the update.
- [var updateAction: UICollectionViewUpdateItem.Action](uicollectionviewupdateitem/updateaction.md)
  The action being performed on the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action)*