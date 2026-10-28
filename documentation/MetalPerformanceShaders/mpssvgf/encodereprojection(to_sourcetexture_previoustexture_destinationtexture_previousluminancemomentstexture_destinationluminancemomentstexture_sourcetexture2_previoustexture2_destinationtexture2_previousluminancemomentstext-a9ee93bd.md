# encodeReprojection(to:sourceTexture:previousTexture:destinationTexture:previousLuminanceMomentsTexture:destinationLuminanceMomentsTexture:sourceTexture2:previousTexture2:destinationTexture2:previousLuminanceMomentsTexture2:destinationLuminanceMomentsTexture2:previousFrameCount:destinationFrameCount:motionVectorTexture:depthNormalTexture:previousDepthNormalTexture:)

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
func encodeReprojection(to commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, previousLuminanceMomentsTexture: any MTLTexture, destinationLuminanceMomentsTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, previousTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, previousLuminanceMomentsTexture2: (any MTLTexture)?, destinationLuminanceMomentsTexture2: (any MTLTexture)?, previousFrameCount previousFrameCountTexture: any MTLTexture, destinationFrameCount destinationFrameCountTexture: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: (any MTLTexture)?, previousDepthNormalTexture: (any MTLTexture)?)
```

```objc
- (void) encodeReprojectionToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) sourceTexture previousTexture:(id<MTLTexture>) previousTexture destinationTexture:(id<MTLTexture>) destinationTexture previousLuminanceMomentsTexture:(id<MTLTexture>) previousLuminanceMomentsTexture destinationLuminanceMomentsTexture:(id<MTLTexture>) destinationLuminanceMomentsTexture sourceTexture2:(id<MTLTexture>) sourceTexture2 previousTexture2:(id<MTLTexture>) previousTexture2 destinationTexture2:(id<MTLTexture>) destinationTexture2 previousLuminanceMomentsTexture2:(id<MTLTexture>) previousLuminanceMomentsTexture2 destinationLuminanceMomentsTexture2:(id<MTLTexture>) destinationLuminanceMomentsTexture2 previousFrameCountTexture:(id<MTLTexture>) previousFrameCountTexture destinationFrameCountTexture:(id<MTLTexture>) destinationFrameCountTexture motionVectorTexture:(id<MTLTexture>) motionVectorTexture depthNormalTexture:(id<MTLTexture>) depthNormalTexture previousDepthNormalTexture:(id<MTLTexture>) previousDepthNormalTexture;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf/encodereprojection%28to:sourcetexture:previoustexture:destinationtexture:previousluminancemomentstexture:destinationluminancemomentstexture:sourcetexture2:previoustexture2:destinationtexture2:previousluminancemomentstexture2:destinationlumina-5nbfn)*