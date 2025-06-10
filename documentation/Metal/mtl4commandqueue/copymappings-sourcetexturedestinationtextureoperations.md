# copyMappings(sourceTexture:destinationTexture:operations:)

**Framework**: Metal  
**Kind**: method

Copies multiple regions within a source placement sparse texture to a destination placement sparse texture.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func copyMappings(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, operations: [MTL4CopySparseTextureMappingOperation])
```

#### Discussion

You are responsible for ensuring the source and destination textures have the same [`placementSparsePageSize`](mtltexturedescriptor/placementsparsepagesize.md).

Additionally, you are responsible for ensuring that the source and destination textures don’t use the same aliased tiles at the same time.

> **Note**: If a sparse texture and a sparse buffer share the same backing tiles, these don’t provide you you with meaningful views of the other resource’s data.

## Parameters

- `sourceTexture`: The source placement sparse  .
- `destinationTexture`: The destination placement sparse  .
- `operations`: An array of   instances to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/copymappings(sourcetexture:destinationtexture:operations:))*