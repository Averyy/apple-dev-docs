# encodeBatch(commandBuffer:sourceImages:reshapedWidth:reshapedHeight:reshapedFeatureChannels:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [MPSImage], reshapedWidth: Int, reshapedHeight: Int, reshapedFeatureChannels: Int) -> [MPSImage]
```

```objc
- (MPSImageBatch *) encodeBatchToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImages:(MPSImageBatch *) sourceImages reshapedWidth:(NSUInteger) reshapedWidth reshapedHeight:(NSUInteger) reshapedHeight reshapedFeatureChannels:(NSUInteger) reshapedFeatureChannels;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnreshape/encodebatch(commandbuffer:sourceimages:reshapedwidth:reshapedheight:reshapedfeaturechannels:))*