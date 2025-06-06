# prepareForTransition(to:)

**Framework**: AppKit  
**Kind**: method

Prepares the layout object to be uninstalled from the collection view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func prepareForTransition(to newLayout: NSCollectionViewLayout)
```

#### Discussion

Prior to transitioning to a new layout object, the collection view calls this method on the old layout object to give it time to perform any cleanup operations.

## Parameters

- `newLayout`: The layout object to install in the collection view at the end of the transition.

## See Also

- [func prepareForTransition(from: NSCollectionViewLayout)](nscollectionviewlayout/preparefortransition(from:).md)
  Prepares the layout object to be installed in the collection view.
- [func finalizeLayoutTransition()](nscollectionviewlayout/finalizelayouttransition.md)
  Performs any final steps related to a layout transition before the transition animations actually occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/preparefortransition(to:))*