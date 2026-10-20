# MPSSVGF

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
class MPSSVGF
```

```objc
@interface MPSSVGF : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpssvgf/init%28coder,device%29.md)
- [init(device: any MTLDevice)](./mpssvgf/init%28device%29.md)
### Instance Properties
- [var bilateralFilterRadius: Int](./mpssvgf/bilateralfilterradius.md)
- [var bilateralFilterSigma: Float](./mpssvgf/bilateralfiltersigma.md)
- [var channelCount: Int](./mpssvgf/channelcount.md)
- [var channelCount2: Int](./mpssvgf/channelcount2.md)
- [var depthWeight: Float](./mpssvgf/depthweight.md)
- [var luminanceWeight: Float](./mpssvgf/luminanceweight.md)
- [var minimumFramesForVarianceEstimation: Int](./mpssvgf/minimumframesforvarianceestimation.md)
- [var normalWeight: Float](./mpssvgf/normalweight.md)
- [var reprojectionThreshold: Float](./mpssvgf/reprojectionthreshold.md)
- [var temporalReprojectionBlendFactor: Float](./mpssvgf/temporalreprojectionblendfactor.md)
- [var temporalWeighting: MPSTemporalWeighting](./mpssvgf/temporalweighting.md)
- [var varianceEstimationRadius: Int](./mpssvgf/varianceestimationradius.md)
- [var varianceEstimationSigma: Float](./mpssvgf/varianceestimationsigma.md)
- [var variancePrefilterRadius: Int](./mpssvgf/varianceprefilterradius.md)
- [var variancePrefilterSigma: Float](./mpssvgf/varianceprefiltersigma.md)
### Instance Methods
- [func copy(with: NSZone?, device: (any MTLDevice)?) -> Self](./mpssvgf/copy%28with,device%29.md)
- [func encode(with: NSCoder)](./mpssvgf/encode%28with%29.md)
- [func encodeBilateralFilter(to: any MTLCommandBuffer, stepDistance: Int, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, depthNormalTexture: any MTLTexture)](./mpssvgf/encodebilateralfilter%28to,stepdistance,sourcetexture,destinationtexture,depthnormaltexture%29.md)
- [func encodeBilateralFilter(to: any MTLCommandBuffer, stepDistance: Int, sourceTexture: any MTLTexture, destinationTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, depthNormalTexture: any MTLTexture)](./mpssvgf/encodebilateralfilter%28to,stepdistance,sourcetexture,destinationtexture,sourcetexture2,destinationtexture2,depthnormaltexture%29.md)
- [func encodeReprojection(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, previousLuminanceMomentsTexture: any MTLTexture, destinationLuminanceMomentsTexture: any MTLTexture, previousFrameCount: any MTLTexture, destinationFrameCount: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: (any MTLTexture)?, previousDepthNormalTexture: (any MTLTexture)?)](./mpssvgf/encodereprojection%28to_sourcetexture_previoustexture_destinationtexture_previousluminancemomentstexture_destinationluminancemomentstexture_previousframecount_destinationframecount_motionvectortexture_depthnormaltexture_-b41497b8.md)
- [func encodeReprojection(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, previousTexture: any MTLTexture, destinationTexture: any MTLTexture, previousLuminanceMomentsTexture: any MTLTexture, destinationLuminanceMomentsTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, previousTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, previousLuminanceMomentsTexture2: (any MTLTexture)?, destinationLuminanceMomentsTexture2: (any MTLTexture)?, previousFrameCount: any MTLTexture, destinationFrameCount: any MTLTexture, motionVectorTexture: (any MTLTexture)?, depthNormalTexture: (any MTLTexture)?, previousDepthNormalTexture: (any MTLTexture)?)](./mpssvgf/encodereprojection%28to_sourcetexture_previoustexture_destinationtexture_previousluminancemomentstexture_destinationluminancemomentstexture_sourcetexture2_previoustexture2_destinationtexture2_previousluminancemomentstext-a9ee93bd.md)
- [func encodeVarianceEstimation(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, luminanceMomentsTexture: any MTLTexture, destinationTexture: any MTLTexture, frameCount: any MTLTexture, depthNormalTexture: (any MTLTexture)?)](./mpssvgf/encodevarianceestimation%28to,sourcetexture,luminancemomentstexture,destinationtexture,framecount,depthnormaltexture%29.md)
- [func encodeVarianceEstimation(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, luminanceMomentsTexture: any MTLTexture, destinationTexture: any MTLTexture, sourceTexture2: (any MTLTexture)?, luminanceMomentsTexture2: (any MTLTexture)?, destinationTexture2: (any MTLTexture)?, frameCount: any MTLTexture, depthNormalTexture: (any MTLTexture)?)](./mpssvgf/encodevarianceestimation%28to,sourcetexture,luminancemomentstexture,destinationtexture,sourcetexture2,luminancemomentstexture2,destinationtexture2,framecount,depthnormaltexture%29.md)

## Relationships

### Inherits From
- [MPSKernel](./mpskernel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssvgf)*