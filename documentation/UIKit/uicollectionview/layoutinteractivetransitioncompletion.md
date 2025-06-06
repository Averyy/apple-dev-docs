# UICollectionView.LayoutInteractiveTransitionCompletion

**Framework**: UIKit  
**Kind**: typealias

The completion block called at the end of an interactive transition for a collection view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias LayoutInteractiveTransitionCompletion = (Bool, Bool) -> Void
```

#### Discussion

This completion block takes the following parameters:

## See Also

- [var collectionViewLayout: UICollectionViewLayout](uicollectionview/collectionviewlayout.md)
  The layout used to organize the collected view’s items.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool)](uicollectionview/setcollectionviewlayout(_:animated:).md)
  Changes the collection view’s layout and optionally animates the change.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool, completion: ((Bool) -> Void)?)](uicollectionview/setcollectionviewlayout(_:animated:completion:).md)
  Changes the collection view’s layout and notifies you when the animations complete.
- [func startInteractiveTransition(to: UICollectionViewLayout, completion: UICollectionView.LayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout](uicollectionview/startinteractivetransition(to:completion:).md)
  Changes the collection view’s current layout using an interactive transition effect.
- [func finishInteractiveTransition()](uicollectionview/finishinteractivetransition.md)
  Tells the collection view to finish an interactive transition by installing the intended target layout.
- [func cancelInteractiveTransition()](uicollectionview/cancelinteractivetransition.md)
  Tells the collection view to cancel an interactive transition and return to its original layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/layoutinteractivetransitioncompletion)*