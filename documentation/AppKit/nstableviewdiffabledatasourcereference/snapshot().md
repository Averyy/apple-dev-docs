# snapshot()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a representation of the current state of the data in the table view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func snapshot() -> NSDiffableDataSourceSnapshotReference
```

```objc
- (NSDiffableDataSourceSnapshot<id,id> *) snapshot;
```

## Return Value

A snapshot that contains row and item identifiers in the order they appear in the UI.

## See Also

### Updating Data
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](./applysnapshot%28_,animatingdifferences%29.md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](./applysnapshot%28_,animatingdifferences,completion%29.md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [var defaultRowAnimation: NSTableView.AnimationOptions](./defaultrowanimation.md)
  The default animation the UI uses to show differences between rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/snapshot())*