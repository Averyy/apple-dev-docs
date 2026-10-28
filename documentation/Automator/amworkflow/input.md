# input

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

The input data that is passed to the first action in the workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var input: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id input;
```

## Return Value

The input for the first action in the workflow. Should be a data type the action can use, or a type that can be converted to one the action can use. Use `setInput:` to set the input data for the workflow.

## See Also

### Working with the Workflow’s Input and Output
- [var output: Any?](./output.md)
  The output data that is provided by the last action in the workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflow/input)*