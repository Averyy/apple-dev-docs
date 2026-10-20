# prepareForTransition(to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the layout object that it is about to be removed as the layout for the collection view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func prepareForTransition(to newLayout: UICollectionViewLayout)
```

```objc
- (void) prepareForTransitionToLayout:(UICollectionViewLayout *) newLayout;
```

#### Discussion

Prior to performing a layout transition, the collection view calls this method so that your layout object can perform any initial calculations needed to generate layout attributes.

## Parameters

- `newLayout`: The layout object to be installed in the collection view at the end of the transition. You might use this object to provide different starting attributes depending on the final layout object.

## See Also

### Transitioning between layouts
- [func prepareForTransition(from: UICollectionViewLayout)](./preparefortransition%28from%29.md)
  Tells the layout object to prepare to be installed as the layout for the collection view.
- [func finalizeLayoutTransition()](./finalizelayouttransition%28%29.md)
  Tells the layout object to perform any final steps before the transition animations occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/preparefortransition(to:))*