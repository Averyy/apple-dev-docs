# UICollectionViewDiffableDataSourceSectionSnapshotHandlers

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Handlers for expanding and collapsing items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface UICollectionViewDiffableDataSourceSectionSnapshotHandlers : NSObject
```

## Topics

### Expanding and collapsing items
- [shouldCollapseItemHandler](./uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldcollapseitemhandler.md)
  The handler that determines whether a particular item is collapsable.
- [shouldExpandItemHandler](./uicollectionviewdiffabledatasourcesectionsnapshothandlers/shouldexpanditemhandler.md)
  The handler that determines whether a particular item is expandable.
- [willCollapseItemHandler](./uicollectionviewdiffabledatasourcesectionsnapshothandlers/willcollapseitemhandler.md)
  The handler that prepares the diffable data source for collapsing an item.
- [willExpandItemHandler](./uicollectionviewdiffabledatasourcesectionsnapshothandlers/willexpanditemhandler.md)
  The handler that prepares the diffable data source for expanding an item.
- [snapshotForExpandingParentItemHandler](./uicollectionviewdiffabledatasourcesectionsnapshothandlers/snapshotforexpandingparentitemhandler.md)
  The handler that provides the section snapshot for expanding the parent item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Supporting expanding and collapsing
- [var sectionSnapshotHandlers: __UICollectionViewDiffableDataSourceSectionSnapshotHandlers](./uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers.md)
  The diffable data source’s handlers for expanding and collapsing items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcesectionsnapshothandlers)*