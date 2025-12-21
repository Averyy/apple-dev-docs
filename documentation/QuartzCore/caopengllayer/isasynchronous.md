# isAsynchronous

**Framework**: Core Animation  
**Kind**: property

Determines when the contents of the layer are updated.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
var isAsynchronous: Bool { get set }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/Swift/false), the contents of the layer are updated only in response to receiving a [`setNeedsDisplay()`](calayer/setneedsdisplay().md) message. When [`true`](https://developer.apple.com/documentation/Swift/true), the receiver’s [`canDraw(inCGLContext:pixelFormat:forLayerTime:displayTime:)`](caopengllayer/candraw(incglcontext:pixelformat:forlayertime:displaytime:).md) is called periodically to determine if the OpenGL content should be updated.

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
- [func canDraw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?) -> Bool](caopengllayer/candraw(incglcontext:pixelformat:forlayertime:displaytime:).md)
  Returns whether the receiver should draw OpenGL content for the specified time.
- [func draw(inCGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, forLayerTime: CFTimeInterval, displayTime: UnsafePointer<CVTimeStamp>?)](caopengllayer/draw(incglcontext:pixelformat:forlayertime:displaytime:).md)
  Draws the OpenGL content for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caopengllayer/isasynchronous)*