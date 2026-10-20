# UICollectionViewUpdateItem.Action

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the type of action being performed on an item.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Action
```

```c
enum UICollectionUpdateAction : NSInteger;
```

## Topics

### Constants
- [UICollectionViewUpdateItem.Action.none](./action/none.md)
- [UICollectionViewUpdateItem.Action.insert](./action/insert.md)
- [UICollectionViewUpdateItem.Action.delete](./action/delete.md)
- [UICollectionViewUpdateItem.Action.reload](./action/reload.md)
- [UICollectionViewUpdateItem.Action.move](./action/move.md)
### Initializers
- [init?(rawValue: Int)](./action/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the item changes
- [var indexPathBeforeUpdate: IndexPath?](./indexpathbeforeupdate.md)
  The index path of the item before the update.
- [var indexPathAfterUpdate: IndexPath?](./indexpathafterupdate.md)
  The index path of the item after the update.
- [var updateAction: UICollectionViewUpdateItem.Action](./updateaction.md)
  The action being performed on the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/action)*