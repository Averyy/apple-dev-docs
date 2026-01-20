# MPSImageReadWriteParams

**Framework**: Metal Performance Shaders  
**Kind**: struct

Parameters that control reading and writing of a particular set of feature channels.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSImageReadWriteParams
```

## Topics

### Instance Properties
- [var featureChannelOffset: Int](mpsimagereadwriteparams/featurechanneloffset.md)
- [var numberOfFeatureChannelsToReadWrite: Int](mpsimagereadwriteparams/numberoffeaturechannelstoreadwrite.md)
### Initializers
- [init()](mpsimagereadwriteparams/init.md)
- [init(featureChannelOffset: Int, numberOfFeatureChannelsToReadWrite: Int)](mpsimagereadwriteparams/init(featurechanneloffset:numberoffeaturechannelstoreadwrite:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/readbytes(_:datalayout:bytesperrow:region:featurechannelinfo:imageindex:).md)
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/readbytes(_:datalayout:imageindex:).md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](mpsimage/writebytes(_:datalayout:bytesperrow:region:featurechannelinfo:imageindex:).md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](mpsimage/writebytes(_:datalayout:imageindex:).md)
- [enum MPSDataLayout](mpsdatalayout.md)
  Options that define how buffer data is arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagereadwriteparams)*