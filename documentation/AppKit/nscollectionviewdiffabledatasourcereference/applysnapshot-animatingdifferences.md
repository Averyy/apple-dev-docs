# applySnapshot(_:animatingDifferences:)

**Framework**: AppKit  
**Kind**: method

Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)
```

#### Discussion

It’s safe to call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## Parameters

- `snapshot`: The snapshot reflecting the new state of the data in the collection view.
- `animatingDifferences`: If  , the diffable data source computes the difference between the collection view’s current state and the new state in the snapshot, which is an O( ) operation, where   is the number of items in the snapshot. The differences in the UI between the current state and new state are animated. If  , the collection view UI is set to the new state without any animations, with no additional overhead for computing a diff. Any ongoing item animations are interrupted and the collection view’s content is reloaded immediately.

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshotReference](nscollectionviewdiffabledatasourcereference/snapshot.md)
  Returns a representation of the current state of the data in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:))*