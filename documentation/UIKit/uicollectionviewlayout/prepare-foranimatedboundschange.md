# prepare(forAnimatedBoundsChange:)

**Framework**: UIKit  
**Kind**: method

Prepares the layout object for animated changes to the view’s bounds or the insertion or deletion of items.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func prepare(forAnimatedBoundsChange oldBounds: CGRect)
```

#### Discussion

The collection view calls this method before performing any animated changes to the view’s bounds or before the animated insertion or deletion of items. This method is the layout object’s opportunity to perform any calculations needed to prepare for those animated changes. Specifically, you might use this method to calculate the initial or final positions of inserted or deleted items so that you can return those values when asked for them.

You can also use this method to perform additional animations. Any animations you create are added to the animation block used to handle the insertions, deletions, and bounds changes.

## Parameters

- `oldBounds`: The current bounds of the collection view.

## See Also

- [func finalizeAnimatedBoundsChange()](uicollectionviewlayout/finalizeanimatedboundschange.md)
  Cleans up after any animated changes to the view’s bounds or after the insertion or deletion of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/prepare(foranimatedboundschange:))*