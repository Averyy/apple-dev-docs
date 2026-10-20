# draw(inCGLContext:pixelFormat:forLayerTime:displayTime:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Draws the OpenGL content for the specified time.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func draw(inCGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>?)
```

```objc
- (void) drawInCGLContext:(CGLContextObj) ctx pixelFormat:(CGLPixelFormatObj) pf forLayerTime:(CFTimeInterval) t displayTime:(const CVTimeStamp *) ts;
```

#### Discussion

This method is called when a new frame needs to be generated for the layer time specified by `timeInterval`. The viewport of `glContext` is set correctly for the size of the layer. No other state is defined. If the method enables OpenGL features, it should disable them before returning.

The default implementation of the method flushes the context.

## Parameters

- `ctx`: The rendering context in to which the OpenGL content should be rendered.
- `pf`: The pixel format used when the `glContext` was created.
- `t`: The current layer time.
- `ts`: The display timestamp associated with `timeInterval`. Can be `null`.

## See Also

### Drawing Layer Content
- [var isAsynchronous: Bool](./isasynchronous.md)
  Determines when the contents of the layer are updated.
- [func canDraw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?) -> Bool](./candraw%28incglcontext,pixelformat,forlayertime,displaytime%29.md)
  Returns whether the receiver should draw OpenGL content for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/draw(incglcontext:pixelformat:forlayertime:displaytime:))*