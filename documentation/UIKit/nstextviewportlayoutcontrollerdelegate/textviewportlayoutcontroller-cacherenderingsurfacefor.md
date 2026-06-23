# textViewportLayoutController(_:cacheRenderingSurface:for:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to cache a rendering surface for later retrieval.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, cacheRenderingSurface renderingSurface: any NSTextViewportRenderingSurface, for renderingSurfaceKey: any NSTextViewportRenderingSurfaceKey)
```

## Parameters

- `textViewportLayoutController`: The viewport layout controller.
- `renderingSurface`: The rendering surface to cache.
- `renderingSurfaceKey`: The key identifying the rendering surface.

## See Also

- [func textViewportLayoutController(NSTextViewportLayoutController, retrieveCachedRenderingSurfaceFor: any NSTextViewportRenderingSurfaceKey) -> any NSTextViewportRenderingSurface](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:retrievecachedrenderingsurfacefor:).md)
  Asks the delegate to return a previously cached rendering surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:))*