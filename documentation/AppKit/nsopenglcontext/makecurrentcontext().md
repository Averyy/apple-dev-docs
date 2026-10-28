# makeCurrentContext()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the context as the current OpenGL context object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
func makeCurrentContext()
```

```objc
- (void) makeCurrentContext;
```

## Discussion

Subsequent OpenGL calls are rendered into the context defined by the receiver.

> **Note**:  A context is current on a per-thread basis. Multiple threads must serialize calls into the same context object.

## See Also

### Managing the Current Context
- [class func clearCurrentContext()](./clearcurrentcontext%28%29.md)
  Clears the current context.
- [class var current: NSOpenGLContext?](./current.md)
  Returns the current OpenGL graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/makecurrentcontext())*