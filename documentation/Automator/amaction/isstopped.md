# isStopped

**Framework**: Automator  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user clicked the stop button on the parent workflow.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var isStopped: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isStopped) BOOL stopped;
```

## Discussion

This value is [`true`](../../Swift/true.md) if the user clicked the stop button, or [`false`](../../Swift/false.md) if the workflow is still running. This property should be referenced during lengthy action processes, such as a loop, in order to determine whether to exit the operation and stop the action.

## See Also

### Getting Action Information
- [var name: String](./name.md)
  The name of the action.
- [var progressValue: CGFloat](./progressvalue.md)
  A float value between 0 and 1, which indicates how far along the action is while processing.
- [var ignoresInput: Bool](./ignoresinput.md)
  A Boolean value that indicates whether the action acts upon its input or the input is ignored.
- [var output: Any?](./output.md)
  The action’s output.
- [var selectedInputType: String?](./selectedinputtype.md)
  The type of input, in UTI format, of the input received by the action.
- [var selectedOutputType: String?](./selectedoutputtype.md)
  The type of output, in UTI format, of the output to be produced by the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/isstopped)*