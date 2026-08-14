# MPSImageNormalizedHistogram

**Framework**: Metal Performance Shaders  
**Kind**: class

A filter that computes the normalized histogram of an image.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MPSImageNormalizedHistogram
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpsimagenormalizedhistogram/init(coder:device:).md)
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](mpsimagenormalizedhistogram/init(device:histograminfo:).md)
### Instance Properties
- [var clipRectSource: MTLRegion](mpsimagenormalizedhistogram/cliprectsource.md)
- [var histogramInfo: MPSImageHistogramInfo](mpsimagenormalizedhistogram/histograminfo.md)
- [var zeroHistogram: Bool](mpsimagenormalizedhistogram/zerohistogram.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, minmaxTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](mpsimagenormalizedhistogram/encode(to:sourcetexture:minmaxtexture:histogram:histogramoffset:).md)
- [func histogramSize(forSourceFormat: MTLPixelFormat) -> Int](mpsimagenormalizedhistogram/histogramsize(forsourceformat:).md)

## Relationships

### Inherits From
- [MPSKernel](mpskernel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagenormalizedhistogram)*