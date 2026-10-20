# textViewportLayoutController(_:cacheRenderingSurface:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) textViewportLayoutController:(NSTextViewportLayoutController *) textViewportLayoutController cacheRenderingSurface:(id<NSTextViewportRenderingSurface>) renderingSurface forKey:(id<NSTextViewportRenderingSurfaceKey>) renderingSurfaceKey;
```

## Parameters

- `textViewportLayoutController`: The viewport layout controller.
- `renderingSurface`: The rendering surface to cache.
- `renderingSurfaceKey`: The key identifying the rendering surface.

## See Also

### Storing rendering surfaces
- [func textViewportLayoutController(NSTextViewportLayoutController, retrieveCachedRenderingSurfaceFor: any NSTextViewportRenderingSurfaceKey) -> any NSTextViewportRenderingSurface](./textviewportlayoutcontroller%28_,retrievecachedrenderingsurfacefor%29.md)
  Asks the delegate to return a previously cached rendering surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:))*