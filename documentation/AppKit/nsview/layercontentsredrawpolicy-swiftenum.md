# NSView.LayerContentsRedrawPolicy

**Framework**: AppKit  
**Kind**: enum

Constants that specify how layer resizing is handled when a view is layer-backed or layer-hosting. For more information, see the  [`layerContentsRedrawPolicy`](nsview/layercontentsredrawpolicy-swift.property.md) property.

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum LayerContentsRedrawPolicy
```

## Topics

### Constants
- [NSView.LayerContentsRedrawPolicy.never](nsview/layercontentsredrawpolicy-swift.enum/never.md)
  Leave the layer’s contents alone. Never mark the layer as needing display, or draw the view’s contents to the layer. This is how developer created layers (layer-hosting views) are treated.
- [NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay](nsview/layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md)
  Any of the `setNeedsDisplay` methods sent to the view will cause the view redraw the affected layer parts by invoking the view’s [`draw(_:)`](nsview/draw(_:).md), but neither the layer or the view are marked as needing display when the view’s size changes.
- [NSView.LayerContentsRedrawPolicy.duringViewResize](nsview/layercontentsredrawpolicy-swift.enum/duringviewresize.md)
  Resize the view’s backing-layer and redraw the view to the layer when the view’s size changes. If the resize is animated, AppKit will drive the resize animation itself and will do this resize and redraw at each step of the animation. Affected parts of the layer will also be redrawn when the view is marked as needing display. This mode is a superset of [`NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay`](nsview/layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md). This is the way that layer-backed views are currently treated.
- [NSView.LayerContentsRedrawPolicy.beforeViewResize](nsview/layercontentsredrawpolicy-swift.enum/beforeviewresize.md)
  Resize the layer and redraw the view to the layer when the view’s size changes. This will be done just once at the beginning of a resize animation, not at each frame of the animation. Affected parts of the layer will also be redrawn when the view is marked as needing display. This mode is a superset of [`NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay`](nsview/layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md).
- [NSView.LayerContentsRedrawPolicy.crossfade](nsview/layercontentsredrawpolicy-swift.enum/crossfade.md)
  Redraw the layer contents at the new size and crossfade from the old contents to the new contents. Use this in conjunction with the [`NSView.LayerContentsPlacement`](nsview/layercontentsplacement-swift.enum.md) constants to get a nice crossfade animation for complex layer-backed views that cannot update correctly at each step of the animation.
### Initializers
- [init?(rawValue: Int)](nsview/layercontentsredrawpolicy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var wantsLayer: Bool](nsview/wantslayer.md)
  A Boolean value indicating whether the view uses a layer as its backing store.
- [var wantsUpdateLayer: Bool](nsview/wantsupdatelayer.md)
  A Boolean value indicating which drawing path the view takes when updating its contents.
- [var layer: CALayer?](nsview/layer.md)
  The Core Animation layer that the view uses as its backing store.
- [func makeBackingLayer() -> CALayer](nsview/makebackinglayer.md)
  Creates the view’s backing layer.
- [var layerContentsPlacement: NSView.LayerContentsPlacement](nsview/layercontentsplacement-swift.property.md)
  The current layer contents placement policy.
- [NSView.LayerContentsPlacement](nsview/layercontentsplacement-swift.enum.md)
  These constants specify the location of the layer content when the content is not rerendered in response to view resizing. For more information, see the [`layerContentsPlacement`](nsview/layercontentsplacement-swift.property.md) property.
- [var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy](nsview/layercontentsredrawpolicy-swift.property.md)
  The contents redraw policy for the view’s layer.
- [var canDrawSubviewsIntoLayer: Bool](nsview/candrawsubviewsintolayer.md)
  A Boolean value indicating whether the view incorporates content from its subviews into its own layer.
- [var layerUsesCoreImageFilters: Bool](nsview/layerusescoreimagefilters.md)
  A Boolean value indicating whether the view’s layer uses Core Image filters and needs in-process rendering.
- [protocol NSViewLayerContentScaleDelegate](nsviewlayercontentscaledelegate.md)
  An optional layer delegate method for handling resolution changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layercontentsredrawpolicy-swift.enum)*