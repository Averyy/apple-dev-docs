# Command Encoder Factory Methods

**Framework**: Metal

A command encoder defines the actions of a single pass, such as GPU commands that draw, compute, or quickly copy resource data.

## Topics

### Creating Render Encoders
- [func makeRenderCommandEncoder(descriptor: MTLRenderPassDescriptor) -> (any MTLRenderCommandEncoder)?](mtlcommandbuffer/makerendercommandencoder(descriptor:).md)
  Creates a render command encoder from a descriptor.
### Creating Parallel Render Encoders
- [func makeParallelRenderCommandEncoder(descriptor: MTLRenderPassDescriptor) -> (any MTLParallelRenderCommandEncoder)?](mtlcommandbuffer/makeparallelrendercommandencoder(descriptor:).md)
  Creates a parallel render command encoder from a descriptor.
### Creating Acceleration Structure Encoders
- [func makeAccelerationStructureCommandEncoder(descriptor: MTLAccelerationStructurePassDescriptor) -> any MTLAccelerationStructureCommandEncoder](mtlcommandbuffer/makeaccelerationstructurecommandencoder(descriptor:).md)
  Creates a ray-tracing acceleration structure command encoder from a descriptor.
- [func makeAccelerationStructureCommandEncoder() -> (any MTLAccelerationStructureCommandEncoder)?](mtlcommandbuffer/makeaccelerationstructurecommandencoder.md)
  Creates a ray-tracing acceleration structure command encoder that uses default settings.
### Creating Compute Encoders
- [func makeComputeCommandEncoder(descriptor: MTLComputePassDescriptor) -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder(descriptor:).md)
  Creates a compute command encoder from a descriptor.
- [func makeComputeCommandEncoder() -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder.md)
  Creates a compute command encoder that uses default settings.
- [func makeComputeCommandEncoder(dispatchType: MTLDispatchType) -> (any MTLComputeCommandEncoder)?](mtlcommandbuffer/makecomputecommandencoder(dispatchtype:).md)
  Creates a compute command encoder with a dispatch type.
- [enum MTLDispatchType](mtldispatchtype.md)
  The type of dispatch method to use when calling encoded functions.
### Creating Blit Encoders
- [func makeBlitCommandEncoder() -> (any MTLBlitCommandEncoder)?](mtlcommandbuffer/makeblitcommandencoder.md)
  Creates a block information transfer (blit) encoder.
- [func makeBlitCommandEncoder(descriptor: MTLBlitPassDescriptor) -> (any MTLBlitCommandEncoder)?](mtlcommandbuffer/makeblitcommandencoder(descriptor:).md)
  Creates a block information transfer (blit) encoder from a descriptor.
### Creating Resource State Encoders
- [func resourceStateCommandEncoder(with: MTLResourceStatePassDescriptor) -> (any MTLResourceStateCommandEncoder)?](mtlcommandbuffer/resourcestatecommandencoder(with:).md)
  Creates a resource state command encoder from a descriptor.
- [func makeResourceStateCommandEncoder() -> (any MTLResourceStateCommandEncoder)?](mtlcommandbuffer/makeresourcestatecommandencoder.md)
  Creates a resource state command encoder that uses default settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/command-encoder-factory-methods)*