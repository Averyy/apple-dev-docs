# inheritBuffers

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines where commands in the indirect command buffer get their buffer arguments from when you execute them.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var inheritBuffers: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL inheritBuffers;
```

#### Discussion

Always set this property explicitly.

If you set the value to [`true`](../../Swift/true.md), don’t set buffer arguments when you encode commands into the indirect command buffer. The commands use (inherit) the buffer arguments that you set on the parent encoder.

If you set the value to [`false`](../../Swift/false.md), set the buffer arguments when you encode the commands into the indirect command buffer. The commands ignore any buffer arguments set on the parent encoder.

## See Also

### Declaring command inheritance
- [var inheritPipelineState: Bool](./inheritpipelinestate.md)
  A Boolean value that determines where commands in the indirect command buffer get their pipeline state from when you execute them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbufferdescriptor/inheritbuffers)*