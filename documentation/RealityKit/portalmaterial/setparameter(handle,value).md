# setParameter(handle:value:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Sets the value of a parameter identified by a handle.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func setParameter(handle: MaterialParameters.Handle, value newValue: MaterialParameters.Value) throws
```

## Discussion

Use this overload alongside [`parameterHandle(name:)`](./parameterhandle%28name%29.md) when you update the same parameter often enough that avoiding repeated name lookups matters. For one-off updates, [`setParameter(name:value:)`](./setparameter%28name,value%29.md) is more readable.

> **Throws**: An error if the parameter doesn’t exist on this material’s program, or if the value’s type doesn’t match the parameter’s declared type.

## Parameters

- `handle`: A handle previously returned by [`parameterHandle(name:)`](./parameterhandle%28name%29.md).

## See Also

### Accessing shader parameters
- [func getParameter(name: String) -> MaterialParameters.Value?](./getparameter%28name%29.md)
  Returns the value of a parameter by name.
- [func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?](./getparameter%28handle%29.md)
  Returns the value of a parameter identified by a handle.
- [func setParameter(name: String, value: MaterialParameters.Value) throws](./setparameter%28name,value%29.md)
  Sets the value of a parameter by name.
- [static func parameterHandle(name: String) -> MaterialParameters.Handle](./parameterhandle%28name%29.md)
  Returns a handle for the parameter with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/setparameter(handle:value:))*