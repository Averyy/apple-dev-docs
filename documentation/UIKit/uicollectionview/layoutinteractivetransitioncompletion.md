# UICollectionView.LayoutInteractiveTransitionCompletion

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The completion block called at the end of an interactive transition for a collection view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
typealias LayoutInteractiveTransitionCompletion = (Bool, Bool) -> Void
```

```c
typedef void (^)(_Bool, _Bool) UICollectionViewLayoutInteractiveTransitionCompletion;
```

## Discussion

This completion block takes the following parameters:

- **completed**: A Boolean indicating whether the animations ran to completion.
- **finish**: A Boolean indicating whether the transition finished or was canceled. This parameter is [`true`](../../Swift/true.md) if the transition ran to completion and the new layout is installed. It is [`false`](../../Swift/false.md) if the user canceled the transition and the old layout is installed.

## See Also

### Changing the layout
- [var collectionViewLayout: UICollectionViewLayout](./collectionviewlayout.md)
  The layout used to organize the collected view’s items.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool)](./setcollectionviewlayout%28_,animated%29.md)
  Changes the collection view’s layout and optionally animates the change.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool, completion: ((Bool) -> Void)?)](./setcollectionviewlayout%28_,animated,completion%29.md)
  Changes the collection view’s layout and notifies you when the animations complete.
- [func startInteractiveTransition(to: UICollectionViewLayout, completion: UICollectionView.LayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout](./startinteractivetransition%28to,completion%29.md)
  Changes the collection view’s current layout using an interactive transition effect.
- [func finishInteractiveTransition()](./finishinteractivetransition%28%29.md)
  Tells the collection view to finish an interactive transition by installing the intended target layout.
- [func cancelInteractiveTransition()](./cancelinteractivetransition%28%29.md)
  Tells the collection view to cancel an interactive transition and return to its original layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/layoutinteractivetransitioncompletion)*