# textViewportLayoutController(_:cacheRenderingSurface:for:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to cache a rendering surface for later retrieval.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, cacheRenderingSurface renderingSurface: any NSTextViewportRenderingSurface, for renderingSurfaceKey: any NSTextViewportRenderingSurfaceKey)
```

## Parameters

- `textViewportLayoutController`: The viewport layout controller.
- `renderingSurface`: The rendering surface to cache.
- `renderingSurfaceKey`: The key identifying the rendering surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:))*