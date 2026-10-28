# applySnapshot(_:animatingDifferences:completion:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (@Sendable () -> Void)? = nil)
```

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool) async
```

```objc
- (void) applySnapshot:(NSDiffableDataSourceSnapshot<id,id> *) snapshot animatingDifferences:(BOOL) animatingDifferences completion:(void (^)()) completion;
```

## Discussion

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the table view.
- `animatingDifferences`: If `true`, the diffable data source computes the difference between the table view’s current state and the new state in the snapshot, which is an O(n) operation, where n is the number of items in the snapshot. The system animates the differences in the UI between the current state and new state. If `false`, the system sets the table view UI to the new state without any animations, with no additional overhead for computing a diff. Any ongoing row animations are interrupted and the table view’s content immediately reloads.
- `completion`: The closure the system executes when the animations are complete. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## See Also

### Updating Data
- [func snapshot() -> NSDiffableDataSourceSnapshotReference](./snapshot%28%29.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](./applysnapshot%28_,animatingdifferences%29.md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.
- [var defaultRowAnimation: NSTableView.AnimationOptions](./defaultrowanimation.md)
  The default animation the UI uses to show differences between rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:))*