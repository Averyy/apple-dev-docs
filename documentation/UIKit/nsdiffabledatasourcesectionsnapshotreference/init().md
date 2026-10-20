# init()

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an empty section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## See Also

### Creating a section snapshot
- [func ofParentItem(Any) -> NSDiffableDataSourceSectionSnapshotReference](./ofparentitem%28_%29.md)
  Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.
- [func ofParentItem(Any, includingParentItem: Bool) -> NSDiffableDataSourceSectionSnapshotReference](./ofparentitem%28_,includingparentitem%29.md)
  Creates a section snapshot containing the child items of the specified parent item, including the parent item.
- [func appendItems([Any])](./appenditems%28_%29.md)
  Adds the specified items to the section snapshot.
- [func appendItems([Any], intoParentItem: Any?)](./appenditems%28_,intoparentitem%29.md)
  Adds the specified items as child items of the specified parent item in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/init())*