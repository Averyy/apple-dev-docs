# MPSImageReadWriteParams

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

Parameters that control reading and writing of a particular set of feature channels.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSImageReadWriteParams
```

```c
typedef struct { ... } MPSImageReadWriteParams;
```

## Topics

### Instance Properties
- [var featureChannelOffset: Int](./mpsimagereadwriteparams/featurechanneloffset.md)
- [var numberOfFeatureChannelsToReadWrite: Int](./mpsimagereadwriteparams/numberoffeaturechannelstoreadwrite.md)
### Initializers
- [init()](./mpsimagereadwriteparams/init%28%29.md)
- [init(featureChannelOffset: Int, numberOfFeatureChannelsToReadWrite: Int)](./mpsimagereadwriteparams/init%28featurechanneloffset,numberoffeaturechannelstoreadwrite%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Methods to Read and Write Raw Data
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/readbytes%28_,datalayout,bytesperrow,region,featurechannelinfo,imageindex%29.md)
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](./mpsimage/readbytes%28_,datalayout,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./mpsimage/writebytes%28_,datalayout,bytesperrow,region,featurechannelinfo,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](./mpsimage/writebytes%28_,datalayout,imageindex%29.md)
- [enum MPSDataLayout](./mpsdatalayout.md)
  Options that define how buffer data is arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagereadwriteparams)*