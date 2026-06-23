# textViewportLayoutController(_:retrieveCachedRenderingSurfaceFor:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to return a previously cached rendering surface.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, retrieveCachedRenderingSurfaceFor renderingSurfaceKey: any NSTextViewportRenderingSurfaceKey) -> any NSTextViewportRenderingSurface
```

#### Return Value

The cached rendering surface, or `nil`.

## Parameters

- `textViewportLayoutController`: The viewport layout controller.
- `renderingSurfaceKey`: The key identifying the rendering surface.

## See Also

- [func textViewportLayoutController(NSTextViewportLayoutController, cacheRenderingSurface: any NSTextViewportRenderingSurface, for: any NSTextViewportRenderingSurfaceKey)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:).md)
  Asks the delegate to cache a rendering surface for later retrieval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:retrievecachedrenderingsurfacefor:))*