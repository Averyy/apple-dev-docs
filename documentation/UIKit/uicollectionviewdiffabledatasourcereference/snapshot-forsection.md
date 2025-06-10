# snapshot(forSection:)

**Framework**: UIKit  
**Kind**: method

Returns a representation of the current state of the data in the specified section of the collection view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func snapshot(forSection section: Any) -> NSDiffableDataSourceSectionSnapshotReference
```

## See Also

- [func applySnapshot(NSDiffableDataSourceSectionSnapshotReference, toSection: Any, animatingDifferences: Bool, completion: (() -> Void)?)](uicollectionviewdiffabledatasourcereference/applysnapshot(_:tosection:animatingdifferences:completion:).md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(NSDiffableDataSourceSectionSnapshotReference, toSection: Any, animatingDifferences: Bool)](uicollectionviewdiffabledatasourcereference/applysnapshot(_:tosection:animatingdifferences:).md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/snapshot(forsection:))*