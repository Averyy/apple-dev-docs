# fillPath:inContext:

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Fills the area enclosed by the specified path.

**Availability**:
- iOS 4.0+ - Deprecated in 7.0
- iPadOS 4.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use an [`MKOverlayPathRenderer`](../mkoverlaypathrenderer.md) object instead.

## Declaration

```objc
- (void) fillPath:(CGPathRef) path inContext:(CGContextRef) context;
```

#### Discussion

You must set the current fill color before calling this method. Typically you do this by calling the [`applyFillPropertiesToContext:atZoomScale:`](./applyfillpropertiestocontext_atzoomscale_.md) method prior to drawing. If the [`fillColor`](./fillcolor.md) property is currently `nil`, this method does nothing.

## Parameters

- `path`: The path to fill.
- `context`: The graphics context in which to draw the path.

## See Also

### Drawing the Path
- [- applyStrokePropertiesToContext:atZoomScale:](./applystrokepropertiestocontext_atzoomscale_.md)
  Applies the receiver’s current stroke-related drawing properties to the specified graphics context.
- [- applyFillPropertiesToContext:atZoomScale:](./applyfillpropertiestocontext_atzoomscale_.md)
  Applies the receiver’s current fill-related drawing properties to the specified graphics context
- [- strokePath:inContext:](./strokepath_incontext_.md)
  Draws a line along the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview/fillpath:incontext:)*