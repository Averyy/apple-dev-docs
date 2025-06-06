# Core Animation Support

**Framework**: AppKit

Manage the layer object that provides the view’s visual representation and accelerates drawing operations.

## Topics

### Managing the View’s Layer
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
- [var layerUsesCoreImageFilters: Bool](nsview/layerusescoreimagefilters.md)
  A Boolean value indicating whether the view’s layer uses Core Image filters and needs in-process rendering.
- [protocol NSViewLayerContentScaleDelegate](nsviewlayercontentscaledelegate.md)
  An optional layer delegate method for handling resolution changes.
### Managing Layer-Related Properties
- [var alphaValue: CGFloat](nsview/alphavalue.md)
  The opacity of the view.
- [var frameCenterRotation: CGFloat](nsview/framecenterrotation.md)
  The rotation angle of the view around the center of its layer.
- [var backgroundFilters: [CIFilter]](nsview/backgroundfilters.md)
  An array of Core Image filters to apply to the view’s background.
- [var compositingFilter: CIFilter?](nsview/compositingfilter.md)
  The Core Image filter used to composite the view’s contents with its background.
- [var contentFilters: [CIFilter]](nsview/contentfilters.md)
  An array of Core Image filters to apply to the contents of the view and its sublayers.
- [var shadow: NSShadow?](nsview/shadow.md)
  The shadow displayed underneath the view.

## See Also

- [View Hierarchy](view-hierarchy.md)
  Manage the subviews, superview, and window of a view and respond to notifications when the view hierarchy changes.
- [View Coordinates](view-coordinates.md)
  Manage the frame and bounds rectangles that determine the size and position of the view in the view hierarchy.
- [Appearance](nsview-appearance.md)
  Change the view’s visibility, vibrancy, and focus ring and respond to appearance-related changes.
- [Related UI](related-ui.md)
  Manage contextual menus, cursors, tool tips, and other system-provided windows and content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/core-animation-support)*