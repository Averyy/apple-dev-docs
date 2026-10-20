# MPSImageGuidedFilter

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSImageGuidedFilter : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsimageguidedfilter/init%28coder,device%29.md)
- [init(device: any MTLDevice, kernelDiameter: Int)](./mpsimageguidedfilter/init%28device,kerneldiameter%29.md)
### Instance Properties
- [var epsilon: Float](./mpsimageguidedfilter/epsilon.md)
- [var kernelDiameter: Int](./mpsimageguidedfilter/kerneldiameter.md)
- [var reconstructOffset: Float](./mpsimageguidedfilter/reconstructoffset.md)
- [var reconstructScale: Float](./mpsimageguidedfilter/reconstructscale.md)
### Instance Methods
- [func encodeReconstruction(commandBuffer: any MTLCommandBuffer, guidance: any MTLTexture, coefficientsA: any MTLTexture, coefficientsB: any MTLTexture, destination: any MTLTexture)](./mpsimageguidedfilter/encodereconstruction%28commandbuffer,guidance,coefficientsa,coefficientsb,destination%29.md)
- [func encodeReconstruction(to: any MTLCommandBuffer, guidanceTexture: any MTLTexture, coefficientsTexture: any MTLTexture, destinationTexture: any MTLTexture)](./mpsimageguidedfilter/encodereconstruction%28to,guidancetexture,coefficientstexture,destinationtexture%29.md)
- [func encodeRegression(commandBuffer: any MTLCommandBuffer, source: any MTLTexture, guidance: any MTLTexture, weights: (any MTLTexture)?, destinationCoefficientsA: any MTLTexture, destinationCoefficientsB: any MTLTexture)](./mpsimageguidedfilter/encoderegression%28commandbuffer,source,guidance,weights,destinationcoefficientsa,destinationcoefficientsb%29.md)
- [func encodeRegression(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, guidanceTexture: any MTLTexture, weightsTexture: (any MTLTexture)?, destinationCoefficientsTexture: any MTLTexture)](./mpsimageguidedfilter/encoderegression%28to,sourcetexture,guidancetexture,weightstexture,destinationcoefficientstexture%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageguidedfilter)*