# name

**Framework**: Automator  
**Kind**: property

The name of the action.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
var name: String { get }
```

## See Also

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
- [var isStopped: Bool](amaction/isstopped.md)
  A Boolean value that indicates whether the user clicked the stop button on the parent workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/name)*