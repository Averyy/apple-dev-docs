# resetCommandsInBuffer:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that resets a range of commands in an indirect command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) resetCommandsInBuffer:(id<MTLIndirectCommandBuffer>) buffer withRange:(NSRange) range;
```

## Parameters

- `buffer`: An [`MTLIndirectCommandBuffer`](../mtlindirectcommandbuffer.md) the command resets.
- `range`: A range of commands within `buffer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/resetcommandsinbuffer:withrange:)*