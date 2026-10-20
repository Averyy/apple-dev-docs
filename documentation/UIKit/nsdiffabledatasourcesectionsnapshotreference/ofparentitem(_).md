# ofParentItem(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func ofParentItem(_ parentItem: Any) -> NSDiffableDataSourceSectionSnapshotReference
```

```objc
- (NSDiffableDataSourceSectionSnapshot<id> *) snapshotOfParentItem:(ItemIdentifierType) parentItem;
```

## See Also

### Creating a section snapshot
- [init()](./init%28%29.md)
  Creates an empty section snapshot.
- [func ofParentItem(Any, includingParentItem: Bool) -> NSDiffableDataSourceSectionSnapshotReference](./ofparentitem%28_,includingparentitem%29.md)
  Creates a section snapshot containing the child items of the specified parent item, including the parent item.
- [func appendItems([Any])](./appenditems%28_%29.md)
  Adds the specified items to the section snapshot.
- [func appendItems([Any], intoParentItem: Any?)](./appenditems%28_,intoparentitem%29.md)
  Adds the specified items as child items of the specified parent item in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/ofparentitem(_:))*