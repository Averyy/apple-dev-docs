# addFunction(descriptor:library:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (BOOL) addFunctionWithDescriptor:(MTLFunctionDescriptor *) descriptor library:(id<MTLLibrary>) library error:(NSError **) error;
```

## Parameters

- `descriptor`: 
- `library`: 

## See Also

### Adding pipeline descriptors
- [func addComputePipelineFunctions(descriptor: MTLComputePipelineDescriptor) throws](./addcomputepipelinefunctions%28descriptor%29.md)
  Adds a description of a compute pipeline to the archive.
- [func addRenderPipelineFunctions(descriptor: MTLRenderPipelineDescriptor) throws](./addrenderpipelinefunctions%28descriptor%29.md)
  Adds a description of a render pipeline to the archive.
- [func addTileRenderPipelineFunctions(descriptor: MTLTileRenderPipelineDescriptor) throws](./addtilerenderpipelinefunctions%28descriptor%29.md)
  Adds a description of a tile renderer pipeline to the archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbinaryarchive/addfunction(descriptor:library:))*