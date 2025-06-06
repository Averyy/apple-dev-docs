# apply(_:animatingDifferences:completion:)

**Framework**: AppKit  
**Kind**: method

Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
func apply(_ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool = true, completion: (() -> Void)? = nil)
```

#### Discussion

It’s safe to call this method from a background queue, but you must do so consistently in your app. Always call this method exclusively from the main queue or from a background queue.

## Parameters

- `snapshot`: The snapshot reflecting the new state of the data in the collection view.
- `animatingDifferences`: If  , the diffable data source computes the difference between the collection view’s current state and the new state in the snapshot, which is an O( ) operation, where   is the number of items in the snapshot. The differences in the UI between the current state and new state are animated. If  , the collection view UI is set to the new state without any animations, with no additional overhead for computing a diff. Any ongoing item animations are interrupted and the collection view’s content is reloaded immediately.
- `completion`: A closure to be executed when the animations are complete. This closure has no return value and takes no parameters. The system calls this closure from the main queue.

## See Also

- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nscollectionviewdiffabledatasource-axww/snapshot.md)
  Returns a representation of the current state of the data in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasource-axww/apply(_:animatingdifferences:completion:))*