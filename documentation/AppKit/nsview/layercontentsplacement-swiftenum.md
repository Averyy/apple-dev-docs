# NSView.LayerContentsPlacement

**Framework**: AppKit  
**Kind**: enum

These constants specify the location of the layer content when the content is not rerendered in response to view resizing. For more information, see the [`layerContentsPlacement`](nsview/layercontentsplacement-swift.property.md) property.

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum LayerContentsPlacement
```

## Topics

### Constants
- [NSView.LayerContentsPlacement.scaleAxesIndependently](nsview/layercontentsplacement-swift.enum/scaleaxesindependently.md)
  The content is resized to fit the entire bounds rectangle.
- [NSView.LayerContentsPlacement.scaleProportionallyToFit](nsview/layercontentsplacement-swift.enum/scaleproportionallytofit.md)
  The content is resized to fit the bounds rectangle, preserving the aspect of the content. If the content does not completely fill the bounds rectangle, the content is centered in the partial axis.
- [NSView.LayerContentsPlacement.scaleProportionallyToFill](nsview/layercontentsplacement-swift.enum/scaleproportionallytofill.md)
  The content is resized to completely fill the bounds rectangle, while still preserving the aspect of the content. The content is centered in the axis it exceeds.
- [NSView.LayerContentsPlacement.center](nsview/layercontentsplacement-swift.enum/center.md)
  The content is horizontally and vertically centered in the bounds rectangle.
- [NSView.LayerContentsPlacement.top](nsview/layercontentsplacement-swift.enum/top.md)
  The content is horizontally centered at the top-edge of the bounds rectangle.
- [NSView.LayerContentsPlacement.topRight](nsview/layercontentsplacement-swift.enum/topright.md)
  The content is positioned in the top-right corner of the bounds rectangle.
- [NSView.LayerContentsPlacement.right](nsview/layercontentsplacement-swift.enum/right.md)
  The content is vertically centered at the right-edge of the bounds rectangle.
- [NSView.LayerContentsPlacement.bottomRight](nsview/layercontentsplacement-swift.enum/bottomright.md)
  The content is positioned in the bottom-right corner of the bounds rectangle.
- [NSView.LayerContentsPlacement.bottom](nsview/layercontentsplacement-swift.enum/bottom.md)
  The content is horizontally centered at the bottom-edge of the bounds rectangle.
- [NSView.LayerContentsPlacement.bottomLeft](nsview/layercontentsplacement-swift.enum/bottomleft.md)
  The content is positioned in the bottom-left corner of the bounds rectangle.
- [NSView.LayerContentsPlacement.left](nsview/layercontentsplacement-swift.enum/left.md)
  The content is vertically centered at the left-edge of the bounds rectangle.
- [NSView.LayerContentsPlacement.topLeft](nsview/layercontentsplacement-swift.enum/topleft.md)
  The content is positioned in the top-left corner of the bounds rectangle.
### Initializers
- [init?(rawValue: Int)](nsview/layercontentsplacement-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/layercontentsplacement-swift.enum)*