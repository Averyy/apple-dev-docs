# NSViewLayerContentScaleDelegate

**Framework**: AppKit  
**Kind**: protocol

An optional layer delegate method for handling resolution changes.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSViewLayerContentScaleDelegate : NSObjectProtocol
```

#### Overview

Use this protocol to manage scale and contents for a layer hosted in a view. When a window changes its backing resolution, AppKit attempts to automatically update the `contentsScale` and `contents` of all `CALayer` objects in the window to match the new resolution. Layers backed by a view are updated automatically. Any layer whose `contents` property is set to an `NSImage` object is also updated automatically. Based on the `NSImage` object’s available representations, AppKit selects an appropriate bitmapped representation, or rasterizes a resolution-independent representation at the appropriate scale factor.

For all other layers, AppKit checks whether the layer has a delegate that implements this protocol.  If so, AppKit asks the layer’s delegate whether it should automatically update the `contentsScale` for that layer to match the new scale factor of the window.

## Topics

### Responding to Resolution Changes
- [func layer(CALayer, shouldInheritContentsScale: CGFloat, from: NSWindow) -> Bool](nsviewlayercontentscaledelegate/layer(_:shouldinheritcontentsscale:from:).md)
  Notifies you when a resolution changes occurs for the window that hosts the layer.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [View Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002978)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewlayercontentscaledelegate)*