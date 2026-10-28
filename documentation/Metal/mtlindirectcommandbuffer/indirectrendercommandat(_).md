# indirectRenderCommandAt(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the render command at the given index.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func indirectRenderCommandAt(_ commandIndex: Int) -> any MTLIndirectRenderCommand
```

```objc
- (id<MTLIndirectRenderCommand>) indirectRenderCommandAtIndex:(NSUInteger) commandIndex;
```

## Discussion

Call this method only if the indirect command buffer contains rendering commands.

## Parameters

- `commandIndex`: The index of the command to retrieve.

## See Also

### Retrieving commands
- [func indirectComputeCommandAt(Int) -> any MTLIndirectComputeCommand](./indirectcomputecommandat%28_%29.md)
  Gets the compute command at the given index.
- [func indirectComputeCommand(at: Int) -> any MTLIndirectComputeCommand](./indirectcomputecommand%28at%29.md)
  Gets the compute command at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/indirectrendercommandat(_:))*