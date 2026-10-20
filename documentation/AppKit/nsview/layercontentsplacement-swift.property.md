# layerContentsPlacement

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current layer contents placement policy.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var layerContentsPlacement: NSView.LayerContentsPlacement { get set }
```

```objc
@property NSViewLayerContentsPlacement layerContentsPlacement;
```

#### Discussion

The content placement determines how the backing layer’s existing cached content image will be mapped into the layer as the layer is resized. It is analogous to, and underpinned by, the [`contentsGravity`](../../QuartzCore/calayer/contentsgravity.md) property of the [`CALayer`](../../QuartzCore/calayer.md) class. The default value of this property is [`NSView.LayerContentsPlacement.scaleAxesIndependently`](./layercontentsplacement-swift.enum/scaleaxesindependently.md). For a list of supported values, see [`NSView.LayerContentsPlacement`](./layercontentsplacement-swift.enum.md).

For additional information about the performance impacts of this property, see the [`layerContentsRedrawPolicy`](./layercontentsredrawpolicy-swift.property.md) property.

## See Also

### Managing the View’s Layer
- [var wantsLayer: Bool](./wantslayer.md)
  A Boolean value indicating whether the view uses a layer as its backing store.
- [var wantsUpdateLayer: Bool](./wantsupdatelayer.md)
  A Boolean value indicating which drawing path the view takes when updating its contents.
- [var layer: CALayer?](./layer.md)
  The Core Animation layer that the view uses as its backing store.
- [func makeBackingLayer() -> CALayer](./makebackinglayer%28%29.md)
  Creates the view’s backing layer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layercontentsplacement-swift.property)*