# defaultRowAnimation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The default animation the UI uses to show differences between rows.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var defaultRowAnimation: NSTableView.AnimationOptions { get set }
```

```objc
@property NSTableViewAnimationOptions defaultRowAnimation;
```

## Discussion

The default value of this property is [`effectFade`](../nstableview/animationoptions/effectfade.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [`applySnapshot(_:animatingDifferences:)`](./applysnapshot%28_,animatingdifferences%29.md).

## See Also

### Updating Data
- [func snapshot() -> NSDiffableDataSourceSnapshotReference](./snapshot%28%29.md)
  Returns a representation of the current state of the data in the table view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](./applysnapshot%28_,animatingdifferences%29.md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](./applysnapshot%28_,animatingdifferences,completion%29.md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/defaultrowanimation)*