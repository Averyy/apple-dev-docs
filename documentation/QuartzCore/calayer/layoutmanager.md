# layoutManager

**Framework**: Core Animation  
**Kind**: property

The object responsible for laying out the layer’s sublayers.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
var layoutManager: (any CALayoutManager)? { get set }
```

#### Discussion

The object you assign to this property must nominally implement the CALayoutManager Informal Protocol informal protocol. If the layer’s delegate does not handle layout updates, the object assigned to this property is given a chance to update the layout of the layer’s sublayers.

In macOS, assign an instance of the [`CAConstraintLayoutManager`](caconstraintlayoutmanager.md) class to this property if your layer uses layer-based constraints to handle layout changes.

The default value of this property is `nil`.

## See Also

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
- [func resizeSublayers(withOldSize: CGSize)](calayer/resizesublayers(witholdsize:).md)
  Informs the receiver’s sublayers that the receiver’s size has changed.
- [func preferredFrameSize() -> CGSize](calayer/preferredframesize.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/layoutmanager)*