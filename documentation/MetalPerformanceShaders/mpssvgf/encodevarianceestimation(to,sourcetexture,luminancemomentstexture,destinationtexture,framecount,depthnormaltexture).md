# encodeVarianceEstimation(to:sourceTexture:luminanceMomentsTexture:destinationTexture:frameCount:depthNormalTexture:)

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
func encodeVarianceEstimation(to commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, luminanceMomentsTexture: any MTLTexture, destinationTexture: any MTLTexture, frameCount frameCountTexture: any MTLTexture, depthNormalTexture: (any MTLTexture)?)
```

```objc
- (void) encodeVarianceEstimationToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceTexture:(id<MTLTexture>) sourceTexture luminanceMomentsTexture:(id<MTLTexture>) luminanceMomentsTexture destinationTexture:(id<MTLTexture>) destinationTexture frameCountTexture:(id<MTLTexture>) frameCountTexture depthNormalTexture:(id<MTLTexture>) depthNormalTexture;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf/encodevarianceestimation(to:sourcetexture:luminancemomentstexture:destinationtexture:framecount:depthnormaltexture:))*