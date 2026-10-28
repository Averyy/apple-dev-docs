# setCollectionViewLayout(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Changes the collection view’s layout and optionally animates the change.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated: Bool)
```

```objc
- (void) setCollectionViewLayout:(UICollectionViewLayout *) layout animated:(BOOL) animated;
```

## Discussion

This method makes the layout change without further interaction from the user. If you choose to animate the layout change, the animation timing and parameters are controlled by the collection view.

## Parameters

- `layout`: The new layout object for the collection view.
- `animated`: Specify [`true`](../../Swift/true.md) if you want to animate changes from the current layout to the new layout specified by the `layout` parameter. Specify [`false`](../../Swift/false.md) to make the change without animations.

## See Also

### Changing the layout
- [var collectionViewLayout: UICollectionViewLayout](./collectionviewlayout.md)
  The layout used to organize the collected view’s items.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool, completion: ((Bool) -> Void)?)](./setcollectionviewlayout%28_,animated,completion%29.md)
  Changes the collection view’s layout and notifies you when the animations complete.
- [func startInteractiveTransition(to: UICollectionViewLayout, completion: UICollectionView.LayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout](./startinteractivetransition%28to,completion%29.md)
  Changes the collection view’s current layout using an interactive transition effect.
- [func finishInteractiveTransition()](./finishinteractivetransition%28%29.md)
  Tells the collection view to finish an interactive transition by installing the intended target layout.
- [func cancelInteractiveTransition()](./cancelinteractivetransition%28%29.md)
  Tells the collection view to cancel an interactive transition and return to its original layout object.
- [UICollectionView.LayoutInteractiveTransitionCompletion](./layoutinteractivetransitioncompletion.md)
  The completion block called at the end of an interactive transition for a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/setcollectionviewlayout(_:animated:))*