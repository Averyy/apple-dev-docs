# MTLCommandBufferErrorOption

**Framework**: Metal  
**Kind**: struct

Options for reporting errors from a command buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLCommandBufferErrorOption
```

## Topics

### Buffer error options
- [static var encoderExecutionStatus: MTLCommandBufferErrorOption](mtlcommandbuffererroroption/encoderexecutionstatus.md)
  An option that instructs a command buffer to save additional details about a GPU runtime error.
### Protocol support
- [init(rawValue: UInt)](mtlcommandbuffererroroption/init(rawvalue:).md)
  Creates a set of error options from a raw integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var logState: (any MTLLogState)?](mtlcommandbufferdescriptor/logstate.md)
  The shader logging configuration that the command buffer uses.
- [var retainedReferences: Bool](mtlcommandbufferdescriptor/retainedreferences.md)
  A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [var errorOptions: MTLCommandBufferErrorOption](mtlcommandbufferdescriptor/erroroptions.md)
  The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererroroption)*