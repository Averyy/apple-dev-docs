# draw(in:pixelFormat:forLayerTime:displayTime:)

**Framework**: AppKit  
**Kind**: method

Draws the OpenGL content for the specified time.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func draw(in context: NSOpenGLContext, pixelFormat: NSOpenGLPixelFormat, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>)
```

#### Discussion

This method is called when a new frame needs to be generated for the layer time specified by timeInterval.

## Parameters

- `context`: The NSOpenGLContext in to which the OpenGL content would be drawn.
- `pixelFormat`: The pixel format used when the context was created.
- `t`: The current layer time.
- `ts`: The display timestamp associated with timeInterval. Can be  .

## See Also

- [func canDraw(in: NSOpenGLContext, pixelFormat: NSOpenGLPixelFormat, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>) -> Bool](nsopengllayer/candraw(in:pixelformat:forlayertime:displaytime:).md)
  Invoked to ask the layer whether it can (or should) draw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/draw(in:pixelformat:forlayertime:displaytime:))*