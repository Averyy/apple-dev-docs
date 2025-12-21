# Device inspection

**Framework**: Metal

Locate and identify a GPU and the features it supports, and sample its counters.

## Topics

### Checking a GPU device’s feature support
- [func supportsFamily(MTLGPUFamily) -> Bool](mtldevice/supportsfamily(_:).md)
  Returns a Boolean value that indicates whether the GPU device supports the feature set of a specific GPU family.
- [enum MTLGPUFamily](mtlgpufamily.md)
  Represents the functionality for families of GPUs.
- [func supportsFeatureSet(MTLFeatureSet) -> Bool](mtldevice/supportsfeatureset(_:).md)
  Returns a Boolean value that indicates whether the GPU device supports a specific feature set.
- [enum MTLFeatureSet](mtlfeatureset.md)
  The device feature sets that define specific platform, hardware, and software configurations.
### Checking compute support
- [var maxThreadgroupMemoryLength: Int](mtldevice/maxthreadgroupmemorylength.md)
  The maximum threadgroup memory available to a compute kernel, in bytes.
- [var maxThreadsPerThreadgroup: MTLSize](mtldevice/maxthreadsperthreadgroup.md)
  The maximum number of threads along each dimension of a threadgroup.
### Checking render support
- [var supportsRaytracing: Bool](mtldevice/supportsraytracing.md)
  A Boolean value that indicates whether the GPU device supports ray tracing.
- [var supportsPrimitiveMotionBlur: Bool](mtldevice/supportsprimitivemotionblur.md)
  A Boolean value that indicates whether the GPU device supports motion blur for ray tracing.
- [var supportsRaytracingFromRender: Bool](mtldevice/supportsraytracingfromrender.md)
  A Boolean value that indicates whether you can call ray-tracing functions from a vertex or fragment shader.
- [var supports32BitMSAA: Bool](mtldevice/supports32bitmsaa.md)
  A Boolean value that indicates whether the GPU can allocate 32-bit integer texture formats and resolve to 32-bit floating-point texture formats.
- [var supportsPullModelInterpolation: Bool](mtldevice/supportspullmodelinterpolation.md)
  A Boolean value that indicates whether the GPU can compute multiple interpolations of a fragment function’s input.
- [var supportsShaderBarycentricCoordinates: Bool](mtldevice/supportsshaderbarycentriccoordinates.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.
- [func supportsVertexAmplificationCount(Int) -> Bool](mtldevice/supportsvertexamplificationcount(_:).md)
  Returns a Boolean value that indicates whether the GPU supports an amplification factor.
- [var areProgrammableSamplePositionsSupported: Bool](mtldevice/areprogrammablesamplepositionssupported.md)
  A Boolean value that indicates whether the GPU supports programmable sample positions.
- [var areRasterOrderGroupsSupported: Bool](mtldevice/arerasterordergroupssupported.md)
  A Boolean value that indicates whether the GPU supports raster order groups.
- [var areBarycentricCoordsSupported: Bool](mtldevice/arebarycentriccoordssupported.md)
  A Boolean value that indicates whether the GPU supports barycentric coordinates.
### Checking texture and sampler support
- [var supports32BitFloatFiltering: Bool](mtldevice/supports32bitfloatfiltering.md)
  A Boolean value that indicates whether the GPU can filter a texture with a 32-bit floating-point format.
- [var supportsBCTextureCompression: Bool](mtldevice/supportsbctexturecompression.md)
  A Boolean value that indicates whether you can use textures that use BC compression.
- [var isDepth24Stencil8PixelFormatSupported: Bool](mtldevice/isdepth24stencil8pixelformatsupported.md)
  A Boolean value that indicates whether a device supports a packed depth-and-stencil pixel format.
- [var supportsQueryTextureLOD: Bool](mtldevice/supportsquerytexturelod.md)
  A Boolean value that indicates whether you can query the texture level of detail from within a shader.
- [var readWriteTextureSupport: MTLReadWriteTextureTier](mtldevice/readwritetexturesupport.md)
  The GPU device’s texture support tier.
### Checking function pointer support
- [var supportsFunctionPointers: Bool](mtldevice/supportsfunctionpointers.md)
  A Boolean value that indicates whether the device supports function pointers in compute kernel functions.
- [var supportsFunctionPointersFromRender: Bool](mtldevice/supportsfunctionpointersfromrender.md)
  A Boolean value that indicates whether the device supports function pointers in render functions.
### Checking a GPU device’s memory
- [var currentAllocatedSize: Int](mtldevice/currentallocatedsize.md)
  The total amount of memory, in bytes, the GPU device is using for all of its resources.
- [var recommendedMaxWorkingSetSize: UInt64](mtldevice/recommendedmaxworkingsetsize.md)
  An approximation of how much memory, in bytes, this GPU device can allocate without affecting its runtime performance.
- [var hasUnifiedMemory: Bool](mtldevice/hasunifiedmemory.md)
  A Boolean value that indicates whether the GPU shares all of its memory with the CPU.
- [var maxTransferRate: UInt64](mtldevice/maxtransferrate.md)
  The highest theoretical rate, in bytes per second, the system can copy between system memory and the GPU’s dedicated memory (VRAM).
### Sampling a GPU device’s counters
- [var counterSets: [any MTLCounterSet]?](mtldevice/countersets.md)
  The counter sets supported by the device object.
- [func supportsCounterSampling(MTLCounterSamplingPoint) -> Bool](mtldevice/supportscountersampling(_:).md)
  Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [enum MTLCounterSamplingPoint](mtlcountersamplingpoint.md)
  Options for different times when you can sample GPU counters.
- [func makeCounterSampleBuffer(descriptor: MTLCounterSampleBufferDescriptor) throws -> any MTLCounterSampleBuffer](mtldevice/makecountersamplebuffer(descriptor:).md)
  Creates a counter sample buffer.
### Sampling GPU and CPU timestamps simultaneously
- [func sampleTimestamps() -> (cpu: MTLTimestamp, gpu: MTLTimestamp)](mtldevice/sampletimestamps.md)
  Captures and returns a CPU timestamp and a GPU timestamp from the same moment in time.
### Identifying a GPU device
- [var name: String](mtldevice/name.md)
  The full name of the GPU device.
- [var architecture: MTLArchitecture](mtldevice/architecture.md)
  The architectural details of the GPU device.
- [class MTLArchitecture](mtlarchitecture.md)
  A class that contains the architectural details of a GPU device.
- [var registryID: UInt64](mtldevice/registryid.md)
  The GPU device’s registry identifier.
- [var location: MTLDeviceLocation](mtldevice/location.md)
  The physical location of the GPU relative to the system.
- [enum MTLDeviceLocation](mtldevicelocation.md)
  Indicates the location of the GPU relative to the system it’s connect to.
- [var locationNumber: Int](mtldevice/locationnumber.md)
  A specific GPU position based on its general location.
- [var isLowPower: Bool](mtldevice/islowpower.md)
  A Boolean value that indicates whether the GPU lowers its performance to conserve energy.
- [var isRemovable: Bool](mtldevice/isremovable.md)
  A Boolean value that indicates whether the GPU is removable.
- [var isHeadless: Bool](mtldevice/isheadless.md)
  A Boolean value that indicates whether a GPU device doesn’t have a connection to a display.
- [var peerGroupID: UInt64](mtldevice/peergroupid.md)
  The peer group ID the GPU belongs to, if applicable.
- [var peerCount: UInt32](mtldevice/peercount.md)
  The total number of GPUs in the peer group, if applicable.
- [var peerIndex: UInt32](mtldevice/peerindex.md)
  The unique identifier for a GPU in a peer group.

## See Also

- [Work submission](work-submission.md)
  Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Pipeline state creation](pipeline-state-creation.md)
  Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Resource creation](resource-creation.md)
  Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
- [Shader library and archive creation](shader-library-and-archive-creation.md)
  Create static and dynamic shader libraries, and binary shader archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/device-inspection)*