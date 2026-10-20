# wantsLayer

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view uses a layer as its backing store.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var wantsLayer: Bool { get set }
```

```objc
@property BOOL wantsLayer;
```

#### Discussion

Setting the value of this property to [`true`](../../Swift/true.md) turns the view into a layer-backed view—that is, the view uses a [`CALayer`](../../QuartzCore/calayer.md) object to manage its rendered content. Creating a layer-backed view implicitly causes the entire view hierarchy under that view to become layer-backed. Thus, the view and all of its subviews (including subviews of subviews) become layer-backed. The default value of this property is [`false`](../../Swift/false.md).

In a layer-backed view, any drawing done by the view is cached to the underlying layer object. This cached content can then be manipulated in ways that are more performant than redrawing the view contents explicitly. AppKit automatically creates the underlying layer object (using the [`makeBackingLayer()`](./makebackinglayer%28%29.md) method) and handles the caching of the view’s content. If the [`wantsUpdateLayer`](./wantsupdatelayer.md) method returns [`false`](../../Swift/false.md), you should not interact with the underlying layer object directly. Instead, use the methods of this class to make any changes to the view and its layer. If [`wantsUpdateLayer`](./wantsupdatelayer.md) returns [`true`](../../Swift/true.md), it is acceptable (and appropriate) to modify the layer in the view’s [`updateLayer()`](./updatelayer%28%29.md) method.

For layer-backed views, you can flatten the layer hierarchy by setting the [`canDrawSubviewsIntoLayer`](./candrawsubviewsintolayer.md) property to [`true`](../../Swift/true.md). To prevent a subview from having its contents flattened into this view’s layer, explicitly set the value of the subview’s [`wantsLayer`](./wantslayer.md) property to [`true`](../../Swift/true.md).

In addition to creating a layer-backed view, you can create a layer-hosting view by assigning a layer directly to the view’s [`layer`](./layer.md) property. In a layer-hosting view, you are responsible for managing the view’s layer. To create a layer-hosting view, you must set the [`layer`](./layer.md) property first and then set this property to [`true`](../../Swift/true.md). The order in which you set the values of these properties is crucial.

In a layer-hosting view, do not rely on the view for drawing. Similarly, do not add subviews to a layer-hosting view. The root layer—that is, the layer you set using the [`layer`](./layer.md) property—becomes the root layer of the layer tree. Any manipulations of that layer tree must be done using the Core Animation interfaces. You still use the view for handling mouse and keyboard events, but drawing must be handled by Core Animation.

## See Also

### Managing the View’s Layer
- [var wantsUpdateLayer: Bool](./wantsupdatelayer.md)
  A Boolean value indicating which drawing path the view takes when updating its contents.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/wantslayer)*