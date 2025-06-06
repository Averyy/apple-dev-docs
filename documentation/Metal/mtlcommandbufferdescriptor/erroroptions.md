# errorOptions

**Framework**: Metal  
**Kind**: property

The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var errorOptions: MTLCommandBufferErrorOption { get set }
```

#### Discussion

By default, a GPU driver doesn’t report additional error information.

To create a command buffer that saves additional GPU runtime error information, add the [`encoderExecutionStatus`](mtlcommandbuffererroroption/encoderexecutionstatus.md) option to this property. If the GPU encounters an error as it runs the command buffer, you can retrieve the additional information from the command buffer’s [`error`](mtlcommandbuffer/error.md) property.

> **Note**:  Enabling the [`encoderExecutionStatus`](mtlcommandbuffererroroption/encoderexecutionstatus.md) option can slightly reduce your app’s CPU runtime performance.

 Enabling the [`encoderExecutionStatus`](mtlcommandbuffererroroption/encoderexecutionstatus.md) option can slightly reduce your app’s CPU runtime performance.

## See Also

- [var logState: (any MTLLogState)?](mtlcommandbufferdescriptor/logstate.md)
  The shader logging configuration that the command buffer uses.
- [var retainedReferences: Bool](mtlcommandbufferdescriptor/retainedreferences.md)
  A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [struct MTLCommandBufferErrorOption](mtlcommandbuffererroroption.md)
  Options for reporting errors from a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferdescriptor/erroroptions)*