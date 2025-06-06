# output

**Framework**: Automator  
**Kind**: property

The action’s output.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
var output: Any? { get set }
```

#### Return Value

The receiving action’s output, or `nil` if called before the action is run.

#### Discussion

`nil` if called before the action is run.

This method is used in conjunction with the [`AMWorkflow`](amworkflow.md) class, which allows access to the actions in a workflow. Within a workflow, for example, you might iteratively inspect the output of each action. Or, on completion of a workflow, you might examine the output of the last action, to determine the output of the workflow.

This parameter can also be used when running an action asynchronously. Call `setOutput` to specify the output the action produces.

## See Also

- [var name: String](amaction/name.md)
  The name of the action.
- [var progressValue: CGFloat](amaction/progressvalue.md)
  A float value between 0 and 1, which indicates how far along the action is while processing.
- [var ignoresInput: Bool](amaction/ignoresinput.md)
  A Boolean value that indicates whether the action acts upon its input or the input is ignored.
- [var selectedInputType: String?](amaction/selectedinputtype.md)
  The type of input, in UTI format, of the input received by the action.
- [var selectedOutputType: String?](amaction/selectedoutputtype.md)
  The type of output, in UTI format, of the output to be produced by the action.
- [var isStopped: Bool](amaction/isstopped.md)
  A Boolean value that indicates whether the user clicked the stop button on the parent workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/output)*