# collectionViewLayout

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The layout used to organize the collected view’s items.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var collectionViewLayout: UICollectionViewLayout { get set }
```

```objc
@property (nonatomic, strong) UICollectionViewLayout * collectionViewLayout;
```

#### Discussion

Assigning a new layout object to this property causes the new layout to be applied (without animations) to the collection view’s items.

For more information, see [Layouts](../uicollectionview.md#Layouts).

## See Also

### Changing the layout
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
- [UICollectionView.LayoutInteractiveTransitionCompletion](./layoutinteractivetransitioncompletion.md)
  The completion block called at the end of an interactive transition for a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/collectionviewlayout)*