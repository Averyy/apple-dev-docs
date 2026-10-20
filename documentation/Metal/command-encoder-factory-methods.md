# Command encoder factory methods

**Framework**: Metal  
**Role**: API Collection

A command encoder defines the actions of a single pass, such as GPU commands that draw, compute, or quickly copy resource data.

## Topics

### Creating render encoders
- [func makeRenderCommandEncoder(descriptor: MTLRenderPassDescriptor) -> (any MTLRenderCommandEncoder)?](./mtlcommandbuffer/makerendercommandencoder%28descriptor%29.md)
  Creates a render command encoder from a descriptor.
### Creating parallel render encoders
- [func makeParallelRenderCommandEncoder(descriptor: MTLRenderPassDescriptor) -> (any MTLParallelRenderCommandEncoder)?](./mtlcommandbuffer/makeparallelrendercommandencoder%28descriptor%29.md)
  Creates a parallel render command encoder from a descriptor.
### Creating acceleration structure encoders
- [func makeAccelerationStructureCommandEncoder(descriptor: MTLAccelerationStructurePassDescriptor) -> any MTLAccelerationStructureCommandEncoder](./mtlcommandbuffer/makeaccelerationstructurecommandencoder%28descriptor%29.md)
  Creates a ray-tracing acceleration structure command encoder from a descriptor.
- [func makeAccelerationStructureCommandEncoder() -> (any MTLAccelerationStructureCommandEncoder)?](./mtlcommandbuffer/makeaccelerationstructurecommandencoder%28%29.md)
  Creates a ray-tracing acceleration structure command encoder that uses default settings.
### Creating compute encoders
- [func makeComputeCommandEncoder(descriptor: MTLComputePassDescriptor) -> (any MTLComputeCommandEncoder)?](./mtlcommandbuffer/makecomputecommandencoder%28descriptor%29.md)
  Creates a compute command encoder from a descriptor.
- [func makeComputeCommandEncoder() -> (any MTLComputeCommandEncoder)?](./mtlcommandbuffer/makecomputecommandencoder%28%29.md)
  Creates a compute command encoder that uses default settings.
- [func makeComputeCommandEncoder(dispatchType: MTLDispatchType) -> (any MTLComputeCommandEncoder)?](./mtlcommandbuffer/makecomputecommandencoder%28dispatchtype%29.md)
  Creates a compute command encoder with a dispatch type.
- [enum MTLDispatchType](./mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.
### Creating blit encoders
- [func makeBlitCommandEncoder() -> (any MTLBlitCommandEncoder)?](./mtlcommandbuffer/makeblitcommandencoder%28%29.md)
  Creates a block information transfer (blit) encoder.
- [func makeBlitCommandEncoder(descriptor: MTLBlitPassDescriptor) -> (any MTLBlitCommandEncoder)?](./mtlcommandbuffer/makeblitcommandencoder%28descriptor%29.md)
  Creates a block information transfer (blit) encoder from a descriptor.
### Creating resource state encoders
- [func resourceStateCommandEncoder(with: MTLResourceStatePassDescriptor) -> (any MTLResourceStateCommandEncoder)?](./mtlcommandbuffer/resourcestatecommandencoder%28with%29.md)
  Creates a resource state command encoder from a descriptor.
- [func makeResourceStateCommandEncoder() -> (any MTLResourceStateCommandEncoder)?](./mtlcommandbuffer/makeresourcestatecommandencoder%28%29.md)
  Creates a resource state command encoder that uses default settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/command-encoder-factory-methods)*