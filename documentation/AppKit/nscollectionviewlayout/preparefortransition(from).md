# prepareForTransition(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prepares the layout object to be installed in the collection view.

**Availability**:
- macOS

## Declaration

```swift
func prepareForTransition(from oldLayout: NSCollectionViewLayout)
```

```objc
- (void) prepareForTransitionFromLayout:(NSCollectionViewLayout *) oldLayout;
```

#### Discussion

Prior to transitioning to a new layout object, the collection view calls this method on the new layout object to give it time to perform any initial calculations.

## Parameters

- `oldLayout`: The layout object installed in the collection view at the beginning of the transition. You might use this object to retrieve the current layout attributes for items and views.

## See Also

### Transitioning Between Layouts
- [func prepareForTransition(to: NSCollectionViewLayout)](./preparefortransition%28to%29.md)
  Prepares the layout object to be uninstalled from the collection view.
- [func finalizeLayoutTransition()](./finalizelayouttransition%28%29.md)
  Performs any final steps related to a layout transition before the transition animations actually occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/preparefortransition(from:))*