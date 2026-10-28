# textViewportLayoutController(_:retrieveCachedRenderingSurfaceFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id<NSTextViewportRenderingSurface>) textViewportLayoutController:(NSTextViewportLayoutController *) textViewportLayoutController retrieveCachedRenderingSurfaceForKey:(id<NSTextViewportRenderingSurfaceKey>) renderingSurfaceKey;
```

## Return Value

The cached rendering surface, or `nil`.

## Parameters

- `textViewportLayoutController`: The viewport layout controller.
- `renderingSurfaceKey`: The key identifying the rendering surface.

## See Also

### Storing rendering surfaces
- [func textViewportLayoutController(NSTextViewportLayoutController, cacheRenderingSurface: any NSTextViewportRenderingSurface, for: any NSTextViewportRenderingSurfaceKey)](./textviewportlayoutcontroller%28_,cacherenderingsurface,for%29.md)
  Asks the delegate to cache a rendering surface for later retrieval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:retrievecachedrenderingsurfacefor:))*