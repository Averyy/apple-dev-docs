# fragmentBuffers

**Framework**: Metal  
**Kind**: property

An array that contains the buffer mutability options for a render pipeline’s fragment function.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var fragmentBuffers: MTLPipelineBufferDescriptorArray { get }
```

#### Discussion

This property returns an array of [`MTLPipelineBufferDescriptor`](mtlpipelinebufferdescriptor.md) instances, where each element corresponds to the index in the buffer argument table for the render pipeline’s fragment function.

```objective-c
// Indicate the fragment buffer at index 8 is immutable while setting up the render pipeline.
MTLRenderPipelineDescriptor *renderDescriptor = [MTLRenderPipelineDescriptor new];
renderDescriptor.fragmentBuffers[8].mutability = MTLMutabilityImmutable;

// Create an encoder for the render pass.
id <MTLRenderCommandEncoder> renderEncoder;
renderEncoder = [_commandBuffer renderCommandEncoderWithDescriptor:_renderPassDescriptor];

// Assign the buffer at index 8 for the render pass.
[renderEncoder setFragmentBuffer:_buffer offset:0 atIndex:8];
```

## See Also

- [var vertexBuffers: MTLPipelineBufferDescriptorArray](mtlrenderpipelinedescriptor/vertexbuffers.md)
  An array that contains the buffer mutability options for a render pipeline’s vertex function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/fragmentbuffers)*