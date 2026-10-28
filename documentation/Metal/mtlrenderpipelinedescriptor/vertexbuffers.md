# vertexBuffers

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array that contains the buffer mutability options for a render pipeline’s vertex function.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var vertexBuffers: MTLPipelineBufferDescriptorArray { get }
```

```objc
@property (readonly) MTLPipelineBufferDescriptorArray * vertexBuffers;
```

## Discussion

This property returns an array of [`MTLPipelineBufferDescriptor`](../mtlpipelinebufferdescriptor.md) instances, where each element corresponds to the same index in the buffer argument table for the render pipeline’s vertex function.

```objective-c
// Indicate the vertex buffer at index 7 is immutable while setting up the render pipeline.
MTLRenderPipelineDescriptor *renderDescriptor = [MTLRenderPipelineDescriptor new];
renderDescriptor.vertexBuffers[7].mutability = MTLMutabilityImmutable;

// Create an encoder for the render pass.
id <MTLRenderCommandEncoder> renderEncoder;
renderEncoder = [_commandBuffer renderCommandEncoderWithDescriptor:_renderPassDescriptor];

// Assign the buffer at index 7 for the render pass.
[renderEncoder setVertexBuffer:_buffer offset:0 atIndex:7];
```

## See Also

### Specifying buffer mutability
- [var fragmentBuffers: MTLPipelineBufferDescriptorArray](./fragmentbuffers.md)
  An array that contains the buffer mutability options for a render pipeline’s fragment function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/vertexbuffers)*