# prepareForTransition(from:)

**Framework**: AppKit  
**Kind**: method

Prepares the layout object to be installed in the collection view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func prepareForTransition(from oldLayout: NSCollectionViewLayout)
```

#### Discussion

Prior to transitioning to a new layout object, the collection view calls this method on the new layout object to give it time to perform any initial calculations.

## Parameters

- `oldLayout`: The layout object installed in the collection view at the beginning of the transition. You might use this object to retrieve the current layout attributes for items and views.

## See Also

- [func prepareForTransition(to: NSCollectionViewLayout)](nscollectionviewlayout/preparefortransition(to:).md)
  Prepares the layout object to be uninstalled from the collection view.
- [func finalizeLayoutTransition()](nscollectionviewlayout/finalizelayouttransition.md)
  Performs any final steps related to a layout transition before the transition animations actually occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/preparefortransition(from:))*