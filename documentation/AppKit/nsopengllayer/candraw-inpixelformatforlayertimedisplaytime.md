# canDraw(in:pixelFormat:forLayerTime:displayTime:)

**Framework**: AppKit  
**Kind**: method

Invoked to ask the layer whether it can (or should) draw.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func canDraw(in context: NSOpenGLContext, pixelFormat: NSOpenGLPixelFormat, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver should render OpenGL content, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

This method is called before attempting to render the frame for the layer time specified by `timeInterval`. If the method returns [`false`](https://developer.apple.com/documentation/swift/false), the frame is skipped. The default implementation always returns [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `context`: The NSOpenGLContext in to which the OpenGL content would be drawn.
- `pixelFormat`: The pixel format used when the context was created.
- `t`: The current layer time.
- `ts`: The display timestamp associated with timeInterval. Can be  .

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
- [func draw(in: NSOpenGLContext, pixelFormat: NSOpenGLPixelFormat, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>)](nsopengllayer/draw(in:pixelformat:forlayertime:displaytime:).md)
  Draws the OpenGL content for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/candraw(in:pixelformat:forlayertime:displaytime:))*