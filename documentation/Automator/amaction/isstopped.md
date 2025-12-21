# isStopped

**Framework**: Automator  
**Kind**: property

A Boolean value that indicates whether the user clicked the stop button on the parent workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var isStopped: Bool { get }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/Swift/true) if the user clicked the stop button, or [`false`](https://developer.apple.com/documentation/Swift/false) if the workflow is still running. This property should be referenced during lengthy action processes, such as a loop, in order to determine whether to exit the operation and stop the action.

## See Also

- [var name: String](amaction/name.md)
  The name of the action.
- [var progressValue: CGFloat](amaction/progressvalue.md)
  A float value between 0 and 1, which indicates how far along the action is while processing.
- [var ignoresInput: Bool](amaction/ignoresinput.md)
  A Boolean value that indicates whether the action acts upon its input or the input is ignored.
- [var output: Any?](amaction/output.md)
  The action’s output.
- [var selectedInputType: String?](amaction/selectedinputtype.md)
  The type of input, in UTI format, of the input received by the action.
- [var selectedOutputType: String?](amaction/selectedoutputtype.md)
  The type of output, in UTI format, of the output to be produced by the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/isstopped)*