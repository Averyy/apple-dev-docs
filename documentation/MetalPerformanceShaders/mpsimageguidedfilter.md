# MPSImageGuidedFilter

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that performs edge-aware filtering on an image.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSImageGuidedFilter
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageguidedfilter/init(coder:device:).md)
- [init(device: any MTLDevice, kernelDiameter: Int)](mpsimageguidedfilter/init(device:kerneldiameter:).md)
### Instance Properties
- [var epsilon: Float](mpsimageguidedfilter/epsilon.md)
- [var kernelDiameter: Int](mpsimageguidedfilter/kerneldiameter.md)
- [var reconstructOffset: Float](mpsimageguidedfilter/reconstructoffset.md)
- [var reconstructScale: Float](mpsimageguidedfilter/reconstructscale.md)
### Instance Methods
- [func encodeReconstruction(commandBuffer: any MTLCommandBuffer, guidance: any MTLTexture, coefficientsA: any MTLTexture, coefficientsB: any MTLTexture, destination: any MTLTexture)](mpsimageguidedfilter/encodereconstruction(commandbuffer:guidance:coefficientsa:coefficientsb:destination:).md)
- [func encodeReconstruction(to: any MTLCommandBuffer, guidanceTexture: any MTLTexture, coefficientsTexture: any MTLTexture, destinationTexture: any MTLTexture)](mpsimageguidedfilter/encodereconstruction(to:guidancetexture:coefficientstexture:destinationtexture:).md)
- [func encodeRegression(commandBuffer: any MTLCommandBuffer, source: any MTLTexture, guidance: any MTLTexture, weights: (any MTLTexture)?, destinationCoefficientsA: any MTLTexture, destinationCoefficientsB: any MTLTexture)](mpsimageguidedfilter/encoderegression(commandbuffer:source:guidance:weights:destinationcoefficientsa:destinationcoefficientsb:).md)
- [func encodeRegression(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, guidanceTexture: any MTLTexture, weightsTexture: (any MTLTexture)?, destinationCoefficientsTexture: any MTLTexture)](mpsimageguidedfilter/encoderegression(to:sourcetexture:guidancetexture:weightstexture:destinationcoefficientstexture:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageguidedfilter)*