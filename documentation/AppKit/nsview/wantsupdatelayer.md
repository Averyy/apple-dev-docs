# wantsUpdateLayer

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating which drawing path the view takes when updating its contents.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var wantsUpdateLayer: Bool { get }
```

```objc
@property (readonly) BOOL wantsUpdateLayer;
```

#### Discussion

A view can update its contents using one of two techniques. It can draw those contents using its [`draw(_:)`](./draw%28_%29.md) method or it can modify its underlying layer object directly. During the view update cycle, each dirty view calls this method on itself to determine which technique to use. The default implementation of this method returns [`false`](../../Swift/false.md), which causes the view to use its [`draw(_:)`](./draw%28_%29.md) method.

If your view is layer-backed and updates itself by modifying its layer, override this property and change the return value to [`true`](../../Swift/true.md). Modifying the layer is significantly faster than redrawing the layer contents using [`draw(_:)`](./draw%28_%29.md). If you override this property to be [`true`](../../Swift/true.md), you must also override the [`updateLayer()`](./updatelayer%28%29.md) method of your view and use it to make the changes to your layer. Do not modify your layer in your implementation of this property. Your implementation should return [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md) quickly and not perform other tasks.

If the [`canDrawSubviewsIntoLayer`](./candrawsubviewsintolayer.md) property is set to [`true`](../../Swift/true.md), the view ignores the value returned by this method. Instead, the view always uses its [`draw(_:)`](./draw%28_%29.md) method to draw its content.

> **Note**:  When using the [`updateLayer()`](./updatelayer%28%29.md) method to update your view, it is recommended that you set the view’s redraw policy to [`NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay`](./layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md). This policy lets you control when you want to update the layer’s contents.

## See Also

### Related Documentation
- [func updateLayer()](./updatelayer%28%29.md)
  Updates the view’s content by modifying its underlying layer.
### Managing the View’s Layer
- [var wantsLayer: Bool](./wantslayer.md)
  A Boolean value indicating whether the view uses a layer as its backing store.
- [var layer: CALayer?](./layer.md)
  The Core Animation layer that the view uses as its backing store.
- [func makeBackingLayer() -> CALayer](./makebackinglayer%28%29.md)
  Creates the view’s backing layer.
- [var layerContentsPlacement: NSView.LayerContentsPlacement](./layercontentsplacement-swift.property.md)
  The current layer contents placement policy.
- [NSView.LayerContentsPlacement](./layercontentsplacement-swift.enum.md)
  These constants specify the location of the layer content when the content is not rerendered in response to view resizing. For more information, see the [`layerContentsPlacement`](./layercontentsplacement-swift.property.md) property.
- [var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy](./layercontentsredrawpolicy-swift.property.md)
  The contents redraw policy for the view’s layer.
- [NSView.LayerContentsRedrawPolicy](./layercontentsredrawpolicy-swift.enum.md)
  Constants that specify how layer resizing is handled when a view is layer-backed or layer-hosting. For more information, see the  [`layerContentsRedrawPolicy`](./layercontentsredrawpolicy-swift.property.md) property.
- [var canDrawSubviewsIntoLayer: Bool](./candrawsubviewsintolayer.md)
  A Boolean value indicating whether the view incorporates content from its subviews into its own layer.
- [var layerUsesCoreImageFilters: Bool](./layerusescoreimagefilters.md)
  A Boolean value indicating whether the view’s layer uses Core Image filters and needs in-process rendering.
- [protocol NSViewLayerContentScaleDelegate](../nsviewlayercontentscaledelegate.md)
  An optional layer delegate method for handling resolution changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/wantsupdatelayer)*