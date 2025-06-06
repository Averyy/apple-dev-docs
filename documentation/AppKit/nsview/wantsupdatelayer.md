# wantsUpdateLayer

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating which drawing path the view takes when updating its contents.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var wantsUpdateLayer: Bool { get }
```

#### Discussion

A view can update its contents using one of two techniques. It can draw those contents using its [`draw(_:)`](nsview/draw(_:).md) method or it can modify its underlying layer object directly. During the view update cycle, each dirty view calls this method on itself to determine which technique to use. The default implementation of this method returns [`false`](https://developer.apple.com/documentation/swift/false), which causes the view to use its [`draw(_:)`](nsview/draw(_:).md) method.

If your view is layer-backed and updates itself by modifying its layer, override this property and change the return value to [`true`](https://developer.apple.com/documentation/swift/true). Modifying the layer is significantly faster than redrawing the layer contents using [`draw(_:)`](nsview/draw(_:).md). If you override this property to be [`true`](https://developer.apple.com/documentation/swift/true), you must also override the [`updateLayer()`](nsview/updatelayer().md) method of your view and use it to make the changes to your layer. Do not modify your layer in your implementation of this property. Your implementation should return [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false) quickly and not perform other tasks.

If the [`canDrawSubviewsIntoLayer`](nsview/candrawsubviewsintolayer.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true), the view ignores the value returned by this method. Instead, the view always uses its [`draw(_:)`](nsview/draw(_:).md) method to draw its content.

> **Note**:  When using the [`updateLayer()`](nsview/updatelayer().md) method to update your view, it is recommended that you set the view’s redraw policy to [`NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay`](nsview/layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md). This policy lets you control when you want to update the layer’s contents.

 When using the [`updateLayer()`](nsview/updatelayer().md) method to update your view, it is recommended that you set the view’s redraw policy to [`NSView.LayerContentsRedrawPolicy.onSetNeedsDisplay`](nsview/layercontentsredrawpolicy-swift.enum/onsetneedsdisplay.md). This policy lets you control when you want to update the layer’s contents.

## See Also

- [func updateLayer()](nsview/updatelayer.md)
  Updates the view’s content by modifying its underlying layer.
- [var wantsLayer: Bool](nsview/wantslayer.md)
  A Boolean value indicating whether the view uses a layer as its backing store.
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
- [NSView.LayerContentsRedrawPolicy](nsview/layercontentsredrawpolicy-swift.enum.md)
  Constants that specify how layer resizing is handled when a view is layer-backed or layer-hosting. For more information, see the  [`layerContentsRedrawPolicy`](nsview/layercontentsredrawpolicy-swift.property.md) property.
- [var canDrawSubviewsIntoLayer: Bool](nsview/candrawsubviewsintolayer.md)
  A Boolean value indicating whether the view incorporates content from its subviews into its own layer.
- [var layerUsesCoreImageFilters: Bool](nsview/layerusescoreimagefilters.md)
  A Boolean value indicating whether the view’s layer uses Core Image filters and needs in-process rendering.
- [protocol NSViewLayerContentScaleDelegate](nsviewlayercontentscaledelegate.md)
  An optional layer delegate method for handling resolution changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/wantsupdatelayer)*