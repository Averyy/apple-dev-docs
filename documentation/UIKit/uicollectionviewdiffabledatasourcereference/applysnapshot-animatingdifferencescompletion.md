# applySnapshot(_:animatingDifferences:completion:)

**Framework**: UIKit  
**Kind**: method

Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)? = nil)
```

#### Discussion

The diffable data source computes the difference between the collection view’s current state and the new state in the applied snapshot, which is an O(*n*) operation, where *n* is the number of items in the snapshot.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the collection view.
- `animatingDifferences`: If [`true`](https://developer.apple.com/documentation/Swift/true), the system animates the updates to the collection view. If [`false`](https://developer.apple.com/documentation/Swift/false), the system doesn’t animate the updates to the collection view.
- `completion`: A closure to execute when the animations are complete. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshotReference](uicollectionviewdiffabledatasourcereference/snapshot.md)
  Returns a representation of the current state of the data in the collection view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](uicollectionviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference)](uicollectionviewdiffabledatasourcereference/applysnapshot(usingreloaddata:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)?)](uicollectionviewdiffabledatasourcereference/applysnapshot(usingreloaddata:completion:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:completion:))*