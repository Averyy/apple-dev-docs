# canDraw(in:pixelFormat:forLayerTime:displayTime:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to ask the layer whether it can (or should) draw.

**Availability**:
- macOS 10.6+ - Deprecated in 10.14

> **Deprecated**: Please use CAMetalLayer instead.

## Declaration

```swift
func canDraw(in context: NSOpenGLContext, pixelFormat: NSOpenGLPixelFormat, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>) -> Bool
```

```objc
- (BOOL) canDrawInOpenGLContext:(NSOpenGLContext *) context pixelFormat:(NSOpenGLPixelFormat *) pixelFormat forLayerTime:(CFTimeInterval) t displayTime:(const CVTimeStamp *) ts;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver should render OpenGL content, [`false`](../../Swift/false.md) otherwise.

#### Discussion

This method is called before attempting to render the frame for the layer time specified by `timeInterval`. If the method returns [`false`](../../Swift/false.md), the frame is skipped. The default implementation always returns [`true`](../../Swift/true.md).

## Parameters

- `context`: The NSOpenGLContext in to which the OpenGL content would be drawn.
- `pixelFormat`: The pixel format used when the context was created.
- `t`: The current layer time.
- `ts`: The display timestamp associated with timeInterval. Can be `null`.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Drawing the Content
- [func draw(in: NSOpenGLContext, pixelFormat: NSOpenGLPixelFormat, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>)](./draw%28in,pixelformat,forlayertime,displaytime%29.md)
  Draws the OpenGL content for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopengllayer/candraw(in:pixelformat:forlayertime:displaytime:))*