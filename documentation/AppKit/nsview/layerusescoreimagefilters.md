# layerUsesCoreImageFilters

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view’s layer uses Core Image filters and needs in-process rendering.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var layerUsesCoreImageFilters: Bool { get set }
```

#### Discussion

If your view uses a custom layer and you assigned Core Image to that layer directly, you must set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to let AppKit know of that fact. In macOS 10.9 and later, AppKit prefers to render layer trees out-of-process but cannot do so if any layers have Core Image filters attached to them. Specifying [`true`](https://developer.apple.com/documentation/Swift/true) for property lets AppKit know that it must move rendering of the layer hierarchy back into your app’s process. If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), adding a filter to the view’s layer triggers an exception.

You do not need to modify this property if you assigned the filters using the [`backgroundFilters`](nsview/backgroundfilters.md), [`compositingFilter`](nsview/compositingfilter.md), or [`contentFilters`](nsview/contentfilters.md) properties of the view. Those methods automatically let AppKit know that it needs to render the layer hierarchy in-process. Set it only if you set the filters on the layer directly.

## See Also

- [func removeConstraint(NSLayoutConstraint)](nsview/removeconstraint(_:).md)
  Removes the specified constraint from the view.
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
- [NSView.LayerContentsRedrawPolicy](nsview/layercontentsredrawpolicy-swift.enum.md)
  Constants that specify how layer resizing is handled when a view is layer-backed or layer-hosting. For more information, see the  [`layerContentsRedrawPolicy`](nsview/layercontentsredrawpolicy-swift.property.md) property.
- [var canDrawSubviewsIntoLayer: Bool](nsview/candrawsubviewsintolayer.md)
  A Boolean value indicating whether the view incorporates content from its subviews into its own layer.
- [protocol NSViewLayerContentScaleDelegate](nsviewlayercontentscaledelegate.md)
  An optional layer delegate method for handling resolution changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layerusescoreimagefilters)*