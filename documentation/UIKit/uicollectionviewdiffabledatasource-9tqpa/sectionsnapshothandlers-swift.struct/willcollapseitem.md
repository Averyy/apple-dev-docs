# willCollapseItem

**Framework**: UIKit  
**Kind**: property

The handler that prepares the diffable data source for collapsing an item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var willCollapseItem: ((ItemIdentifierType) -> Void)? { get set }
```

## See Also

- [var shouldCollapseItem: ((ItemIdentifierType) -> Bool)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldcollapseitem.md)
  The handler that determines whether a particular item is collapsable.
- [var shouldExpandItem: ((ItemIdentifierType) -> Bool)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldexpanditem.md)
  The handler that determines whether a particular item is expandable.
- [var willExpandItem: ((ItemIdentifierType) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willexpanditem.md)
  The handler that prepares the diffable data source for expanding an item.
- [var snapshotForExpandingParent: ((ItemIdentifierType, NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/snapshotforexpandingparent.md)
  The handler that provides the section snapshot for expanding the parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willcollapseitem)*