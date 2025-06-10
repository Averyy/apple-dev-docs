# resize(withOldSuperlayerSize:)

**Framework**: Core Animation  
**Kind**: method

Informs the receiver that the size of its superlayer changed.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func resize(withOldSuperlayerSize size: CGSize)
```

#### Discussion

When the [`autoresizingMask`](calayer/autoresizingmask.md) property is used for resizing and the bounds of a layer change, that layer calls this method on each of its sublayers. Sublayers use this method to adjust their own frame rectangles to reflect the new superlayer bounds, which can be retrieved directly from the superlayer. The old size of the superlayer is passed to this method so that the sublayer has that information for any calculations it must make.

## Parameters

- `size`: The previous size of the superlayer.

## See Also

- [var layoutManager: (any CALayoutManager)?](calayer/layoutmanager.md)
  The object responsible for laying out the layer’s sublayers.
- [func setNeedsLayout()](calayer/setneedslayout.md)
  Invalidates the layer’s layout and marks it as needing an update.
- [func layoutSublayers()](calayer/layoutsublayers.md)
  Tells the layer to update its layout.
- [func layoutIfNeeded()](calayer/layoutifneeded.md)
  Recalculate the receiver’s layout, if required.
- [func needsLayout() -> Bool](calayer/needslayout.md)
  Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [var autoresizingMask: CAAutoresizingMask](calayer/autoresizingmask.md)
  A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [func resizeSublayers(withOldSize: CGSize)](calayer/resizesublayers(witholdsize:).md)
  Informs the receiver’s sublayers that the receiver’s size has changed.
- [func preferredFrameSize() -> CGSize](calayer/preferredframesize.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/resize(witholdsuperlayersize:))*