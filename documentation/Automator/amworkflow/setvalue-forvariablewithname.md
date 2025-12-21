# setValue(_:forVariableWithName:)

**Framework**: Automator  
**Kind**: method

Sets the value of the workflow variable with the specified name.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func setValue(_ value: Any?, forVariableWithName variableName: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `variableName` was found and its value is set; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method does nothing if the variable specified by `variableName` is not found.

## Parameters

- `value`: The value to set for the named variable.
- `variableName`: The name of a variable to set the value for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/setvalue(_:forvariablewithname:))*