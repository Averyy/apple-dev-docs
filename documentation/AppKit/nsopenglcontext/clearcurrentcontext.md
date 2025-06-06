# clearCurrentContext()

**Framework**: AppKit  
**Kind**: method

Clears the current context.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func clearCurrentContext()
```

#### Discussion

Until you issue a subsequent call to the [`makeCurrentContext()`](nsopenglcontext/makecurrentcontext().md) method, OpenGL calls do nothing.

## See Also

- [class var current: NSOpenGLContext?](nsopenglcontext/current.md)
  Returns the current OpenGL graphics context.
- [func makeCurrentContext()](nsopenglcontext/makecurrentcontext.md)
  Sets the context as the current OpenGL context object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/clearcurrentcontext())*