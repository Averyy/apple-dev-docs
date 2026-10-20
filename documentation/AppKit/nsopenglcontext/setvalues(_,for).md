# setValues(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the value of the specified parameter.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
func setValues(_ vals: UnsafePointer<GLint>, for param: NSOpenGLContext.Parameter)
```

```objc
- (void) setValues:(const GLint *) vals forParameter:(NSOpenGLContextParameter) param;
```

## Parameters

- `vals`: The new value (or values) for the parameter.
- `param`: The parameter you want to modify. For a list of parameters, see [`NSOpenGLContext.Parameter`](./parameter.md).

## See Also

### Context Parameter Handling
- [func getValues(UnsafeMutablePointer<GLint>, for: NSOpenGLContext.Parameter)](./getvalues%28_,for%29.md)
  Returns the value of the requested parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/setvalues(_:for:))*