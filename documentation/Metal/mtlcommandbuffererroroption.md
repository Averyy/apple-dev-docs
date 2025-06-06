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

### Buffer Error Options
- [static var encoderExecutionStatus: MTLCommandBufferErrorOption](mtlcommandbuffererroroption/encoderexecutionstatus.md)
  An option that instructs a command buffer to save additional details about a GPU runtime error.
### Protocol Support
- [init(rawValue: UInt)](mtlcommandbuffererroroption/init(rawvalue:).md)
  Creates a set of error options from a raw integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var logState: (any MTLLogState)?](mtlcommandbufferdescriptor/logstate.md)
  The shader logging configuration that the command buffer uses.
- [var retainedReferences: Bool](mtlcommandbufferdescriptor/retainedreferences.md)
  A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [var errorOptions: MTLCommandBufferErrorOption](mtlcommandbufferdescriptor/erroroptions.md)
  The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffererroroption)*