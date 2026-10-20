# MPSImageEDLines

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 13.4+
- visionOS 1.0+

## Declaration

```swift
class MPSImageEDLines
```

```objc
@interface MPSImageEDLines : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsimageedlines/init%28coder,device%29.md)
- [init(device: any MTLDevice, gaussianSigma: Float, minLineLength: UInt16, maxLines: Int, detailRatio: UInt16, gradientThreshold: Float, lineErrorThreshold: Float, mergeLocalityThreshold: Float)](./mpsimageedlines/init%28device,gaussiansigma,minlinelength,maxlines,detailratio,gradientthreshold,lineerrorthreshold,mergelocalitythreshold%29.md)
### Instance Properties
- [var clipRectSource: MTLRegion](./mpsimageedlines/cliprectsource.md)
- [var detailRatio: UInt16](./mpsimageedlines/detailratio.md)
- [var gaussianSigma: Float](./mpsimageedlines/gaussiansigma.md)
- [var gradientThreshold: Float](./mpsimageedlines/gradientthreshold.md)
- [var lineErrorThreshold: Float](./mpsimageedlines/lineerrorthreshold.md)
- [var maxLines: Int](./mpsimageedlines/maxlines.md)
- [var mergeLocalityThreshold: Float](./mpsimageedlines/mergelocalitythreshold.md)
- [var minLineLength: UInt16](./mpsimageedlines/minlinelength.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: (any MTLTexture)?, endpointBuffer: any MTLBuffer, endpointOffset: Int)](./mpsimageedlines/encode%28to,sourcetexture,destinationtexture,endpointbuffer,endpointoffset%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedlines)*