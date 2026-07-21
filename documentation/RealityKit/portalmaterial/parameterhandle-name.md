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

#### Return Value

A handle that identifies the parameter on any [`PortalMaterial`](portalmaterial.md) whose program declares an input with the given name.

#### Discussion

Handles bypass the per-call string lookup that [`setParameter(name:value:)`](portalmaterial/setparameter(name:value:).md) and [`getParameter(name:)`](portalmaterial/getparameter(name:).md) perform. In performance-sensitive code that updates the same parameter every frame, obtain a handle once during setup and reuse it.

## Parameters

- `name`: The name of the parameter as declared in the shader graph.

## See Also

- [func getParameter(name: String) -> MaterialParameters.Value?](portalmaterial/getparameter(name:).md)
  Returns the value of a parameter by name.
- [func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?](portalmaterial/getparameter(handle:).md)
  Returns the value of a parameter identified by a handle.
- [func setParameter(name: String, value: MaterialParameters.Value) throws](portalmaterial/setparameter(name:value:).md)
  Sets the value of a parameter by name.
- [func setParameter(handle: MaterialParameters.Handle, value: MaterialParameters.Value) throws](portalmaterial/setparameter(handle:value:).md)
  Sets the value of a parameter identified by a handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/parameterhandle(name:))*