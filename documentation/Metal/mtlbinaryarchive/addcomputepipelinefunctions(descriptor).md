# addComputePipelineFunctions(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds a description of a compute pipeline to the archive.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func addComputePipelineFunctions(descriptor: MTLComputePipelineDescriptor) throws
```

```objc
- (BOOL) addComputePipelineFunctionsWithDescriptor:(MTLComputePipelineDescriptor *) descriptor error:(NSError **) error;
```

## Parameters

- `descriptor`: A description of the compute pipeline to archive.

## See Also

### Adding pipeline descriptors
- [func addRenderPipelineFunctions(descriptor: MTLRenderPipelineDescriptor) throws](./addrenderpipelinefunctions%28descriptor%29.md)
  Adds a description of a render pipeline to the archive.
- [func addTileRenderPipelineFunctions(descriptor: MTLTileRenderPipelineDescriptor) throws](./addtilerenderpipelinefunctions%28descriptor%29.md)
  Adds a description of a tile renderer pipeline to the archive.
- [func addFunction(descriptor: MTLFunctionDescriptor, library: any MTLLibrary) throws](./addfunction%28descriptor,library%29.md)
  Adds a description of a function to the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchive/addcomputepipelinefunctions(descriptor:))*