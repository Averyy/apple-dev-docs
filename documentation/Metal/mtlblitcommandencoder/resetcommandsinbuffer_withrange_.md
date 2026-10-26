# resetCommandsInBuffer:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that resets a range of commands in an indirect command buffer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```objc
- (void) resetCommandsInBuffer:(id<MTLIndirectCommandBuffer>) buffer withRange:(NSRange) range;
```

## Parameters

- `buffer`: An indirect command buffer the command resets.
- `range`: A range of commands within `buffer`.

## See Also

### Managing indirect command buffers
- [- copyIndirectCommandBuffer:sourceRange:destination:destinationIndex:](./copyindirectcommandbuffer_sourcerange_destination_destinationindex_.md)
  Encodes a command that copies commands from one indirect command buffer into another.
- [- optimizeIndirectCommandBuffer:withRange:](./optimizeindirectcommandbuffer_withrange_.md)
  Encodes a command that can improve the performance of a range of commands within an indirect command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resetcommandsinbuffer:withrange:)*