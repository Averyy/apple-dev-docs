# makeCurrentContext()

**Framework**: Appkit  
**Kind**: method

Sets the context as the current OpenGL context object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func makeCurrentContext()
```

#### Discussion

Subsequent OpenGL calls are rendered into the context defined by the receiver.

> **Note**:  A context is current on a per-thread basis. Multiple threads must serialize calls into the same context object.

## See Also

- [class func clearCurrentContext()](nsopenglcontext/clearcurrentcontext.md)
  Clears the current context.
- [class var current: NSOpenGLContext?](nsopenglcontext/current.md)
  Returns the current OpenGL graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/makecurrentcontext())*