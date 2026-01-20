# encodeVarianceEstimation(to:sourceTexture:luminanceMomentsTexture:destinationTexture:sourceTexture2:luminanceMomentsTexture2:destinationTexture2:frameCount:depthNormalTexture:)

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encodeVarianceEstimation(to commandBuffer: any MTLCommandBuffer, sourceTexture: any MTLTexture, luminanceMomentsTexture: any MTLTexture, destinationTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, luminanceMomentsTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, frameCount frameCountTexture: any MTLTexture, depthNormalTexture: (any MTLTexture)?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf/encodevarianceestimation(to:sourcetexture:luminancemomentstexture:destinationtexture:sourcetexture2:luminancemomentstexture2:destinationtexture2:framecount:depthnormaltexture:))*