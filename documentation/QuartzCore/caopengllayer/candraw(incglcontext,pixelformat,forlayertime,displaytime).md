# canDraw(inCGLContext:pixelFormat:forLayerTime:displayTime:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Returns whether the receiver should draw OpenGL content for the specified time.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func canDraw(inCGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>?) -> Bool
```

```objc
- (BOOL) canDrawInCGLContext:(CGLContextObj) ctx pixelFormat:(CGLPixelFormatObj) pf forLayerTime:(CFTimeInterval) t displayTime:(const CVTimeStamp *) ts;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver should render OpenGL content, [`false`](../../Swift/false.md) otherwise.

## Discussion

This method is called before attempting to render the frame for the layer time specified by `timeInterval`. If the method returns [`false`](../../Swift/false.md), the frame is skipped. The default implementation always returns [`true`](../../Swift/true.md).

## Parameters

- `ctx`: The `CGLContextObj` in to which the OpenGL content would be drawn.
- `pf`: The pixel format used when the `glContext` was created.
- `t`: The current layer time.
- `ts`: The display timestamp associated with `timeInterval`. Can be `null`.

## See Also

### Drawing Layer Content
- [var isAsynchronous: Bool](./isasynchronous.md)
  Determines when the contents of the layer are updated.
- [func draw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?)](./draw%28incglcontext,pixelformat,forlayertime,displaytime%29.md)
  Draws the OpenGL content for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/candraw(incglcontext:pixelformat:forlayertime:displaytime:))*