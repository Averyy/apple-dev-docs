# makeCommandBuffer()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeCommandBuffer() -> (any MTL4CommandBuffer)?
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Return Value

A [`MTL4CommandBuffer`](mtl4commandbuffer.md) instance, or `nil` if the function failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecommandbuffer())*