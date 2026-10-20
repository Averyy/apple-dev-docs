# updateAction

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The action being performed on the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var updateAction: UICollectionViewUpdateItem.Action { get }
```

```objc
@property (nonatomic, readonly) UICollectionUpdateAction updateAction;
```

#### Discussion

For a list of relevant action types, see [`UICollectionViewUpdateItem.Action`](./action.md).

## See Also

### Accessing the item changes
- [var indexPathBeforeUpdate: IndexPath?](./indexpathbeforeupdate.md)
  The index path of the item before the update.
- [var indexPathAfterUpdate: IndexPath?](./indexpathafterupdate.md)
  The index path of the item after the update.
- [UICollectionViewUpdateItem.Action](./action.md)
  Constants indicating the type of action being performed on an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem/updateaction)*