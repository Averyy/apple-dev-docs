# indirectComputeCommand(at:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Gets the compute command at the given index.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0 (renamed: indirectComputeCommandAt)
- iPadOS 13.0+ - Deprecated in 14.0 (renamed: indirectComputeCommandAt)
- Mac Catalyst 14.0+ - Deprecated in 14.0 (renamed: indirectComputeCommandAt)
- tvOS 13.0+ - Deprecated in 14.0 (renamed: indirectComputeCommandAt)
- visionOS

## Declaration

```swift
func indirectComputeCommand(at Index: Int) -> any MTLIndirectComputeCommand
```

#### Discussion

Call this method only if the indirect command buffer contains compute commands.

## Parameters

- `Index`: The index of the command to retrieve.

## See Also

### Retrieving commands
- [func indirectRenderCommandAt(Int) -> any MTLIndirectRenderCommand](./indirectrendercommandat%28_%29.md)
  Gets the render command at the given index.
- [func indirectComputeCommandAt(Int) -> any MTLIndirectComputeCommand](./indirectcomputecommandat%28_%29.md)
  Gets the compute command at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommand(at:))*