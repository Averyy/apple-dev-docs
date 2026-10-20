# MPSSVGFDenoiser

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSSVGFDenoiser : NSObject
```

## Topics

### Initializers
- [init(SVGF: MPSSVGF, textureAllocator: any MPSSVGFTextureAllocator)](./mpssvgfdenoiser/init%28svgf,textureallocator%29.md)
- [init(device: any MTLDevice)](./mpssvgfdenoiser/init%28device%29.md)
### Instance Properties
- [var bilateralFilterIterations: Int](./mpssvgfdenoiser/bilateralfilteriterations.md)
- [var svgf: MPSSVGF](./mpssvgfdenoiser/svgf.md)
- [var textureAllocator: any MPSSVGFTextureAllocator](./mpssvgfdenoiser/textureallocator.md)
### Instance Methods
- [func clearTemporalHistory()](./mpssvgfdenoiser/cleartemporalhistory%28%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: AutoreleasingUnsafeMutablePointer<any MTLTexture>, sourceTexture2: (any MTLTexture)?, destinationTexture2: AutoreleasingUnsafeMutablePointer<any MTLTexture>?, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?)](./mpssvgfdenoiser/encode%28commandbuffer,sourcetexture,destinationtexture,sourcetexture2,destinationtexture2,motionvectortexture,depthnormaltexture,previousdepthnormaltexture%29.md)
- [func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?) -> any MTLTexture](./mpssvgfdenoiser/encode%28commandbuffer,sourcetexture,motionvectortexture,depthnormaltexture,previousdepthnormaltexture%29.md)
- [func releaseTemporaryTextures()](./mpssvgfdenoiser/releasetemporarytextures%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdenoiser)*