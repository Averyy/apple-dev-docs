# clearCurrentContext()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Clears the current context.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
class func clearCurrentContext()
```

```objc
+ (void) clearCurrentContext;
```

## Discussion

Until you issue a subsequent call to the [`makeCurrentContext()`](./makecurrentcontext%28%29.md) method, OpenGL calls do nothing.

## See Also

### Managing the Current Context
- [class var current: NSOpenGLContext?](./current.md)
  Returns the current OpenGL graphics context.
- [func makeCurrentContext()](./makecurrentcontext%28%29.md)
  Sets the context as the current OpenGL context object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/clearcurrentcontext())*