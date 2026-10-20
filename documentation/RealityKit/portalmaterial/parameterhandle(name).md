# parameterHandle(name:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Returns a handle for the parameter with the given name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func parameterHandle(name: String) -> MaterialParameters.Handle
```

#### Return Value

A handle that identifies the parameter on any [`PortalMaterial`](../portalmaterial.md) whose program declares an input with the given name.

#### Discussion

Handles bypass the per-call string lookup that [`setParameter(name:value:)`](./setparameter%28name,value%29.md) and [`getParameter(name:)`](./getparameter%28name%29.md) perform. In performance-sensitive code that updates the same parameter every frame, obtain a handle once during setup and reuse it.

## Parameters

- `name`: The name of the parameter as declared in the shader graph.

## See Also

### Accessing shader parameters
- [func getParameter(name: String) -> MaterialParameters.Value?](./getparameter%28name%29.md)
  Returns the value of a parameter by name.
- [func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?](./getparameter%28handle%29.md)
  Returns the value of a parameter identified by a handle.
- [func setParameter(name: String, value: MaterialParameters.Value) throws](./setparameter%28name,value%29.md)
  Sets the value of a parameter by name.
- [func setParameter(handle: MaterialParameters.Handle, value: MaterialParameters.Value) throws](./setparameter%28handle,value%29.md)
  Sets the value of a parameter identified by a handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/parameterhandle(name:))*