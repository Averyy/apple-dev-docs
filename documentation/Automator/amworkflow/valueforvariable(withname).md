# valueForVariable(withName:)

**Framework**: Automator  
**Kind**: method

Returns the value of the workflow variable with the specified name.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func valueForVariable(withName variableName: String) -> Any?
```

#### Return Value

The value for the variable. Returns `nil` if no variable is found with the specified name.

## Parameters

- `variableName`: The variable name.

## See Also

- [var actions: [AMAction]](amworkflow/actions.md)
  An array of the workflow’s actions.
- [var fileURL: URL?](amworkflow/fileurl.md)
  A URL that specifies the location of the workflow file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/valueforvariable(withname:))*