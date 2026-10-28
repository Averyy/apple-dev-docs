# resizeSublayers(withOldSize:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Informs the receiver’s sublayers that the receiver’s size has changed.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func resizeSublayers(withOldSize size: CGSize)
```

```objc
- (void) resizeSublayersWithOldSize:(CGSize) size;
```

## Discussion

When the [`autoresizingMask`](./autoresizingmask.md) property is used for resizing and the bounds of this layer change, the layer calls this method. The default implementation calls the [`resize(withOldSuperlayerSize:)`](./resize%28witholdsuperlayersize%29.md) method of each sublayer to let it know its superlayer’s bounds changed. You should not need to call or override this method directly.

## Parameters

- `size`: The previous size of the current layer.

## See Also

### Managing layer resizing and layout
- [var layoutManager: (any CALayoutManager)?](./layoutmanager.md)
  The object responsible for laying out the layer’s sublayers.
- [func setNeedsLayout()](./setneedslayout%28%29.md)
  Invalidates the layer’s layout and marks it as needing an update.
- [func layoutSublayers()](./layoutsublayers%28%29.md)
  Tells the layer to update its layout.
- [func layoutIfNeeded()](./layoutifneeded%28%29.md)
  Recalculate the receiver’s layout, if required.
- [func needsLayout() -> Bool](./needslayout%28%29.md)
  Returns a Boolean indicating whether the layer has been marked as needing a layout update.
- [var autoresizingMask: CAAutoresizingMask](./autoresizingmask.md)
  A bitmask defining how the layer is resized when the bounds of its superlayer changes.
- [func resize(withOldSuperlayerSize: CGSize)](./resize%28witholdsuperlayersize%29.md)
  Informs the receiver that the size of its superlayer changed.
- [func preferredFrameSize() -> CGSize](./preferredframesize%28%29.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/resizesublayers(witholdsize:))*