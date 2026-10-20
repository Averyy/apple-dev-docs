# collectionView(_:didUpdateFocusIn:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a focus update occurred.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, didUpdateFocusIn context: UICollectionViewFocusUpdateContext, with coordinator: UIFocusAnimationCoordinator)
```

```objc
- (void) collectionView:(UICollectionView *) collectionView didUpdateFocusInContext:(UICollectionViewFocusUpdateContext *) context withAnimationCoordinator:(UIFocusAnimationCoordinator *) coordinator;
```

#### Discussion

The collection view calls this method when a focus-related change occurs. You can use this method to update your app’s state information or to animate changes to your app’s visual appearance.

If you subclass [`UICollectionView`](../uicollectionview.md), you can also implement the same behavior by overriding the [`didUpdateFocus(in:with:)`](../uifocusenvironment/didupdatefocus%28in,with%29.md) method, which is defined by the [`UIFocusEnvironment`](../uifocusenvironment.md) protocol and adopted by all views.

## Parameters

- `collectionView`: The collection view object notifying you of the focus change.
- `context`: The context object containing metadata associated with the focus change. This object contains the index path of the previously focused item and the currently focused item.
- `coordinator`: The animation coordinator to use when creating any additional animations.

## See Also

### Related Documentation
- [func didUpdateFocus(in: UIFocusUpdateContext, with: UIFocusAnimationCoordinator)](../uifocusenvironment/didupdatefocus%28in,with%29.md)
  Called immediately after the system updates the focus to a new view.
### Working with focus
- [func collectionView(UICollectionView, canFocusItemAt: IndexPath) -> Bool](./collectionview%28_,canfocusitemat%29.md)
  Asks the delegate whether the item at the specified index path can be focused.
- [func indexPathForPreferredFocusedView(in: UICollectionView) -> IndexPath?](./indexpathforpreferredfocusedview%28in%29.md)
  Asks the delegate for the index path of the cell that should be focused.
- [func collectionView(UICollectionView, shouldUpdateFocusIn: UICollectionViewFocusUpdateContext) -> Bool](./collectionview%28_,shouldupdatefocusin%29.md)
  Asks the delegate whether a change in focus should occur.
- [func collectionView(UICollectionView, selectionFollowsFocusForItemAt: IndexPath) -> Bool](./collectionview%28_,selectionfollowsfocusforitemat%29.md)
  Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didupdatefocusin:with:))*