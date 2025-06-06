# makeParallelRenderCommandEncoder(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a parallel render command encoder from a descriptor.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeParallelRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> (any MTLParallelRenderCommandEncoder)?
```

#### Discussion

An [`MTLParallelRenderCommandEncoder`](mtlparallelrendercommandencoder.md) instance can create multiple, independent render command encoders that contribute to the same render pass on different threads.

## Parameters

- `renderPassDescriptor`: An   instance that configures the   the method returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeparallelrendercommandencoder(descriptor:))*