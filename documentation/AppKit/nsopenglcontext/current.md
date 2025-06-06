# current

**Framework**: AppKit  
**Kind**: property

Returns the current OpenGL graphics context.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class var current: NSOpenGLContext? { get }
```

#### Return Value

The current OpenGL graphics context, or `nil` if no such object has been set.

## See Also

- [class func clearCurrentContext()](nsopenglcontext/clearcurrentcontext.md)
  Clears the current context.
- [func makeCurrentContext()](nsopenglcontext/makecurrentcontext.md)
  Sets the context as the current OpenGL context object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/current)*