# parameterHandle(name:)

**Framework**: RealityKit  
**Kind**: method

Returns a handle for the parameter with the given name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func parameterHandle(name: String) -> MaterialParameters.Handle
```

#### Discussion

Handles provide a faster path for repeated parameter access compared to name-based lookups. Obtain a handle once and reuse it across frames.

## Parameters

- `name`: The name of the parameter as declared in the shader graph.

## See Also

- [func getParameter(name: String) -> MaterialParameters.Value?](portalmaterial/getparameter(name:).md)
  Returns the current value of a parameter by name, or `nil` if no value has been set.
- [func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?](portalmaterial/getparameter(handle:).md)
  Returns the current value of a parameter identified by its precomputed handle, or `nil` if no value has been set.
- [func setParameter(name: String, value: MaterialParameters.Value) throws](portalmaterial/setparameter(name:value:).md)
  Sets the value of a parameter by name.
- [func setParameter(handle: MaterialParameters.Handle, value: MaterialParameters.Value) throws](portalmaterial/setparameter(handle:value:).md)
  Sets the value of a parameter identified by its precomputed handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/parameterhandle(name:))*