# MTLBinaryArchive

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MTLBinaryArchive <NSObject>
```

## Mentions

- [Creating binary archives from device-built pipeline state objects](./creating-binary-archives-from-device-built-pipeline-state-objects.md)

## Topics

### Identifying the archive
- [var device: any MTLDevice](./mtlbinaryarchive/device.md)
  The Metal device object that created the binary archive.
- [var label: String?](./mtlbinaryarchive/label.md)
  A string that identifies the library.
### Adding pipeline descriptors
- [func addComputePipelineFunctions(descriptor: MTLComputePipelineDescriptor) throws](./mtlbinaryarchive/addcomputepipelinefunctions%28descriptor%29.md)
  Adds a description of a compute pipeline to the archive.
- [func addRenderPipelineFunctions(descriptor: MTLRenderPipelineDescriptor) throws](./mtlbinaryarchive/addrenderpipelinefunctions%28descriptor%29.md)
  Adds a description of a render pipeline to the archive.
- [func addTileRenderPipelineFunctions(descriptor: MTLTileRenderPipelineDescriptor) throws](./mtlbinaryarchive/addtilerenderpipelinefunctions%28descriptor%29.md)
  Adds a description of a tile renderer pipeline to the archive.
- [func addFunction(descriptor: MTLFunctionDescriptor, library: any MTLLibrary) throws](./mtlbinaryarchive/addfunction%28descriptor,library%29.md)
  Adds a description of a function to the archive.
### Serializing archives
- [func serialize(to: URL) throws](./mtlbinaryarchive/serialize%28to%29.md)
  Writes the contents of the archive to a file.
### Instance Methods
- [func addLibrary(descriptor: MTLStitchedLibraryDescriptor) throws](./mtlbinaryarchive/addlibrary%28descriptor%29.md)
- [func addMeshRenderPipelineFunctions(descriptor: MTLMeshRenderPipelineDescriptor) throws](./mtlbinaryarchive/addmeshrenderpipelinefunctions%28descriptor%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Shader library management
- [protocol MTLLibrary](./mtllibrary.md)
  A collection of Metal shader functions.
- [protocol MTLDynamicLibrary](./mtldynamiclibrary.md)
  A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [class MTLCompileOptions](./mtlcompileoptions.md)
  Compilation settings for a Metal shader library.
- [enum MTLLibraryType](./mtllibrarytype.md)
  A set of options for Metal library types.
- [enum MTLLanguageVersion](./mtllanguageversion.md)
  Metal shading language versions.
- [enum MTLCompileSymbolVisibility](./mtlcompilesymbolvisibility.md)
- [enum MTLLibraryOptimizationLevel](./mtllibraryoptimizationlevel.md)
  The optimization options for the Metal compiler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchive)*