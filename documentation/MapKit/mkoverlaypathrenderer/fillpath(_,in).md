# fillPath(_:in:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Fills the area that the specified path encloses.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func fillPath(_ path: CGPath, in context: CGContext)
```

```objc
- (void) fillPath:(CGPathRef) path inContext:(CGContextRef) context;
```

## Discussion

You must set the current fill color before calling this method. Typically you do this by calling the [`applyFillProperties(to:atZoomScale:)`](./applyfillproperties%28to,atzoomscale%29.md) method prior to drawing. If the [`fillColor`](./fillcolor.md) property is currently `nil`, this method does nothing.

## Parameters

- `path`: The path to fill.
- `context`: The graphics context in which to draw the path.

## See Also

### Drawing the path
- [func applyStrokeProperties(to: CGContext, atZoomScale: MKZoomScale)](./applystrokeproperties%28to,atzoomscale%29.md)
  Applies the renderer’s stroke-related drawing properties to the specified graphics context.
- [func applyFillProperties(to: CGContext, atZoomScale: MKZoomScale)](./applyfillproperties%28to,atzoomscale%29.md)
  Applies the receiver’s fill-related drawing properties to the specified graphics context.
- [func strokePath(CGPath, in: CGContext)](./strokepath%28_,in%29.md)
  Draws a line along the specified path.
- [var shouldRasterize: Bool](./shouldrasterize.md)
  A Boolean value that determines whether the overlay path renderer renders the overlay as a bitmap before compositing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/fillpath(_:in:))*