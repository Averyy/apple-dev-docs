# readBytes(_:dataLayout:bytesPerRow:region:featureChannelInfo:imageIndex:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func readBytes(_ dataBytes: UnsafeMutableRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)
```

```objc
- (void) readBytes:(void *) dataBytes dataLayout:(MPSDataLayout) dataLayout bytesPerRow:(NSUInteger) bytesPerRow region:(MTLRegion) region featureChannelInfo:(MPSImageReadWriteParams) featureChannelInfo imageIndex:(NSUInteger) imageIndex;
```

## See Also

### Methods to Read and Write Raw Data
- [func readBytes(UnsafeMutableRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](./readbytes%28_,datalayout,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)](./writebytes%28_,datalayout,bytesperrow,region,featurechannelinfo,imageindex%29.md)
- [func writeBytes(UnsafeRawPointer, dataLayout: MPSDataLayout, imageIndex: Int)](./writebytes%28_,datalayout,imageindex%29.md)
- [struct MPSImageReadWriteParams](../mpsimagereadwriteparams.md)
  Parameters that control reading and writing of a particular set of feature channels.
- [enum MPSDataLayout](../mpsdatalayout.md)
  Options that define how buffer data is arranged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/readbytes(_:datalayout:bytesperrow:region:featurechannelinfo:imageindex:))*