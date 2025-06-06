# indirectComputeCommand(at:)

**Framework**: Metal  
**Kind**: method

Gets the compute command at the given index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func indirectComputeCommand(at Index: Int) -> any MTLIndirectComputeCommand
```

#### Discussion

Call this method only if the indirect command buffer contains compute commands.

## Parameters

- `Index`: The index of the command to retrieve.

## See Also

- [func indirectRenderCommandAt(Int) -> any MTLIndirectRenderCommand](mtlindirectcommandbuffer/indirectrendercommandat(_:).md)
  Gets the render command at the given index.
- [func indirectComputeCommandAt(Int) -> any MTLIndirectComputeCommand](mtlindirectcommandbuffer/indirectcomputecommandat(_:).md)
  Gets the compute command at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommand(at:))*