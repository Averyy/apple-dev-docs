# addRenderPipelineFunctions(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Adds a description of a render pipeline to the archive.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func addRenderPipelineFunctions(descriptor: MTLRenderPipelineDescriptor) throws
```

## Parameters

- `descriptor`: A description of the render pipeline to archive.

## See Also

- [func addComputePipelineFunctions(descriptor: MTLComputePipelineDescriptor) throws](mtlbinaryarchive/addcomputepipelinefunctions(descriptor:).md)
  Adds a description of a compute pipeline to the archive.
- [func addTileRenderPipelineFunctions(descriptor: MTLTileRenderPipelineDescriptor) throws](mtlbinaryarchive/addtilerenderpipelinefunctions(descriptor:).md)
  Adds a description of a tile renderer pipeline to the archive.
- [func addFunction(descriptor: MTLFunctionDescriptor, library: any MTLLibrary) throws](mtlbinaryarchive/addfunction(descriptor:library:).md)
  Adds a description of a function to the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchive/addrenderpipelinefunctions(descriptor:))*