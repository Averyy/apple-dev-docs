# resizeSublayers(withOldSize:)

**Framework**: Core Animation  
**Kind**: method

Informs the receiver’s sublayers that the receiver’s size has changed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func resizeSublayers(withOldSize size: CGSize)
```

#### Discussion

When the [`autoresizingMask`](calayer/autoresizingmask.md) property is used for resizing and the bounds of this layer change, the layer calls this method. The default implementation calls the [`resize(withOldSuperlayerSize:)`](calayer/resize(witholdsuperlayersize:).md) method of each sublayer to let it know its superlayer’s bounds changed. You should not need to call or override this method directly.

## Parameters

- `size`: The previous size of the current layer.

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
- [func resize(withOldSuperlayerSize: CGSize)](calayer/resize(witholdsuperlayersize:).md)
  Informs the receiver that the size of its superlayer changed.
- [func preferredFrameSize() -> CGSize](calayer/preferredframesize.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/resizesublayers(witholdsize:))*