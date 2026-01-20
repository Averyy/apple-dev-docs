# MPSSVGFDenoiser

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSSVGFDenoiser
```

## Topics

### Initializers
- [init(SVGF: MPSSVGF, textureAllocator: any MPSSVGFTextureAllocator)](mpssvgfdenoiser/init(svgf:textureallocator:).md)
- [init(device: any MTLDevice)](mpssvgfdenoiser/init(device:).md)
### Instance Properties
- [var bilateralFilterIterations: Int](mpssvgfdenoiser/bilateralfilteriterations.md)
- [var svgf: MPSSVGF](mpssvgfdenoiser/svgf.md)
- [var textureAllocator: any MPSSVGFTextureAllocator](mpssvgfdenoiser/textureallocator.md)
### Instance Methods
- [func clearTemporalHistory()](mpssvgfdenoiser/cleartemporalhistory.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: AutoreleasingUnsafeMutablePointer<any MTLTexture>, sourceTexture2: (any MTLTexture)?, destinationTexture2: AutoreleasingUnsafeMutablePointer<any MTLTexture>?, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?)](mpssvgfdenoiser/encode(commandbuffer:sourcetexture:destinationtexture:sourcetexture2:destinationtexture2:motionvectortexture:depthnormaltexture:previousdepthnormaltexture:).md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?) -> any MTLTexture](mpssvgfdenoiser/encode(commandbuffer:sourcetexture:motionvectortexture:depthnormaltexture:previousdepthnormaltexture:).md)
- [func releaseTemporaryTextures()](mpssvgfdenoiser/releasetemporarytextures.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdenoiser)*