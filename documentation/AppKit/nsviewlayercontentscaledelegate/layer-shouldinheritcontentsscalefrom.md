# layer(_:shouldInheritContentsScale:from:)

**Framework**: AppKit  
**Kind**: method

Notifies you when a resolution changes occurs for the window that hosts the layer.

**Availability**:
- macOS 10.7+

## Declaration

```swift
nonisolated
optional func layer(_ layer: CALayer, shouldInheritContentsScale newScale: CGFloat, from window: NSWindow) -> Bool
```

#### Return Value

A Boolean value that specifies whether to change the layer’s `contentsScale` property.

#### Discussion

When a resolution change occurs for a given window, the system traverses the layer trees in that window to decide what action, if any, to take for each layer. The system queries the layer’s delegate to determine whether to change the layer’s `contentsScale` property to the new scale (either `2.0` or `1.0`).

Note that you don’t need to manage [`NSImage`](nsimage.md) contents and that this method is not called on the delegate of a layer whose content is an [`NSImage`](nsimage.md) object.

If the delegate returns [`true`](https://developer.apple.com/documentation/Swift/true), it should make any corresponding changes to the layer’s properties, as required by the resolution change. For example, a layer whose contents contain a CGImage object needs to determine whether an alternate CGImage object is available for the new scale factor. If the delegate finds a suitable CGImage object, then in addition to returning [`true`](https://developer.apple.com/documentation/Swift/true), it should set the appropriate CGImage object as the layer’s new contents.

## Parameters

- `layer`: The layer whose scale and content might need updating.
- `newScale`: The new scale of the window.
- `window`: The window that hosts the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewlayercontentscaledelegate/layer(_:shouldinheritcontentsscale:from:))*