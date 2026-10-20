# textViewportLayoutController(_:cacheRenderingSurface:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to cache a rendering surface for later retrieval.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, cacheRenderingSurface renderingSurface: any NSTextViewportRenderingSurface, for renderingSurfaceKey: any NSTextViewportRenderingSurfaceKey)
```

```objc
- (void) textViewportLayoutController:(NSTextViewportLayoutController *) textViewportLayoutController cacheRenderingSurface:(id<NSTextViewportRenderingSurface>) renderingSurface forKey:(id<NSTextViewportRenderingSurfaceKey>) renderingSurfaceKey;
```

## Parameters

- `textViewportLayoutController`: The viewport layout controller.
- `renderingSurface`: The rendering surface to cache.
- `renderingSurfaceKey`: The key identifying the rendering surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:))*