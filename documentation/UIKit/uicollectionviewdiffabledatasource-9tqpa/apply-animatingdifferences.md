# apply(_:animatingDifferences:)

**Framework**: UIKit  
**Kind**: method

Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func apply(_ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool = true) async
```

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](uicollectionviewdiffabledatasource-9tqpa/snapshot.md)
  Returns a representation of the current state of the data in the collection view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](uicollectionviewdiffabledatasource-9tqpa/apply(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>) async](uicollectionviewdiffabledatasource-9tqpa/applysnapshotusingreloaddata(_:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, completion: (() -> Void)?)](uicollectionviewdiffabledatasource-9tqpa/applysnapshotusingreloaddata(_:completion:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:animatingdifferences:))*