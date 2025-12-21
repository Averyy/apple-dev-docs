# canDraw(inCGLContext:pixelFormat:forLayerTime:displayTime:)

**Framework**: Core Animation  
**Kind**: method

Returns whether the receiver should draw OpenGL content for the specified time.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func canDraw(inCGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver should render OpenGL content, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

This method is called before attempting to render the frame for the layer time specified by `timeInterval`. If the method returns [`false`](https://developer.apple.com/documentation/Swift/false), the frame is skipped. The default implementation always returns [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `ctx`: The   in to which the OpenGL content would be drawn.
- `pf`: The pixel format used when the   was created.
- `t`: The current layer time.
- `ts`: The display timestamp associated with  . Can be  .

## See Also

- [var isAsynchronous: Bool](caopengllayer/isasynchronous.md)
  Determines when the contents of the layer are updated.
- [func draw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?)](caopengllayer/draw(incglcontext:pixelformat:forlayertime:displaytime:).md)
  Draws the OpenGL content for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/candraw(incglcontext:pixelformat:forlayertime:displaytime:))*