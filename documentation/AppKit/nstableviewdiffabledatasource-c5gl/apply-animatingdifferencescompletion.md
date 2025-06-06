# apply(_:animatingDifferences:completion:)

**Framework**: AppKit  
**Kind**: method

Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func apply(_ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)? = nil)
```

## Parameters

- `snapshot`: The snapshot that reflects the new state of the data in the table view.
- `animatingDifferences`: If  , the diffable data source computes the difference between the table view’s current state and the new state in the snapshot, which is an O( ) operation, where   is the number of items in the snapshot. The system animates the differences in the UI between the current state and new state. If  , the system sets the table view UI to the new state without any animations, with no additional overhead for computing a diff. Any ongoing row animations are interrupted and the table view’s content immediately reloads.
- `completion`: The closure the system executes when the animations are complete. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nstableviewdiffabledatasource-c5gl/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [var defaultRowAnimation: NSTableView.AnimationOptions](nstableviewdiffabledatasource-c5gl/defaultrowanimation.md)
  The default animation the UI uses to show differences between rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/apply(_:animatingdifferences:completion:))*