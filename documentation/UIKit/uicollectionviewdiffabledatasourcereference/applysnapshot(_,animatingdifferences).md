# applySnapshot(_:animatingDifferences:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func applySnapshot(_ snapshot: NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)
```

```objc
- (void) applySnapshot:(NSDiffableDataSourceSnapshot<id,id> *) snapshot animatingDifferences:(BOOL) animatingDifferences;
```

#### Discussion

The diffable data source computes the difference between the collection view’s current state and the new state in the applied snapshot, which is an O(*n*) operation, where *n* is the number of items in the snapshot.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the collection view.
- `animatingDifferences`: If [`true`](../../Swift/true.md), the system animates the updates to the collection view. If [`false`](../../Swift/false.md), the system doesn’t animate the updates to the collection view.

## See Also

### Updating data
- [func snapshot() -> NSDiffableDataSourceSnapshotReference](./snapshot%28%29.md)
  Returns a representation of the current state of the data in the collection view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](./applysnapshot%28_,animatingdifferences,completion%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference)](./applysnapshot%28usingreloaddata%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)?)](./applysnapshot%28usingreloaddata,completion%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:))*