# autoresizingMask

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A bitmask defining how the layer is resized when the bounds of its superlayer changes.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
var autoresizingMask: CAAutoresizingMask { get set }
```

```objc
@property CAAutoresizingMask autoresizingMask;
```

## Discussion

If your app does not use a layout manager or constraints to handle layout changes, you can assign a value to this property to adjust the layer’s size in response to changes in the superlayer’s bounds. For a list of possible values, see [`CAAutoresizingMask`](../caautoresizingmask.md).

The default value of this property is [`kCALayerNotSizable`](../caautoresizingmask/kcalayernotsizable.md).

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
- [func resize(withOldSuperlayerSize: CGSize)](./resize%28witholdsuperlayersize%29.md)
  Informs the receiver that the size of its superlayer changed.
- [func resizeSublayers(withOldSize: CGSize)](./resizesublayers%28witholdsize%29.md)
  Informs the receiver’s sublayers that the receiver’s size has changed.
- [func preferredFrameSize() -> CGSize](./preferredframesize%28%29.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/autoresizingmask)*