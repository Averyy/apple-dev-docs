# apply(_:animatingDifferences:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func apply(_ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool = true, completion: (() -> Void)? = nil)
```

#### Discussion

The diffable data source computes the difference between the collection view’s current state and the new state in the applied snapshot, which is an O(*n*) operation, where *n* is the number of items in the snapshot.

You can safely call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the collection view.
- `animatingDifferences`: If [`true`](../../Swift/true.md), the system animates the updates to the collection view. If [`false`](../../Swift/false.md), the system doesn’t animate the updates to the collection view.
- `completion`: A closure to execute when the animations are complete. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## See Also

### Updating data
- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](./snapshot%28%29.md)
  Returns a representation of the current state of the data in the collection view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool) async](./apply%28_,animatingdifferences%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>) async](./applysnapshotusingreloaddata%28_%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, completion: (() -> Void)?)](./applysnapshotusingreloaddata%28_,completion%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:animatingdifferences:completion:))*