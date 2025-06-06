# prepare(forAnimatedBoundsChange:)

**Framework**: AppKit  
**Kind**: method

Prepares the layout object for animated changes to the collection view’s bounds or for the insertion or deletion of items.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func prepare(forAnimatedBoundsChange oldBounds: NSRect)
```

#### Discussion

The default implementation of this method does nothing. The collection view calls this method before performing any animated changes to the collection view’s bounds. It also calls this method before the animated insertion or deletion of items. Subclasses can use this method to perform any calculations needed to prepare for animated changes. Specifically, you might use this method to calculate the initial or final positions of inserted or deleted items so that you can return those values when asked for them. You can also use this method to perform custom animations. Any animations you create are added to the animation block used to handle the insertions, deletions, and bounds changes.

## Parameters

- `oldBounds`: The current bounds of the collection view.

## See Also

- [func finalizeAnimatedBoundsChange()](nscollectionviewlayout/finalizeanimatedboundschange.md)
  Cleans up after any animated changes to the collection view’s bounds or after the insertion or deletion of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout/prepare(foranimatedboundschange:))*