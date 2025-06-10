# finalizeLayoutTransition()

**Framework**: UIKit  
**Kind**: method

Tells the layout object to perform any final steps before the transition animations occur.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func finalizeLayoutTransition()
```

#### Discussion

The collection view calls this method after it has gathered all of the layout attributes needed to perform a transition from one layout to another. You can use this method to clean up any data structures or caches created by your implementations of the [`prepareForTransition(from:)`](uicollectionviewlayout/preparefortransition(from:).md) or [`prepareForTransition(to:)`](uicollectionviewlayout/preparefortransition(to:).md) methods.

## See Also

- [func prepareForTransition(from: UICollectionViewLayout)](uicollectionviewlayout/preparefortransition(from:).md)
  Tells the layout object to prepare to be installed as the layout for the collection view.
- [func prepareForTransition(to: UICollectionViewLayout)](uicollectionviewlayout/preparefortransition(to:).md)
  Tells the layout object that it is about to be removed as the layout for the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/finalizelayouttransition())*