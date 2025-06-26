# MTLDevice

**Framework**: Metal  
**Kind**: protocol

The main Metal interface to a GPU that apps use to draw graphics and run computations in parallel.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLDevice : NSObjectProtocol, Sendable
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)
- [Finding Multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md)
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md)
- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
- [Creating an Indirect Command Buffer](creating-an-indirect-command-buffer.md)
- [Getting the Default GPU](getting-the-default-gpu.md)
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
- [Creating Sparse Heaps and Sparse Textures](creating-sparse-heaps-and-sparse-textures.md)
- [Converting GPU Timestamps into CPU Time](converting-gpu-timestamps-into-cpu-time.md)
- [Improving Rendering Performance with Vertex Amplification](improving-rendering-performance-with-vertex-amplification.md)
- [Using the Metal 4 compilation API](using-the-metal-4-compilation-api.md)
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
- [Detecting GPU Features and Metal Software Versions](detecting-gpu-features-and-metal-software-versions.md)
- [Creating Binary Archives from Device-Built Pipeline State Objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)
- [Minimizing the Binary Size of a Shader Library](minimizing-the-binary-size-of-a-shader-library.md)

#### Overview

You can get the default [`MTLDevice`](mtldevice.md) at runtime by calling [`MTLCreateSystemDefaultDevice()`](mtlcreatesystemdefaultdevice().md) (see [`Getting the Default GPU`](getting-the-default-gpu.md)). Each Metal device instance represents a GPU and is the main starting point for your app’s interaction with it. With a Metal device instance, you can inspect a GPU’s features and capabilities (see [`Device Inspection`](device-inspection.md)) and create subsidiary type instances with its factory methods.

- Buffers, textures, and other resources store, synchronize, and pass data between the GPU and CPU (see [`Resource Fundamentals`](resource-fundamentals.md)).
- Input/Output command queues efficiently load resources from the file system (see [`Resource Loading`](resource-loading.md)).
- Command queues create command encoders and schedule work for the GPU, including rendering and compute commands (see [`Render Passes`](render-passes.md) and [`Compute Passes`](compute-passes.md)).
- Pipeline states store render or compute pipeline configurations — which can be expensive to create — so that you can reuse them, potentially many times.

If your app uses more than one GPU (see [`Multi-GPU Systems`](multi-gpu-systems.md)), ensure that instances of these types only interact with others from the same device. For example, your app can pass a texture to a command encoder that comes from the same Metal device, but not to another device.

## Topics

### Working with GPU Devices
- [Device Inspection](device-inspection.md)
  Locate and identify a GPU and the features it supports, and sample its counters.
- [Work Submission](work-submission.md)
  Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Pipeline State Creation](pipeline-state-creation.md)
  Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Resource Creation](resource-creation.md)
  Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
- [Shader Library and Archive Creation](shader-library-and-archive-creation.md)
  Create static and dynamic shader libraries, and binary shader archives.
### Instance Properties
- [var maximumConcurrentCompilationTaskCount: Int](mtldevice/maximumconcurrentcompilationtaskcount.md)
  The maximum number of concurrent compilation tasks the device is running.
- [var shouldMaximizeConcurrentCompilation: Bool](mtldevice/shouldmaximizeconcurrentcompilation.md)
  A Boolean value that indicates whether the device uses additional CPU threads for compilation tasks.
### Instance Methods
- [func functionHandle(function: any MTLFunction) -> (any MTLFunctionHandle)?](mtldevice/functionhandle(function:)-4bw39.md)
- [func functionHandle(function: any MTL4BinaryFunction) -> (any MTLFunctionHandle)?](mtldevice/functionhandle(function:)-w9ia.md)
  Get the function handle for the specified binary-linked function from the pipeline state.
- [func makeArchive(url: URL) throws -> any MTL4Archive](mtldevice/makearchive(url:).md)
  Creates a new archive from data available at an `NSURL` address.
- [func makeArgumentTable(descriptor: MTL4ArgumentTableDescriptor) throws -> any MTL4ArgumentTable](mtldevice/makeargumenttable(descriptor:).md)
  Creates a new argument table from an argument table descriptor.
- [func makeBuffer(length: Int, options: MTLResourceOptions, placementSparsePageSize: MTLSparsePageSize) -> (any MTLBuffer)?](mtldevice/makebuffer(length:options:placementsparsepagesize:).md)
  Creates a new placement sparse buffer of a specific length.
- [func makeCommandAllocator() -> (any MTL4CommandAllocator)?](mtldevice/makecommandallocator.md)
  Creates a new command allocator.
- [func makeCommandAllocator(descriptor: MTL4CommandAllocatorDescriptor) throws -> any MTL4CommandAllocator](mtldevice/makecommandallocator(descriptor:).md)
  Creates a new command allocator from a command allocator descriptor.
- [func makeCommandBuffer() -> (any MTL4CommandBuffer)?](mtldevice/makecommandbuffer.md)
  Creates a new command buffer.
- [func makeCommandQueue(descriptor: MTLCommandQueueDescriptor) -> (any MTLCommandQueue)?](mtldevice/makecommandqueue(descriptor:).md)
  Creates a command queue with the provided configuration.
- [func makeCompiler(descriptor: MTL4CompilerDescriptor) throws -> any MTL4Compiler](mtldevice/makecompiler(descriptor:).md)
  Creates a new compiler from a compiler descriptor.
- [func makeCounterHeap(descriptor: MTL4CounterHeapDescriptor) throws -> any MTL4CounterHeap](mtldevice/makecounterheap(descriptor:).md)
  Creates a new counter heap configured from a counter heap descriptor.
- [func makeLogState(descriptor: MTLLogStateDescriptor) throws -> any MTLLogState](mtldevice/makelogstate(descriptor:).md)
  Creates a shader log state with the provided configuration.
- [func makeMTL4CommandQueue() -> (any MTL4CommandQueue)?](mtldevice/makemtl4commandqueue.md)
  Creates a new command queue.
- [func makeMTL4CommandQueue(descriptor: MTL4CommandQueueDescriptor) throws -> any MTL4CommandQueue](mtldevice/makemtl4commandqueue(descriptor:).md)
  Creates a new command queue from a queue descriptor.
- [func makePipelineDataSetSerializer(descriptor: MTL4PipelineDataSetSerializerDescriptor) -> any MTL4PipelineDataSetSerializer](mtldevice/makepipelinedatasetserializer(descriptor:).md)
  Creates a new pipeline data set serializer instance from a descriptor.
- [func makeTensor(descriptor: MTLTensorDescriptor) throws -> any MTLTensor](mtldevice/maketensor(descriptor:).md)
  Creates a tensor by allocating new memory.
- [func makeTextureViewPool(descriptor: MTLResourceViewPoolDescriptor) throws -> any MTLTextureViewPool](mtldevice/maketextureviewpool(descriptor:).md)
  Creates a new texture view pool from a resource view pool descriptor.
- [func queryTimestampFrequency() -> UInt64](mtldevice/querytimestampfrequency.md)
  Queries the frequency of the GPU timestamp in ticks per second.
- [func size(ofCounterHeapEntry: MTL4CounterHeapType) -> Int](mtldevice/size(ofcounterheapentry:).md)
  Returns the size, in bytes, of each entry in a counter heap of a specific counter heap type when your app resolves it into a usable format.
- [func tensorSizeAndAlign(descriptor: MTLTensorDescriptor) -> MTLSizeAndAlign](mtldevice/tensorsizeandalign(descriptor:).md)
  Determines the size and alignment required to hold the data of a tensor you create with a descriptor in a buffer.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Getting the Default GPU](getting-the-default-gpu.md)
  Select the system’s default GPU device on which to run your Metal code.
- [Detecting GPU Features and Metal Software Versions](detecting-gpu-features-and-metal-software-versions.md)
  Use the device object’s properties to determine how you perform tasks in Metal.
- [func MTLCreateSystemDefaultDevice() -> (any MTLDevice)?](mtlcreatesystemdefaultdevice().md)
  Returns the device instance Metal selects as the default.
- [Multi-GPU Systems](multi-gpu-systems.md)
  Locate and work with internal and external GPUs and their displays, video memory, and performance tradeoffs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice)*