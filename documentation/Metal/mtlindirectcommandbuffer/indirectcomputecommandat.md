# indirectComputeCommandAt(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Gets the compute command at the given index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func indirectComputeCommandAt(_ commandIndex: Int) -> any MTLIndirectComputeCommand
```

#### Discussion

Call this method only if the indirect command buffer contains compute commands.

## Parameters

- `commandIndex`: The index of the command to retrieve.

## See Also

- [func indirectRenderCommandAt(Int) -> any MTLIndirectRenderCommand](mtlindirectcommandbuffer/indirectrendercommandat(_:).md)
  Gets the render command at the given index.
- [func indirectComputeCommand(at: Int) -> any MTLIndirectComputeCommand](mtlindirectcommandbuffer/indirectcomputecommand(at:).md)
  Gets the compute command at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommandat(_:))*