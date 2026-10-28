# current

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the current OpenGL graphics context.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
class var current: NSOpenGLContext? { get }
```

```objc
@property (class, strong, readonly, nullable) NSOpenGLContext * currentContext;
```

## Return Value

The current OpenGL graphics context, or `nil` if no such object has been set.

## See Also

### Managing the Current Context
- [class func clearCurrentContext()](./clearcurrentcontext%28%29.md)
  Clears the current context.
- [func makeCurrentContext()](./makecurrentcontext%28%29.md)
  Sets the context as the current OpenGL context object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/current)*