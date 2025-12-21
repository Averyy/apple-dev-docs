# indexPathForPreferredFocusedView(in:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the index path of the cell that should be focused.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func indexPathForPreferredFocusedView(in collectionView: UICollectionView) -> IndexPath?
```

#### Return Value

The index path of the preferred cell. The index path you specify must correspond to a valid cell in the collection view.

#### Discussion

When focus is about to change to a collection view, the collection view must pick which of its subviews should receive that focus. If the collection view’s [`remembersLastFocusedIndexPath`](uitableview/rememberslastfocusedindexpath.md) property is set to [`true`](https://developer.apple.com/documentation/Swift/true), the collection view returns the index path of the cell that was last focused. If the [`remembersLastFocusedIndexPath`](uitableview/rememberslastfocusedindexpath.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), or if there is no saved index path because no cell was previously focused, the collection view calls this method so that you can specify which cell should receive focus. If you do not implement this method, the collection view returns an appropriate cell.

The effects of this method may be ignored during or immediately after a view controller transition, such as a presentation dismissal or navigation stack pop. In such cases, the view controller attempts to restore focus to the item that was focused prior to the transition (for example, prior to the view controller being presented or pushed), which can take precedence over the effects of this method. To learn how to control or disable this behavior in the view controller, see [`restoresFocusAfterTransition`](uiviewcontroller/restoresfocusaftertransition.md).

If you subclass [`UICollectionView`](uicollectionview.md), you can also implement the same behavior by overriding the [`preferredFocusEnvironments`](uifocusenvironment/preferredfocusenvironments.md) property, which is defined by the [`UIFocusEnvironment`](uifocusenvironment.md) protocol and adopted by all views.

## Parameters

- `collectionView`: The collection view object requesting this information.

## See Also

- [var preferredFocusedView: UIView?](uifocusenvironment/preferredfocusedview.md)
  Specifies the view that should be focused if this environment is focused.
- [func collectionView(UICollectionView, canFocusItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:canfocusitemat:).md)
  Asks the delegate whether the item at the specified index path can be focused.
- [func collectionView(UICollectionView, shouldUpdateFocusIn: UICollectionViewFocusUpdateContext) -> Bool](uicollectionviewdelegate/collectionview(_:shouldupdatefocusin:).md)
  Asks the delegate whether a change in focus should occur.
- [func collectionView(UICollectionView, didUpdateFocusIn: UICollectionViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](uicollectionviewdelegate/collectionview(_:didupdatefocusin:with:).md)
  Tells the delegate that a focus update occurred.
- [func collectionView(UICollectionView, selectionFollowsFocusForItemAt: IndexPath) -> Bool](uicollectionviewdelegate/collectionview(_:selectionfollowsfocusforitemat:).md)
  Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/indexpathforpreferredfocusedview(in:))*