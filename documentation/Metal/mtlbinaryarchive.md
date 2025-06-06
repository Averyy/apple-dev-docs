# MTLBinaryArchive

**Framework**: Metal  
**Kind**: protocol

A container for pipeline state descriptors and their associated compiled shader code.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLBinaryArchive : NSObjectProtocol
```

## Mentions

- [Creating Binary Archives from Device-Built Pipeline State Objects](creating-binary-archives-from-device-built-pipeline-state-objects.md)

## Topics

### Identifying the Archive
- [var device: any MTLDevice](mtlbinaryarchive/device.md)
  The Metal device object that created the binary archive.
- [var label: String?](mtlbinaryarchive/label.md)
  A string that identifies the library.
### Adding Pipeline Descriptors
- [func addComputePipelineFunctions(descriptor: MTLComputePipelineDescriptor) throws](mtlbinaryarchive/addcomputepipelinefunctions(descriptor:).md)
  Adds a description of a compute pipeline to the archive.
- [func addRenderPipelineFunctions(descriptor: MTLRenderPipelineDescriptor) throws](mtlbinaryarchive/addrenderpipelinefunctions(descriptor:).md)
  Adds a description of a render pipeline to the archive.
- [func addTileRenderPipelineFunctions(descriptor: MTLTileRenderPipelineDescriptor) throws](mtlbinaryarchive/addtilerenderpipelinefunctions(descriptor:).md)
  Adds a description of a tile renderer pipeline to the archive.
- [func addFunction(descriptor: MTLFunctionDescriptor, library: any MTLLibrary) throws](mtlbinaryarchive/addfunction(descriptor:library:).md)
  Adds a description of a function to the archive.
### Serializing Archives
- [func serialize(to: URL) throws](mtlbinaryarchive/serialize(to:).md)
  Writes the contents of the archive to a file.
### Instance Methods
- [func addLibrary(descriptor: MTLStitchedLibraryDescriptor) throws](mtlbinaryarchive/addlibrary(descriptor:).md)
- [func addMeshRenderPipelineFunctions(descriptor: MTLMeshRenderPipelineDescriptor) throws](mtlbinaryarchive/addmeshrenderpipelinefunctions(descriptor:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLLibrary](mtllibrary.md)
  A collection of Metal shader functions.
- [protocol MTLDynamicLibrary](mtldynamiclibrary.md)
  A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [class MTLCompileOptions](mtlcompileoptions.md)
  Compilation settings for a Metal shader library.
- [enum MTLLibraryType](mtllibrarytype.md)
  A set of options for Metal library types.
- [enum MTLLanguageVersion](mtllanguageversion.md)
  Metal shading language versions.
- [enum MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [enum MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md)
  The optimization options for the Metal compiler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchive)*