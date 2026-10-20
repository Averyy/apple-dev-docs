# prepareForTransition(from:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the layout object to prepare to be installed as the layout for the collection view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func prepareForTransition(from oldLayout: UICollectionViewLayout)
```

```objc
- (void) prepareForTransitionFromLayout:(UICollectionViewLayout *) oldLayout;
```

#### Discussion

Prior to performing a layout transition, the collection view calls this method so that your layout object can perform any initial calculations needed to generate layout attributes.

## Parameters

- `oldLayout`: The layout object installed in the collection view at the beginning of the transition. You might use this object to provide different ending attributes based on the starting layout object.

## See Also

### Transitioning between layouts
- [func prepareForTransition(to: UICollectionViewLayout)](./preparefortransition%28to%29.md)
  Tells the layout object that it is about to be removed as the layout for the collection view.
- [func finalizeLayoutTransition()](./finalizelayouttransition%28%29.md)
  Tells the layout object to perform any final steps before the transition animations occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/preparefortransition(from:))*