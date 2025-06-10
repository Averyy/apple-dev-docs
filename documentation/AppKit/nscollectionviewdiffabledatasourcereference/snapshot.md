# snapshot()

**Framework**: AppKit  
**Kind**: method

Returns a representation of the current state of the data in the collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func snapshot() -> NSDiffableDataSourceSnapshotReference
```

#### Return Value

A snapshot containing section and item identifiers in the order that they appear in the UI.

## See Also

- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](nscollectionviewdiffabledatasourcereference/applysnapshot(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasourcereference/snapshot())*