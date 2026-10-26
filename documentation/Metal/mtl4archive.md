# MTL4Archive

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

A read-only container that stores pipeline states from a shader compiler.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4Archive : NSObjectProtocol, Sendable
```

```objc
@protocol MTL4Archive <NSObject>
```

#### Overview

The pipeline states can have intermediate representation (IR) binaries, GPU- and system-specific binaries, or a combination.

## Topics

### Identifying the archive
- [var label: String?](./mtl4archive/label.md)
  A label that you can associate with this archive.
### Creating binary functions
- [func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor) throws -> any MTL4BinaryFunction](./mtl4archive/makebinaryfunction%28descriptor%29.md)
  Synchronously creates a binary version of a GPU visible function or GPU intersection function.
### Instance Methods
- [func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor?) throws -> any MTLComputePipelineState](./mtl4archive/makecomputepipelinestate%28descriptor,dynamiclinkingdescriptor%29.md)
  Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.
- [func makeRenderPipelineState(descriptor: MTL4PipelineDescriptor, dynamicLinkingDescriptor: MTL4RenderPipelineDynamicLinkingDescriptor?) throws -> any MTLRenderPipelineState](./mtl4archive/makerenderpipelinestate%28descriptor,dynamiclinkingdescriptor%29.md)
  Creates a render pipeline state from the archive with a render descriptor and a dynamic linking descriptor.
### Creating compute pipeline states
- [- newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:](./mtl4archive/newcomputepipelinestatewithdescriptor_dynamiclinkingdescriptor_error_.md)
  Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.
- [- newComputePipelineStateWithDescriptor:error:](./mtl4archive/newcomputepipelinestatewithdescriptor_error_.md)
  Creates a compute pipeline state from the archive with a descriptor.
### Creating render pipeline states
- [- newRenderPipelineStateWithDescriptor:dynamicLinkingDescriptor:error:](./mtl4archive/newrenderpipelinestatewithdescriptor_dynamiclinkingdescriptor_error_.md)
  Creates a render pipeline state from the archive with a render descriptor and a dynamic linking descriptor.
- [- newRenderPipelineStateWithDescriptor:error:](./mtl4archive/newrenderpipelinestatewithdescriptor_error_.md)
  Creates a render pipeline state from the archive with a descriptor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Shader compilation
- [Metal libraries](./metal-libraries.md)
  Compile and manage Metal libraries from the command line.
- [Metal dynamic libraries](./metal-dynamic-libraries.md)
  Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal binary archives](./metal-binary-archives.md)
  Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
- [protocol MTL4Compiler](./mtl4compiler.md)
  A abstraction for a pipeline state and shader function compiler.
- [class MTL4CompilerDescriptor](./mtl4compilerdescriptor.md)
  Groups together properties for creating a compiler context.
- [class MTL4CompilerTaskOptions](./mtl4compilertaskoptions.md)
  The configuration options that control the behavior of a compilation task for a Metal 4 compiler instance.
- [enum MTL4CompilerTaskStatus](./mtl4compilertaskstatus.md)
  Represents the status of a compiler task.
- [protocol MTL4BinaryFunction](./mtl4binaryfunction.md)
  Represents a binary function.
- [class MTL4BinaryFunctionDescriptor](./mtl4binaryfunctiondescriptor.md)
  Base interface for other function-derived interfaces.
- [struct MTL4BinaryFunctionOptions](./mtl4binaryfunctionoptions.md)
  Options for configuring the creation of binary functions.
- [class MTL4PipelineStageDynamicLinkingDescriptor](./mtl4pipelinestagedynamiclinkingdescriptor.md)
  Groups together properties to drive the dynamic linking process of a pipeline stage.
- [MTL4CompilerTask](./mtl4compilertask.md)
  A reference to an asynchronous compilation task that you initiate from a compiler instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4archive)*