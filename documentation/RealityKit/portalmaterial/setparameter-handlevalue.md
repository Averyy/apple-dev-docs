# setParameter(handle:value:)

**Framework**: RealityKit  
**Kind**: method

Sets the value of a parameter identified by a handle.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func setParameter(handle: MaterialParameters.Handle, value newValue: MaterialParameters.Value) throws
```

#### Discussion

Use this overload alongside [`parameterHandle(name:)`](portalmaterial/parameterhandle(name:).md) when you update the same parameter often enough that avoiding repeated name lookups matters. For one-off updates, [`setParameter(name:value:)`](portalmaterial/setparameter(name:value:).md) is more readable.

> **Note**: An error if the parameter doesn’t exist on this material’s program, or if the value’s type doesn’t match the parameter’s declared type.

## Parameters

- `handle`: A handle previously returned by [`parameterHandle(name:)`](portalmaterial/parameterhandle(name:).md).

## See Also

- [func getParameter(name: String) -> MaterialParameters.Value?](portalmaterial/getparameter(name:).md)
  Returns the value of a parameter by name.
- [func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?](portalmaterial/getparameter(handle:).md)
  Returns the value of a parameter identified by a handle.
- [func setParameter(name: String, value: MaterialParameters.Value) throws](portalmaterial/setparameter(name:value:).md)
  Sets the value of a parameter by name.
- [static func parameterHandle(name: String) -> MaterialParameters.Handle](portalmaterial/parameterhandle(name:).md)
  Returns a handle for the parameter with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/setparameter(handle:value:))*