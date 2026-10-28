# renderingSurfaceForKey:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a rendering surface corresponding to the specified key.

## Declaration

```objc
- (id<NSTextViewportRenderingSurface>) renderingSurfaceForKey:(id<NSTextViewportRenderingSurfaceKey>) key;
```

## Return Value

The rendering surface, or `nil`.

## Discussion

The mapping is registered via the returned rendering surfaces from `textViewportLayoutController:renderingSurfaceForTextLayoutFragment:`. In addition, it can return auxiliary rendering surfaces registered through `addRenderingSurface:key:group:placement:`. The mappings are cleared at the beginning of each [`layoutViewport()`](./layoutviewport%28%29.md).

## Parameters

- `key`: The key identifying the rendering surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/renderingsurfaceforkey:)*