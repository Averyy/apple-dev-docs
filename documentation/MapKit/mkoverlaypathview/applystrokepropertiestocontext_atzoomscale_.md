# applyStrokePropertiesToContext:atZoomScale:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Applies the receiver’s current stroke-related drawing properties to the specified graphics context.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayPathRenderer`](../mkoverlaypathrenderer.md) object instead.

## Declaration

```objc
- (void) applyStrokePropertiesToContext:(CGContextRef) context atZoomScale:(MKZoomScale) zoomScale;
```

#### Discussion

This is a convenience method for applying all of the drawing properties used when stroking a path. This method applies the stroke color, line width, line join, line cap, miter limit, line dash phase, and line dash attributes to the specified graphics context. This method applies the scale factor in the `zoomScale` parameter to the line width and line dash pattern automatically so that lines scale appropriately.

This method does not save the current graphics state before applying the new attributes. You must save it yourself and restore it later when you are done drawing.

## Parameters

- `context`: The graphics context used to draw the view’s contents.
- `zoomScale`: The current zoom scale used for drawing.

## See Also

### Drawing the Path
- [- applyFillPropertiesToContext:atZoomScale:](./applyfillpropertiestocontext_atzoomscale_.md)
  Applies the receiver’s current fill-related drawing properties to the specified graphics context
- [- strokePath:inContext:](./strokepath_incontext_.md)
  Draws a line along the specified path.
- [- fillPath:inContext:](./fillpath_incontext_.md)
  Fills the area enclosed by the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/applystrokepropertiestocontext:atzoomscale:)*