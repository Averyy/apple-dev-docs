# autoresizingMask

**Framework**: Core Animation  
**Kind**: property

A bitmask defining how the layer is resized when the bounds of its superlayer changes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
var autoresizingMask: CAAutoresizingMask { get set }
```

#### Discussion

If your app does not use a layout manager or constraints to handle layout changes, you can assign a value to this property to adjust the layer’s size in response to changes in the superlayer’s bounds. For a list of possible values, see [`CAAutoresizingMask`](caautoresizingmask.md).

The default value of this property is [`kCALayerNotSizable`](caautoresizingmask/kcalayernotsizable.md).

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
- [func resize(withOldSuperlayerSize: CGSize)](calayer/resize(witholdsuperlayersize:).md)
  Informs the receiver that the size of its superlayer changed.
- [func resizeSublayers(withOldSize: CGSize)](calayer/resizesublayers(witholdsize:).md)
  Informs the receiver’s sublayers that the receiver’s size has changed.
- [func preferredFrameSize() -> CGSize](calayer/preferredframesize.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/autoresizingmask)*