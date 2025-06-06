# collectionViewLayout

**Framework**: UIKit  
**Kind**: property

The layout used to organize the collected view’s items.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var collectionViewLayout: UICollectionViewLayout { get set }
```

#### Discussion

Assigning a new layout object to this property causes the new layout to be applied (without animations) to the collection view’s items.

For more information, see [`Layouts`](uicollectionview#Layouts.md).

## See Also

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
- [UICollectionView.LayoutInteractiveTransitionCompletion](uicollectionview/layoutinteractivetransitioncompletion.md)
  The completion block called at the end of an interactive transition for a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/collectionviewlayout)*