# getParameter(handle:)

**Framework**: RealityKit  
**Kind**: method

Returns the current value of a parameter identified by its precomputed handle, or `nil` if no value has been set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func getParameter(handle: MaterialParameters.Handle) -> MaterialParameters.Value?
```

## Parameters

- `handle`: A handle previously obtained from [`parameterHandle(name:)`](portalmaterial/parameterhandle(name:).md).

## See Also

- [func getParameter(name: String) -> MaterialParameters.Value?](portalmaterial/getparameter(name:).md)
  Returns the current value of a parameter by name, or `nil` if no value has been set.
- [func setParameter(name: String, value: MaterialParameters.Value) throws](portalmaterial/setparameter(name:value:).md)
  Sets the value of a parameter by name.
- [func setParameter(handle: MaterialParameters.Handle, value: MaterialParameters.Value) throws](portalmaterial/setparameter(handle:value:).md)
  Sets the value of a parameter identified by its precomputed handle.
- [static func parameterHandle(name: String) -> MaterialParameters.Handle](portalmaterial/parameterhandle(name:).md)
  Returns a handle for the parameter with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/getparameter(handle:))*