# addFunction(descriptor:library:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Adds a description of a function to the archive.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func addFunction(descriptor: MTLFunctionDescriptor, library: any MTLLibrary) throws
```

## Parameters

- `descriptor`: 
- `library`: 

## See Also

- [func addComputePipelineFunctions(descriptor: MTLComputePipelineDescriptor) throws](mtlbinaryarchive/addcomputepipelinefunctions(descriptor:).md)
  Adds a description of a compute pipeline to the archive.
- [func addRenderPipelineFunctions(descriptor: MTLRenderPipelineDescriptor) throws](mtlbinaryarchive/addrenderpipelinefunctions(descriptor:).md)
  Adds a description of a render pipeline to the archive.
- [func addTileRenderPipelineFunctions(descriptor: MTLTileRenderPipelineDescriptor) throws](mtlbinaryarchive/addtilerenderpipelinefunctions(descriptor:).md)
  Adds a description of a tile renderer pipeline to the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchive/addfunction(descriptor:library:))*