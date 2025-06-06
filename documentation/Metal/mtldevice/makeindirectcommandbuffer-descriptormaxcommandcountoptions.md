# makeIndirectCommandBuffer(descriptor:maxCommandCount:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates an indirect command buffer instance.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func makeIndirectCommandBuffer(descriptor: MTLIndirectCommandBufferDescriptor, maxCommandCount maxCount: Int, options: MTLResourceOptions = []) -> (any MTLIndirectCommandBuffer)?
```

## Mentions

- [Creating an Indirect Command Buffer](creating-an-indirect-command-buffer.md)

#### Return Value

A new [`MTLIndirectCommandBuffer`](mtlindirectcommandbuffer.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `descriptor`: An   instance.
- `maxCount`: The largest number of commands you can store in the buffer.
- `options`: An   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeindirectcommandbuffer(descriptor:maxcommandcount:options:))*