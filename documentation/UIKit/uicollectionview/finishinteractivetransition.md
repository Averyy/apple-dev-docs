# finishInteractiveTransition()

**Framework**: UIKit  
**Kind**: method

Tells the collection view to finish an interactive transition by installing the intended target layout.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func finishInteractiveTransition()
```

#### Discussion

Call this method after a call to the [`startInteractiveTransition(to:completion:)`](uicollectionview/startinteractivetransition(to:completion:).md) method and after you determine through a gesture recognizer or other event-handling code that the user wants to transition to the new layout. This method removes the intermediate transition layout object from the collection view and installs the intended target layout object. It then performs any final animations to get the collection view’s items from their current positions to the positions specified by the newly installed layout object.

After calling this method, you can also remove the gesture recognizer or event-handling code you installed to manage the interactive portions of the transition.

## See Also

- [var collectionViewLayout: UICollectionViewLayout](uicollectionview/collectionviewlayout.md)
  The layout used to organize the collected view’s items.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool)](uicollectionview/setcollectionviewlayout(_:animated:).md)
  Changes the collection view’s layout and optionally animates the change.
- [func setCollectionViewLayout(UICollectionViewLayout, animated: Bool, completion: ((Bool) -> Void)?)](uicollectionview/setcollectionviewlayout(_:animated:completion:).md)
  Changes the collection view’s layout and notifies you when the animations complete.
- [func startInteractiveTransition(to: UICollectionViewLayout, completion: UICollectionView.LayoutInteractiveTransitionCompletion?) -> UICollectionViewTransitionLayout](uicollectionview/startinteractivetransition(to:completion:).md)
  Changes the collection view’s current layout using an interactive transition effect.
- [func cancelInteractiveTransition()](uicollectionview/cancelinteractivetransition.md)
  Tells the collection view to cancel an interactive transition and return to its original layout object.
- [UICollectionView.LayoutInteractiveTransitionCompletion](uicollectionview/layoutinteractivetransitioncompletion.md)
  The completion block called at the end of an interactive transition for a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/finishinteractivetransition())*