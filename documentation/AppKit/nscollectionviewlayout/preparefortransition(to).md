# prepareForTransition(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Prepares the layout object to be uninstalled from the collection view.

**Availability**:
- macOS

## Declaration

```swift
func prepareForTransition(to newLayout: NSCollectionViewLayout)
```

```objc
- (void) prepareForTransitionToLayout:(NSCollectionViewLayout *) newLayout;
```

#### Discussion

Prior to transitioning to a new layout object, the collection view calls this method on the old layout object to give it time to perform any cleanup operations.

## Parameters

- `newLayout`: The layout object to install in the collection view at the end of the transition.

## See Also

### Transitioning Between Layouts
- [func prepareForTransition(from: NSCollectionViewLayout)](./preparefortransition%28from%29.md)
  Prepares the layout object to be installed in the collection view.
- [func finalizeLayoutTransition()](./finalizelayouttransition%28%29.md)
  Performs any final steps related to a layout transition before the transition animations actually occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/preparefortransition(to:))*