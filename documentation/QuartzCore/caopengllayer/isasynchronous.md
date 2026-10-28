# isAsynchronous

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Determines when the contents of the layer are updated.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: OpenGL is deprecated. (Define GL_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var isAsynchronous: Bool { get set }
```

```objc
@property (getter=isAsynchronous) BOOL asynchronous;
```

## Discussion

If [`false`](../../Swift/false.md), the contents of the layer are updated only in response to receiving a [`setNeedsDisplay()`](../calayer/setneedsdisplay%28%29.md) message. When [`true`](../../Swift/true.md), the receiver’s [`canDraw(inCGLContext:pixelFormat:forLayerTime:displayTime:)`](./candraw%28incglcontext,pixelformat,forlayertime,displaytime%29.md) is called periodically to determine if the OpenGL content should be updated.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Drawing Layer Content
- [func canDraw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?) -> Bool](./candraw%28incglcontext,pixelformat,forlayertime,displaytime%29.md)
  Returns whether the receiver should draw OpenGL content for the specified time.
- [func draw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?)](./draw%28incglcontext,pixelformat,forlayertime,displaytime%29.md)
  Draws the OpenGL content for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/isasynchronous)*