# MPSImageEDLines

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimageedlines/init(coder:device:).md)
- [init(device: any MTLDevice, gaussianSigma: Float, minLineLength: UInt16, maxLines: Int, detailRatio: UInt16, gradientThreshold: Float, lineErrorThreshold: Float, mergeLocalityThreshold: Float)](mpsimageedlines/init(device:gaussiansigma:minlinelength:maxlines:detailratio:gradientthreshold:lineerrorthreshold:mergelocalitythreshold:).md)
### Instance Properties
- [var clipRectSource: MTLRegion](mpsimageedlines/cliprectsource.md)
- [var detailRatio: UInt16](mpsimageedlines/detailratio.md)
- [var gaussianSigma: Float](mpsimageedlines/gaussiansigma.md)
- [var gradientThreshold: Float](mpsimageedlines/gradientthreshold.md)
- [var lineErrorThreshold: Float](mpsimageedlines/lineerrorthreshold.md)
- [var maxLines: Int](mpsimageedlines/maxlines.md)
- [var mergeLocalityThreshold: Float](mpsimageedlines/mergelocalitythreshold.md)
- [var minLineLength: UInt16](mpsimageedlines/minlinelength.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, destinationTexture: (any MTLTexture)?, endpointBuffer: any MTLBuffer, endpointOffset: Int)](mpsimageedlines/encode(to:sourcetexture:destinationtexture:endpointbuffer:endpointoffset:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedlines)*