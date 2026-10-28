# setCollectionViewLayout(_:animated:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Changes the collection view’s layout and notifies you when the animations complete.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setCollectionViewLayout(_ layout: UICollectionViewLayout, animated: Bool, completion: ((Bool) -> Void)? = nil)
```

```objc
- (void) setCollectionViewLayout:(UICollectionViewLayout *) layout animated:(BOOL) animated completion:(void (^)(BOOL finished)) completion;
```

## Discussion

This method initiates a layout change programmatically, notifying you when the transition is complete. If you choose to animate the layout change, the animation timing and parameters are controlled by the collection view.

## Parameters

- `layout`: The new layout object for the collection view.
- `animated`: Specify [`true`](../../Swift/true.md) if you want to animate changes from the current layout to the new layout specified by the `layout` parameter. Specify [`false`](../../Swift/false.md) to make the change without animations.
- `completion`: The block that’s executed when the layout transition finishes or is terminated by the user. This block takes the following parameter:

  - **finished**: A Boolean indicating whether the transition completed successfully. This parameter is [`true`](../../Swift/true.md) if the transition finished and the new layout is installed. It’s [`false`](../../Swift/false.md) if the user aborted the transition and returned to the old layout.

## See Also

### Changing the layout
- [var collectionViewLayout: UICollectionViewLayout](./collectionviewlayout.md)
  The layout used to organize the collected view’s items.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool)](./setcollectionviewlayout%28_,animated%29.md)
  Changes the collection view’s layout and optionally animates the change.
- [func startInteractiveTransition(to: UICollectionViewLayout, completion: UICollectionView.LayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout](./startinteractivetransition%28to,completion%29.md)
  Changes the collection view’s current layout using an interactive transition effect.
- [func finishInteractiveTransition()](./finishinteractivetransition%28%29.md)
  Tells the collection view to finish an interactive transition by installing the intended target layout.
- [func cancelInteractiveTransition()](./cancelinteractivetransition%28%29.md)
  Tells the collection view to cancel an interactive transition and return to its original layout object.
- [UICollectionView.LayoutInteractiveTransitionCompletion](./layoutinteractivetransitioncompletion.md)
  The completion block called at the end of an interactive transition for a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/setcollectionviewlayout(_:animated:completion:))*