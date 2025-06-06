# setValues(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the value of the specified parameter.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setValues(_ vals: UnsafePointer<GLint>, for param: NSOpenGLContext.Parameter)
```

## Parameters

- `vals`: The new value (or values) for the parameter.
- `param`: The parameter you want to modify. For a list of parameters, see  .

## See Also

- [func getValues(UnsafeMutablePointer<GLint>, for: NSOpenGLContext.Parameter)](nsopenglcontext/getvalues(_:for:).md)
  Returns the value of the requested parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/setvalues(_:for:))*