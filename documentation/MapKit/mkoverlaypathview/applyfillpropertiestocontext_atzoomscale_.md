# applyFillPropertiesToContext:atZoomScale:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Applies the receiver’s current fill-related drawing properties to the specified graphics context

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayPathRenderer`](../mkoverlaypathrenderer.md) object instead.

## Declaration

```objc
- (void) applyFillPropertiesToContext:(CGContextRef) context atZoomScale:(MKZoomScale) zoomScale;
```

#### Discussion

This is a convenience method for applying all of the drawing properties used when filling a path. This method applies the current fill color to the specified graphics context.

## Parameters

- `context`: The graphics context used to draw the view’s contents.
- `zoomScale`: The current zoom scale used for drawing.

## See Also

### Drawing the Path
- [- applyStrokePropertiesToContext:atZoomScale:](./applystrokepropertiestocontext_atzoomscale_.md)
  Applies the receiver’s current stroke-related drawing properties to the specified graphics context.
- [- strokePath:inContext:](./strokepath_incontext_.md)
  Draws a line along the specified path.
- [- fillPath:inContext:](./fillpath_incontext_.md)
  Fills the area enclosed by the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/applyfillpropertiestocontext:atzoomscale:)*