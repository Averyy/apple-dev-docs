# layoutManager

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

The object responsible for laying out the layer’s sublayers.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
var layoutManager: (any CALayoutManager)? { get set }
```

```objc
@property (strong, nullable) id<CALayoutManager> layoutManager;
```

## Discussion

The object you assign to this property must nominally implement the CALayoutManager Informal Protocol informal protocol. If the layer’s delegate does not handle layout updates, the object assigned to this property is given a chance to update the layout of the layer’s sublayers.

In macOS, assign an instance of the [`CAConstraintLayoutManager`](../caconstraintlayoutmanager.md) class to this property if your layer uses layer-based constraints to handle layout changes.

The default value of this property is `nil`.

## See Also

### Managing layer resizing and layout
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
- [func resizeSublayers(withOldSize: CGSize)](./resizesublayers%28witholdsize%29.md)
  Informs the receiver’s sublayers that the receiver’s size has changed.
- [func preferredFrameSize() -> CGSize](./preferredframesize%28%29.md)
  Returns the preferred size of the layer in the coordinate space of its superlayer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/layoutmanager)*