# MPSDataLayout

**Framework**: Metal Performance Shaders  
**Kind**: enum

Options that define how buffer data is arranged.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSDataLayout
```

## Topics

### Enumeration Cases
- [MPSDataLayout.featureChannelsxHeightxWidth](mpsdatalayout/featurechannelsxheightxwidth.md)
- [MPSDataLayout.HeightxWidthxFeatureChannels](mpsdatalayout/heightxwidthxfeaturechannels.md)
### Initializers
- [init?(rawValue: UInt)](mpsdatalayout/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/readbytes(_:datalayout:bytesperrow:region:featurechannelinfo:imageindex:).md)
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/readbytes(_:datalayout:imageindex:).md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/writebytes(_:datalayout:bytesperrow:region:featurechannelinfo:imageindex:).md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/writebytes(_:datalayout:imageindex:).md)
- [struct MPSImageReadWriteParams](mpsimagereadwriteparams.md)
  Parameters that control reading and writing of a particular set of feature channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsdatalayout)*