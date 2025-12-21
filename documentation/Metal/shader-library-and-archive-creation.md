# Shader library and archive creation

**Framework**: Metal

Create static and dynamic shader libraries, and binary shader archives.

## Topics

### Creating shader libraries
- [func makeDefaultLibrary() -> (any MTLLibrary)?](mtldevice/makedefaultlibrary.md)
  Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [func makeDefaultLibrary(bundle: Bundle) throws -> any MTLLibrary](mtldevice/makedefaultlibrary(bundle:).md)
  Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [func makeLibrary(URL: URL) throws -> any MTLLibrary](mtldevice/makelibrary(url:).md)
  Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [func makeLibrary(source: String, options: MTLCompileOptions?) throws -> any MTLLibrary](mtldevice/makelibrary(source:options:).md)
  Synchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(source: String, options: MTLCompileOptions?, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](mtldevice/makelibrary(source:options:completionhandler:).md)
  Asynchronously creates a Metal library instance by compiling the functions in a source string.
- [func makeLibrary(stitchedDescriptor: MTLStitchedLibraryDescriptor) throws -> any MTLLibrary](mtldevice/makelibrary(stitcheddescriptor:).md)
  Synchronously creates a Metal library from the function stitching graphs in a descriptor.
- [func makeLibrary(stitchedDescriptor: MTLStitchedLibraryDescriptor, completionHandler: ((any MTLLibrary)?, (any Error)?) -> Void)](mtldevice/makelibrary(stitcheddescriptor:completionhandler:).md)
  Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [func makeLibrary(data: DispatchData) throws -> any MTLLibrary](mtldevice/makelibrary(data:)-7khmh.md)
  Creates a Metal library instance that contains the functions in a precompiled Metal library.
- [func makeLibrary(data: dispatch_data_t) throws -> any MTLLibrary](mtldevice/makelibrary(data:).md)
  Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [typealias MTLNewLibraryCompletionHandler](mtlnewlibrarycompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a Metal library.
- [func makeLibrary(filepath: String) throws -> any MTLLibrary](mtldevice/makelibrary(filepath:).md)
  Creates a Metal library instance that contains the functions in the Metal library file at a file path.
### Creating dynamic shader libraries
- [var supportsDynamicLibraries: Bool](mtldevice/supportsdynamiclibraries.md)
  A Boolean value that indicates whether the GPU device can create and use dynamic libraries in compute pipelines.
- [var supportsRenderDynamicLibraries: Bool](mtldevice/supportsrenderdynamiclibraries.md)
  A Boolean value that indicates whether the GPU device can create and use dynamic libraries in render pipelines.
- [func makeDynamicLibrary(library: any MTLLibrary) throws -> any MTLDynamicLibrary](mtldevice/makedynamiclibrary(library:).md)
  Creates a Metal dynamic library instance from a Metal library instance.
- [func makeDynamicLibrary(url: URL) throws -> any MTLDynamicLibrary](mtldevice/makedynamiclibrary(url:).md)
  Creates a Metal dynamic library instance that contains the functions in the Metal library file at a URL.
- [MTLDynamicLibraryError.Code](mtldynamiclibraryerror-swift.struct/code.md)
  Error codes that Metal can generate when creating dynamic libraries.
- [let MTLDynamicLibraryDomain: String](mtldynamiclibrarydomain.md)
  The domain for Metal dynamic library errors.
### Creating binary shader archives
- [func makeBinaryArchive(descriptor: MTLBinaryArchiveDescriptor) throws -> any MTLBinaryArchive](mtldevice/makebinaryarchive(descriptor:).md)
  Creates a Metal binary archive instance.
- [class MTLBinaryArchiveDescriptor](mtlbinaryarchivedescriptor.md)
  A description of a binary shader archive that you want to create.
- [MTLBinaryArchiveError.Code](mtlbinaryarchiveerror-swift.struct/code.md)
  Error codes when creating binary archives of compiled shader code.
- [let MTLBinaryArchiveDomain: String](mtlbinaryarchivedomain.md)
  The domain for Metal binary archive errors.

## See Also

- [Device inspection](device-inspection.md)
  Locate and identify a GPU and the features it supports, and sample its counters.
- [Work submission](work-submission.md)
  Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Pipeline state creation](pipeline-state-creation.md)
  Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Resource creation](resource-creation.md)
  Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/shader-library-and-archive-creation)*