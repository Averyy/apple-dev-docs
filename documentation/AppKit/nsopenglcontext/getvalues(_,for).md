# getValues(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value of the requested parameter.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use Metal or MetalKit.

## Declaration

```swift
func getValues(_ vals: UnsafeMutablePointer<GLint>, for param: NSOpenGLContext.Parameter)
```

```objc
- (void) getValues:(GLint *) vals forParameter:(NSOpenGLContextParameter) param;
```

## Parameters

- `vals`: On input, a pointer to a variable with enough space for one or more `long` integers. On output, the variable contains the value (or values) for the given parameter.
- `param`: The parameter you want to get. For a list of parameters, see the table in [`NSOpenGLContext.Parameter`](./parameter.md).

## See Also

### Context Parameter Handling
- [func setValues(UnsafePointer<GLint>, for: NSOpenGLContext.Parameter)](./setvalues%28_,for%29.md)
  Sets the value of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/getvalues(_:for:))*