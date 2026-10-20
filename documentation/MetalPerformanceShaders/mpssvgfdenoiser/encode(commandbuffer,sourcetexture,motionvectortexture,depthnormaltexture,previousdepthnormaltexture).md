# encode(commandBuffer:sourceTexture:motionVectorTexture:depthNormalTexture:previousDepthNormalTexture:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encode(commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: any MTLTexture, previousDepthNormalTexture: (any MTLTexture)?) -> any MTLTexture
```

```objc
- (id<MTLTexture>) encodeToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) sourceTexture motionVectorTexture:(id<MTLTexture>) motionVectorTexture depthNormalTexture:(id<MTLTexture>) depthNormalTexture previousDepthNormalTexture:(id<MTLTexture>) previousDepthNormalTexture;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgfdenoiser/encode(commandbuffer:sourcetexture:motionvectortexture:depthnormaltexture:previousdepthnormaltexture:))*