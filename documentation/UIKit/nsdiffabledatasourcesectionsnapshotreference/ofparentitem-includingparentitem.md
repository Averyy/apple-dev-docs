# ofParentItem(_:includingParentItem:)

**Framework**: UIKit  
**Kind**: method

Creates a section snapshot containing the child items of the specified parent item, including the parent item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func ofParentItem(_ parentItem: Any, includingParentItem: Bool) -> NSDiffableDataSourceSectionSnapshotReference
```

## See Also

- [init()](nsdiffabledatasourcesectionsnapshotreference/init.md)
  Creates an empty section snapshot.
- [func ofParentItem(Any) -> NSDiffableDataSourceSectionSnapshotReference](nsdiffabledatasourcesectionsnapshotreference/ofparentitem(_:).md)
  Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.
- [func appendItems([Any])](nsdiffabledatasourcesectionsnapshotreference/appenditems(_:).md)
  Adds the specified items to the section snapshot.
- [func appendItems([Any], intoParentItem: Any?)](nsdiffabledatasourcesectionsnapshotreference/appenditems(_:intoparentitem:).md)
  Adds the specified items as child items of the specified parent item in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/ofparentitem(_:includingparentitem:))*