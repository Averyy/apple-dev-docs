# defaultRowAnimation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The default animation the UI uses to show differences between rows.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var defaultRowAnimation: NSTableView.AnimationOptions
```

#### Discussion

The default value of this property is [`effectFade`](../nstableview/animationoptions/effectfade.md).

If you set the value of this property, the new value becomes the default row animation for the next update that uses [`apply(_:animatingDifferences:completion:)`](./apply%28_,animatingdifferences,completion%29.md).

## See Also

### Updating Data
- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](./snapshot%28%29.md)
  Returns a representation of the current state of the data in the table view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](./apply%28_,animatingdifferences,completion%29.md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/defaultrowanimation)*