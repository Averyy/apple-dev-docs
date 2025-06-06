# getValues(_:for:)

**Framework**: AppKit  
**Kind**: method

Returns the value of the requested parameter.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func getValues(_ vals: UnsafeMutablePointer<GLint>, for param: NSOpenGLContext.Parameter)
```

## Parameters

- `vals`: On input, a pointer to a variable with enough space for one or more   integers. On output, the variable contains the value (or values) for the given parameter.
- `param`: The parameter you want to get. For a list of parameters, see the table in  .

## See Also

- [func setValues(UnsafePointer<GLint>, for: NSOpenGLContext.Parameter)](nsopenglcontext/setvalues(_:for:).md)
  Sets the value of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/getvalues(_:for:))*