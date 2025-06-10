# MTL4Compiler

**Framework**: Metal  
**Kind**: protocol

A abstraction for a pipeline state and shader function compiler.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTL4Compiler : NSObjectProtocol, Sendable
```

## Mentions

- [Using the Metal 4 compilation API](using-the-metal-4-compilation-api.md)

## Topics

### Instance Properties
- [var device: any MTLDevice](mtl4compiler/device.md)
  Returns the device that this compiler belongs to.
- [var label: String?](mtl4compiler/label.md)
  Returns the optional label you specify at creation time.
- [var pipelineDataSetSerializer: (any MTL4PipelineDataSetSerializer)?](mtl4compiler/pipelinedatasetserializer.md)
  Returns the pipeline data set serializer into which this compiler stores data for all pipelines it creates.
### Instance Methods
- [func cancel()](mtl4compiler/cancel.md)
  Cancels all pending compiler tasks for this compiler.
- [func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor, compilerTaskOptions: MTL4CompilerTaskOptions?) throws -> any MTL4BinaryFunction](mtl4compiler/makebinaryfunction(descriptor:compilertaskoptions:)-5o46e.md)
  Creates a new binary visible or intersection function synchronously.
- [func makeBinaryFunction(descriptor: MTL4BinaryFunctionDescriptor, compilerTaskOptions: MTL4CompilerTaskOptions?) async throws -> any MTL4BinaryFunction](mtl4compiler/makebinaryfunction(descriptor:compilertaskoptions:)-hkc4.md)
  Creates a new binary visible or intersection function asynchronously.
- [func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor?, compilerTaskOptions: MTL4CompilerTaskOptions?) async throws -> any MTLComputePipelineState](mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-19x.md)
  Creates a new compute pipeline state asynchronously.
- [func makeComputePipelineState(descriptor: MTL4ComputePipelineDescriptor, dynamicLinkingDescriptor: MTL4PipelineStageDynamicLinkingDescriptor?, compilerTaskOptions: MTL4CompilerTaskOptions?) throws -> any MTLComputePipelineState](mtl4compiler/makecomputepipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-7dqdm.md)
  Creates a new compute pipeline state object synchronously.
- [func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary](mtl4compiler/makedynamiclibrary(library:).md)
  Creates a new dynamic library from a library containing Metal IR code synchronously.
- [func makeDynamicLibrary(url: URL) throws -> any MTLDynamicLibrary](mtl4compiler/makedynamiclibrary(url:).md)
  Creates a new dynamic library from the contents of a file at an URL location synchronously.
- [func makeLibrary(descriptor: MTL4LibraryDescriptor) throws -> any MTLLibrary](mtl4compiler/makelibrary(descriptor:).md)
  Creates a new Metal library synchronously.
- [func makeMachineLearningPipelineState(descriptor: MTL4MachineLearningPipelineDescriptor) async throws -> any MTL4MachineLearningPipelineState](mtl4compiler/makemachinelearningpipelinestate(descriptor:)-36hxx.md)
  Creates a new machine learning pipeline state asynchronously.
- [func makeMachineLearningPipelineState(descriptor: MTL4MachineLearningPipelineDescriptor) throws -> any MTL4MachineLearningPipelineState](mtl4compiler/makemachinelearningpipelinestate(descriptor:)-909v1.md)
  Creates a new ML pipeline state with descriptor.
- [func makeRenderPipelineState(descriptor: MTL4PipelineDescriptor, dynamicLinkingDescriptor: MTL4RenderPipelineDynamicLinkingDescriptor?, compilerTaskOptions: MTL4CompilerTaskOptions?) async throws -> any MTLRenderPipelineState](mtl4compiler/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-66wsk.md)
  Creates a new render pipeline state asynchronously.
- [func makeRenderPipelineState(descriptor: MTL4PipelineDescriptor, dynamicLinkingDescriptor: MTL4RenderPipelineDynamicLinkingDescriptor?, compilerTaskOptions: MTL4CompilerTaskOptions?) throws -> any MTLRenderPipelineState](mtl4compiler/makerenderpipelinestate(descriptor:dynamiclinkingdescriptor:compilertaskoptions:)-84kox.md)
  Creates a new render pipeline state synchronously.
- [func makeRenderPipelineStateBySpecialization(descriptor: MTL4PipelineDescriptor, pipeline: any MTLRenderPipelineState) throws -> any MTLRenderPipelineState](mtl4compiler/makerenderpipelinestatebyspecialization(descriptor:pipeline:)-2636j.md)
  Creates a new render pipeline state from another, previously unspecialized, pipeline state.
- [func makeRenderPipelineStateBySpecialization(descriptor: MTL4PipelineDescriptor, pipeline: any MTLRenderPipelineState) async throws -> any MTLRenderPipelineState](mtl4compiler/makerenderpipelinestatebyspecialization(descriptor:pipeline:)-7s2wp.md)
  Creates a new render pipeline state from another, previously unspecialized, pipeline state

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
- [class MTL4CompilerDescriptor](mtl4compilerdescriptor.md)
  Groups together properties for creating a compiler context.
- [class MTL4CompilerTaskOptions](mtl4compilertaskoptions.md)
- [enum MTL4CompilerTaskStatus](mtl4compilertaskstatus.md)
  Represents the status of a compiler task.
- [protocol MTL4Archive](mtl4archive.md)
  A read-only container that stores pipeline states from a shader compiler.
- [protocol MTL4BinaryFunction](mtl4binaryfunction.md)
  Represents a binary function.
- [class MTL4BinaryFunctionDescriptor](mtl4binaryfunctiondescriptor.md)
  Base interface for other function-derived interfaces.
- [struct MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md)
  Options for configuring the creation of binary functions.
- [struct MTL4BinaryFunctionOptions](mtl4binaryfunctionoptions.md)
  Options for configuring the creation of binary functions.
- [class MTL4BinaryFunctionReflection](mtl4binaryfunctionreflection.md)
  Represents reflection information for a binary function.
- [class MTL4PipelineStageDynamicLinkingDescriptor](mtl4pipelinestagedynamiclinkingdescriptor.md)
  Groups together properties to drive the dynamic linking process of a pipeline stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler)*