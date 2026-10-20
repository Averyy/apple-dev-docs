# MPSImageNormalizedHistogram

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSImageNormalizedHistogram : MPSKernel
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpsimagenormalizedhistogram/init%28coder,device%29.md)
- [init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)](./mpsimagenormalizedhistogram/init%28device,histograminfo%29.md)
### Instance Properties
- [var clipRectSource: MTLRegion](./mpsimagenormalizedhistogram/cliprectsource.md)
- [var histogramInfo: MPSImageHistogramInfo](./mpsimagenormalizedhistogram/histograminfo.md)
- [var zeroHistogram: Bool](./mpsimagenormalizedhistogram/zerohistogram.md)
### Instance Methods
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, minmaxTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](./mpsimagenormalizedhistogram/encode%28to,sourcetexture,minmaxtexture,histogram,histogramoffset%29.md)
- [func histogramSize(forSourceFormat: MTLPixelFormat) -> Int](./mpsimagenormalizedhistogram/histogramsize%28forsourceformat%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagenormalizedhistogram)*