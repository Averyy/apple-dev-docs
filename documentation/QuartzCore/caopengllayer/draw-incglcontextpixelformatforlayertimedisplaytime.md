# draw(inCGLContext:pixelFormat:forLayerTime:displayTime:)

**Framework**: Core Animation  
**Kind**: method

Draws the OpenGL content for the specified time.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func draw(inCGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>?)
```

#### Discussion

This method is called when a new frame needs to be generated for the layer time specified by `timeInterval`. The viewport of `glContext` is set correctly for the size of the layer. No other state is defined. If the method enables OpenGL features, it should disable them before returning.

The default implementation of the method flushes the context.

## Parameters

- `ctx`: The rendering context in to which the OpenGL content should be rendered.
- `pf`: The pixel format used when the   was created.
- `t`: The current layer time.
- `ts`: The display timestamp associated with  . Can be  .

## See Also

- [var isAsynchronous: Bool](caopengllayer/isasynchronous.md)
  Determines when the contents of the layer are updated.
- [func canDraw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?) -> Bool](caopengllayer/candraw(incglcontext:pixelformat:forlayertime:displaytime:).md)
  Returns whether the receiver should draw OpenGL content for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/draw(incglcontext:pixelformat:forlayertime:displaytime:))*