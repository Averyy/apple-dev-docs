# MPSDataLayout

**Framework**: Metal Performance Shaders  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum MPSDataLayout : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSDataLayout.featureChannelsxHeightxWidth](./mpsdatalayout/featurechannelsxheightxwidth.md)
- [MPSDataLayout.HeightxWidthxFeatureChannels](./mpsdatalayout/heightxwidthxfeaturechannels.md)
### Initializers
- [init?(rawValue: UInt)](./mpsdatalayout/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Methods to Read and Write Raw Data
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/readbytes%28_,datalayout,bytesperrow,region,featurechannelinfo,imageindex%29.md)
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](./mpsimage/readbytes%28_,datalayout,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/writebytes%28_,datalayout,bytesperrow,region,featurechannelinfo,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](./mpsimage/writebytes%28_,datalayout,imageindex%29.md)
- [struct MPSImageReadWriteParams](./mpsimagereadwriteparams.md)
  Parameters that control reading and writing of a particular set of feature channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsdatalayout)*