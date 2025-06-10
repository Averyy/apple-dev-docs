# defaultRowAnimation

**Framework**: AppKit  
**Kind**: property

The default animation the UI uses to show differences between rows.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var defaultRowAnimation: NSTableView.AnimationOptions { get set }
```

#### Discussion

The default value of this property is [`effectFade`](nstableview/animationoptions/effectfade.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [`applySnapshot(_:animatingDifferences:)`](nstableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md).

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshotReference](nstableviewdiffabledatasourcereference/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](nstableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](nstableviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/defaultrowanimation)*