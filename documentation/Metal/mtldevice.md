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
protocol MTLDevice : NSObjectProtocol
```

## Mentions

- [Finding Multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md)
- [Converting GPU Timestamps into CPU Time](converting-gpu-timestamps-into-cpu-time.md)
- [Confirming which Counters and Counter Sets a GPU Supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md)
- [Improving your game’s graphics performance and settings](improving-your-games-graphics-performance-and-settings.md)
- [Improving Rendering Performance with Vertex Amplification](improving-rendering-performance-with-vertex-amplification.md)
- [Creating Binary Archives from Device-Built Pipeline State Objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)
- [Detecting GPU Features and Metal Software Versions](detecting-gpu-features-and-metal-software-versions.md)
- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Creating Sparse Heaps and Sparse Textures](creating-sparse-heaps-and-sparse-textures.md)
- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)
- [Minimizing the Binary Size of a Shader Library](minimizing-the-binary-size-of-a-shader-library.md)
- [Getting the Default GPU](getting-the-default-gpu.md)
- [Creating an Indirect Command Buffer](creating-an-indirect-command-buffer.md)

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
- [var shouldMaximizeConcurrentCompilation: Bool](mtldevice/shouldmaximizeconcurrentcompilation.md)
### Instance Methods
- [func makeCommandQueue(descriptor: MTLCommandQueueDescriptor) -> (any MTLCommandQueue)?](mtldevice/makecommandqueue(descriptor:).md)
  Creates a command queue with the provided configuration.
- [func makeLogState(descriptor: MTLLogStateDescriptor) throws -> any MTLLogState](mtldevice/makelogstate(descriptor:).md)
  Creates a shader log state with the provided configuration.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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