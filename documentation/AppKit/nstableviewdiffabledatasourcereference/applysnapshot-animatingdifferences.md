# applySnapshot(_:animatingDifferences:)

**Framework**: AppKit  
**Kind**: method

Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)
```

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the table view.
- `animatingDifferences`: If  , the diffable data source computes the difference between the table view’s current state and the new state in the snapshot, which is an O(n) operation, where n is the number of items in the snapshot. The system animates the differences in the UI between the current state and new state. If  , the system sets the table view UI to the new state without any animations, with no additional overhead for computing a diff. Any ongoing row animations are interrupted and the table view’s content immediately reloads.

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshotReference](nstableviewdiffabledatasourcereference/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](nstableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [var defaultRowAnimation: NSTableView.AnimationOptions](nstableviewdiffabledatasourcereference/defaultrowanimation.md)
  The default animation the UI uses to show differences between rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:))*