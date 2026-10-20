# indirectComputeCommandAt(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MTLIndirectComputeCommand>) indirectComputeCommandAtIndex:(NSUInteger) commandIndex;
```

#### Discussion

Call this method only if the indirect command buffer contains compute commands.

## Parameters

- `commandIndex`: The index of the command to retrieve.

## See Also

### Retrieving commands
- [func indirectRenderCommandAt(Int) -> any MTLIndirectRenderCommand](./indirectrendercommandat%28_%29.md)
  Gets the render command at the given index.
- [func indirectComputeCommand(at: Int) -> any MTLIndirectComputeCommand](./indirectcomputecommand%28at%29.md)
  Gets the compute command at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommandat(_:))*