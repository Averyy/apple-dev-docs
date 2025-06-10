# MTLBuffer

**Framework**: Metal  
**Kind**: protocol

A resource that stores data in a format defined by your app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLBuffer : MTLResource
```

## Mentions

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Estimating How Often a Texture Region Is Accessed](estimating-how-often-a-texture-region-is-accessed.md)
- [Setting Resource Storage Modes](setting-resource-storage-modes.md)
- [Synchronizing a Managed Resource in macOS](synchronizing-a-managed-resource-in-macos.md)
- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)
- [Specifying Drawing and Dispatch Arguments Indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)
- [Indexing Argument Buffers](indexing-argument-buffers.md)
- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)
- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)

#### Overview

A [`MTLBuffer`](mtlbuffer.md) object can be used only with the [`MTLDevice`](mtldevice.md) that created it. Don’t implement this protocol yourself; instead, use the following [`MTLDevice`](mtldevice.md) methods to create `MTLBuffer` objects:

- [`makeBuffer(length:options:)`](mtldevice/makebuffer(length:options:).md) creates a `MTLBuffer` object with a new storage allocation.
- [`makeBuffer(bytes:length:options:)`](mtldevice/makebuffer(bytes:length:options:).md) creates a `MTLBuffer` object by copying data from an existing storage allocation into a new allocation.
- [`makeBuffer(bytesNoCopy:length:options:deallocator:)`](mtldevice/makebuffer(bytesnocopy:length:options:deallocator:).md) creates a `MTLBuffer` object that reuses an existing storage allocation and does not allocate any new storage.

The Metal framework doesn’t know anything about the contents of a [`MTLBuffer`](mtlbuffer.md), just its size. You define the format of the data in the buffer and ensure that your app and your shaders know how to read and write the data. For example, you might create a struct in your shader that defines the data you want to store in the buffer and its memory layout.

If you create a buffer with a managed resource storage mode ([`MTLStorageMode.managed`](mtlstoragemode/managed.md)), you must call [`didModifyRange:`](mtlbuffer/didmodifyrange:.md) to tell Metal to copy any changes to the GPU.

## Topics

### Creating a Texture That Shares Buffer Data
- [func makeTexture(descriptor: MTLTextureDescriptor, offset: Int, bytesPerRow: Int) -> (any MTLTexture)?](mtlbuffer/maketexture(descriptor:offset:bytesperrow:).md)
  Creates a texture that shares its storage with the buffer.
### Reading the Buffer’s Data on the CPU
- [func contents() -> UnsafeMutableRawPointer](mtlbuffer/contents.md)
  Gets the system address of the buffer’s storage allocation.
### Synchronizing Data to the GPU for Managed Buffers
- [func didModifyRange(Range<Int>)](mtlbuffer/didmodifyrange(_:).md)
  Informs the GPU that the CPU has modified a section of the buffer.
### Debugging Buffers
- [func addDebugMarker(String, range: Range<Int>)](mtlbuffer/adddebugmarker(_:range:).md)
  Adds a debug marker string to a specific buffer range.
- [func removeAllDebugMarkers()](mtlbuffer/removealldebugmarkers.md)
  Removes all debug marker strings from the buffer.
### Reading Buffer Length
- [var length: Int](mtlbuffer/length.md)
  The logical size of the buffer, in bytes.
### Creating Views of Buffers on Other GPUs
- [func makeRemoteBufferView(any MTLDevice) -> (any MTLBuffer)?](mtlbuffer/makeremotebufferview(_:).md)
  Creates a remote view of the buffer for another GPU in the same peer group.
- [var remoteStorageBuffer: (any MTLBuffer)?](mtlbuffer/remotestoragebuffer.md)
  The buffer on another GPU that the buffer was created from, if any.
### Instance Properties
- [var gpuAddress: UInt64](mtlbuffer/gpuaddress.md)
- [var sparseBufferTier: MTLBufferSparseTier](mtlbuffer/sparsebuffertier.md)
### Instance Methods
- [func makeTensor(descriptor: MTLTensorDescriptor, offset: Int) throws -> any MTLTensor](mtlbuffer/maketensor(descriptor:offset:).md)
  Creates a tensor that shares storage with this buffer.

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [MTLResource](mtlresource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer)*