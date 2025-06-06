# NSView.LayerContentsRedrawPolicy.never

**Framework**: AppKit  
**Kind**: case

Leave the layer’s contents alone. Never mark the layer as needing display, or draw the view’s contents to the layer. This is how developer created layers (layer-hosting views) are treated.

**Availability**:
- macOS 10.6+

## Declaration

```swift
case never
```

## See Also

- [NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay](nsview/layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md)
  Any of the `setNeedsDisplay` methods sent to the view will cause the view redraw the affected layer parts by invoking the view’s [`draw(_:)`](nsview/draw(_:).md), but neither the layer or the view are marked as needing display when the view’s size changes.
- [NSView.LayerContentsRedrawPolicy.duringViewResize](nsview/layercontentsredrawpolicy-swift.enum/duringviewresize.md)
  Resize the view’s backing-layer and redraw the view to the layer when the view’s size changes. If the resize is animated, AppKit will drive the resize animation itself and will do this resize and redraw at each step of the animation. Affected parts of the layer will also be redrawn when the view is marked as needing display. This mode is a superset of [`NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay`](nsview/layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md). This is the way that layer-backed views are currently treated.
- [NSView.LayerContentsRedrawPolicy.beforeViewResize](nsview/layercontentsredrawpolicy-swift.enum/beforeviewresize.md)
  Resize the layer and redraw the view to the layer when the view’s size changes. This will be done just once at the beginning of a resize animation, not at each frame of the animation. Affected parts of the layer will also be redrawn when the view is marked as needing display. This mode is a superset of [`NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay`](nsview/layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md).
- [NSView.LayerContentsRedrawPolicy.crossfade](nsview/layercontentsredrawpolicy-swift.enum/crossfade.md)
  Redraw the layer contents at the new size and crossfade from the old contents to the new contents. Use this in conjunction with the [`NSView.LayerContentsPlacement`](nsview/layercontentsplacement-swift.enum.md) constants to get a nice crossfade animation for complex layer-backed views that cannot update correctly at each step of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layercontentsredrawpolicy-swift.enum/never)*