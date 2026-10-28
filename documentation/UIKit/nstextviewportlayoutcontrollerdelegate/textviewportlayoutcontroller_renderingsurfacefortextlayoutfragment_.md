# textViewportLayoutController:renderingSurfaceForTextLayoutFragment:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a rendering surface for the specified text layout fragment.

## Declaration

```objc
- (id<NSTextViewportRenderingSurface>) textViewportLayoutController:(NSTextViewportLayoutController *) textViewportLayoutController renderingSurfaceForTextLayoutFragment:(NSTextLayoutFragment *) textLayoutFragment;
```

## Return Value

A rendering surface, or `nil`.

## Discussion

Invoked right before `textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:`. The returned rendering surface is registered and mapped by `renderingSurfaceForKey:`.

## Parameters

- `textViewportLayoutController`: The viewport layout controller.
- `textLayoutFragment`: The layout fragment needing a rendering surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller:renderingsurfacefortextlayoutfragment:)*