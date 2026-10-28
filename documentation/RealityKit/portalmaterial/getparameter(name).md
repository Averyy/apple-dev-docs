# getParameter(name:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the value of a parameter by name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func getParameter(name: String) -> MaterialParameters.Value?
```

## Return Value

The current value of the parameter, or `nil` if the parameter has no value set on this material.

## Parameters

- `name`: The name of the parameter as declared in the shader graph.

## See Also

### Accessing shader parameters
- [func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?](./getparameter%28handle%29.md)
  Returns the value of a parameter identified by a handle.
- [func setParameter(name: String, value: MaterialParameters.Value) throws](./setparameter%28name,value%29.md)
  Sets the value of a parameter by name.
- [func setParameter(handle: MaterialParameters.Handle, value: MaterialParameters.Value) throws](./setparameter%28handle,value%29.md)
  Sets the value of a parameter identified by a handle.
- [static func parameterHandle(name: String) -> MaterialParameters.Handle](./parameterhandle%28name%29.md)
  Returns a handle for the parameter with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/getparameter(name:))*