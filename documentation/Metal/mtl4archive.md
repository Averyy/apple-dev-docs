# MTL4Archive

**Framework**: Metal  
**Kind**: protocol

A read-only container that stores pipeline states from a shader compiler.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTL4Archive : NSObjectProtocol, Sendable
```

#### Overview

The pipeline states can have intermediate representation (IR) binaries, GPU- and system-specifc binaries, or a combination.

## Topics

### Identifiying the archive
- [var label: String?](mtl4archive/label.md)
  A label that you can associate with this archive.
### Instance Methods
- [func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor) throws -> any MTL4BinaryFunction](mtl4archive/makebinaryfunction(descriptor:).md)
  Method used to create a binary function, with a given descriptor, from the contents of the archive.
- [func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor?) throws -> any MTLComputePipelineState](mtl4archive/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:).md)
  Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.
- [func makeRenderPipelineState(descriptor: MTL4PipelineDescriptor, dynamicLinkingDescriptor: MTL4RenderPipelineDynamicLinkingDescriptor?) throws -> any MTLRenderPipelineState](mtl4archive/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:).md)
  Creates a render pipeline state from the archive with a render descriptor and a dynamic linking descriptor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Metal Libraries](metal-libraries.md)
  Compile and manage Metal libraries from the command line.
- [Metal Dynamic Libraries](metal-dynamic-libraries.md)
  Create a single Metal library containing reusable code to reduce library size and avoid repeated shader compilation at runtime.
- [Metal Binary Archives](metal-binary-archives.md)
  Distribute precompiled GPU-specific binaries as part of your app to avoid runtime compilation of Metal shaders.
- [protocol MTL4Compiler](mtl4compiler.md)
  A abstraction for a pipeline state and shader function compiler.
- [class MTL4CompilerDescriptor](mtl4compilerdescriptor.md)
  Groups together properties for creating a compiler context.
- [class MTL4CompilerTaskOptions](mtl4compilertaskoptions.md)
- [enum MTL4CompilerTaskStatus](mtl4compilertaskstatus.md)
  Represents the status of a compiler task.
- [protocol MTL4BinaryFunction](mtl4binaryfunction.md)
  Represents a binary function.
- [class MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md)
  Base interface for other function-derived interfaces.
- [struct MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md)
  Options for configuring the creation of binary functions.
- [class MTL4BinaryFunctionReflection](mtl4binaryfunctionreflection.md)
  Represents reflection information for a binary function.
- [class MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md)
  Groups together properties to drive the dynamic linking process of a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4archive)*