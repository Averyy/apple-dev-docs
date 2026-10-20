# applySnapshot(_:toSection:animatingDifferences:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSectionSnapshotReference, toSection sectionIdentifier: Any, animatingDifferences: Bool)
```

```objc
- (void) applySnapshot:(NSDiffableDataSourceSectionSnapshot<id> *) snapshot toSection:(SectionIdentifierType) sectionIdentifier animatingDifferences:(BOOL) animatingDifferences;
```

## See Also

### Updating section data
- [func snapshot(forSection: Any) -> NSDiffableDataSourceSectionSnapshotReference](./snapshot%28forsection%29.md)
  Returns a representation of the current state of the data in the specified section of the collection view.
- [func applySnapshot(NSDiffableDataSourceSectionSnapshotReference, toSection: Any, animatingDifferences: Bool, completion: (() -> Void)?)](./applysnapshot%28_,tosection,animatingdifferences,completion%29.md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(_:tosection:animatingdifferences:))*