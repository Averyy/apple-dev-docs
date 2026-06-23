# textViewportLayoutController(_:retrieveCachedRenderingSurfaceFor:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to return a previously cached rendering surface.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, retrieveCachedRenderingSurfaceFor renderingSurfaceKey: any NSTextViewportRenderingSurfaceKey) -> any NSTextViewportRenderingSurface
```

#### Return Value

The cached rendering surface, or `nil`.

## Parameters

- `textViewportLayoutController`: The viewport layout controller.
- `renderingSurfaceKey`: The key identifying the rendering surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:retrievecachedrenderingsurfacefor:))*