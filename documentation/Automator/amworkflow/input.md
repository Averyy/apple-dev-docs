# input

**Framework**: Automator  
**Kind**: property

The input data that is passed to the first action in the workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var input: Any? { get set }
```

#### Return Value

The input for the first action in the workflow. Should be a data type the action can use, or a type that can be converted to one the action can use. Use `setInput:` to set the input data for the workflow.

## See Also

- [var output: Any?](amworkflow/output.md)
  The output data that is provided by the last action in the workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/input)*