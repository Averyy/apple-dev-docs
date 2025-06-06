# inheritPipelineState

**Framework**: Metal  
**Kind**: property

A Boolean value that determines where commands in the indirect command buffer get their pipeline state from when you execute them.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var inheritPipelineState: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false). If the value is [`false`](https://developer.apple.com/documentation/swift/false), set the pipeline state object when you encode the commands into the indirect command buffer. The commands ignore any pipeline state object set on the parent encoder.

If you set the value to [`true`](https://developer.apple.com/documentation/swift/true), don’t set a pipeline state object when you encode commands into the indirect command buffer. The commands use (inherit) the pipeline stage object that you set on the parent encoder.

In IOS prior to iOS 13, and tvOS prior to tvOS 13, this property didn’t exist. If you create an indirect command buffer on those systems, it inherits the pipeline state, exactly as if the property existed, with a value of [`true`](https://developer.apple.com/documentation/swift/true). If you need your app to run on earlier versions of iOS, use an availability attribute to set the property conditionally:

## See Also

- [var inheritBuffers: Bool](mtlindirectcommandbufferdescriptor/inheritbuffers.md)
  A Boolean value that determines where commands in the indirect command buffer get their buffer arguments from when you execute them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/inheritpipelinestate)*