# setParameter(name:value:)

**Framework**: RealityKit  
**Kind**: method

Sets the value of a parameter by name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func setParameter(name: String, value newValue: MaterialParameters.Value) throws
```

#### Discussion

> **Note**: If the value type is incompatible with the parameter’s declared type.

## Parameters

- `name`: The name of the parameter as declared in the shader graph.

## See Also

- [func getParameter(name: String) -> MaterialParameters.Value?](portalmaterial/getparameter(name:).md)
  Returns the current value of a parameter by name, or `nil` if no value has been set.
- [func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?](portalmaterial/getparameter(handle:).md)
  Returns the current value of a parameter identified by its precomputed handle, or `nil` if no value has been set.
- [func setParameter(handle: MaterialParameters.Handle, value: MaterialParameters.Value) throws](portalmaterial/setparameter(handle:value:).md)
  Sets the value of a parameter identified by its precomputed handle.
- [static func parameterHandle(name: String) -> MaterialParameters.Handle](portalmaterial/parameterhandle(name:).md)
  Returns a handle for the parameter with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/setparameter(name:value:))*