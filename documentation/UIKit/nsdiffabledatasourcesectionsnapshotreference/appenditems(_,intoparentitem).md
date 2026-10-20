# appendItems(_:intoParentItem:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified items as child items of the specified parent item in the section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func appendItems(_ items: [Any], intoParentItem parentItem: Any?)
```

```objc
- (void) appendItems:(NSArray<id> *) items intoParentItem:(ItemIdentifierType) parentItem;
```

## Parameters

- `items`: The identifiers of the items to append to the parent item in the section snapshot.
- `parentItem`: The parent item to append the items to.

## See Also

### Creating a section snapshot
- [init()](./init%28%29.md)
  Creates an empty section snapshot.
- [func ofParentItem(Any) -> NSDiffableDataSourceSectionSnapshotReference](./ofparentitem%28_%29.md)
  Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.
- [func ofParentItem(Any, includingParentItem: Bool) -> NSDiffableDataSourceSectionSnapshotReference](./ofparentitem%28_,includingparentitem%29.md)
  Creates a section snapshot containing the child items of the specified parent item, including the parent item.
- [func appendItems([Any])](./appenditems%28_%29.md)
  Adds the specified items to the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/appenditems(_:intoparentitem:))*