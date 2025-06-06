# logState

**Framework**: Metal  
**Kind**: property

The shader logging configuration that the command buffer uses.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var logState: (any MTLLogState)? { get set }
```

## See Also

- [var retainedReferences: Bool](mtlcommandbufferdescriptor/retainedreferences.md)
  A Boolean value that indicates whether the command buffer the descriptor creates maintains strong references to the resources it uses.
- [var errorOptions: MTLCommandBufferErrorOption](mtlcommandbufferdescriptor/erroroptions.md)
  The reporting configuration that indicates which information the GPU driver stores in a command buffer’s error property.
- [struct MTLCommandBufferErrorOption](mtlcommandbuffererroroption.md)
  Options for reporting errors from a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferdescriptor/logstate)*