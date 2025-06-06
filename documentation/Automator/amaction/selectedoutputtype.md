# selectedOutputType

**Framework**: Automator  
**Kind**: property

The type of output, in UTI format, of the output to be produced by the action.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.6+

## Declaration

```swift
var selectedOutputType: String? { get set }
```

#### Discussion

Getting this value provides the type of output the action is configured to produce. For example, your action may have the ability to output files and folders, or documents, depending on how it’s configured or what it encounters while processing.

The output types the action supports are specified in the action’s `Info.plist` file. By default, this property defaults to the first output type in the `Info.plist` file.

Set this value to explicitly specify the output type the action produces. Setting this value to accurately reflect the appropriate output helps Automator determine whether the output is compatible, or can be made compatible, with the next action in the workflow.

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
- [var isStopped: Bool](amaction/isstopped.md)
  A Boolean value that indicates whether the user clicked the stop button on the parent workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/selectedoutputtype)*