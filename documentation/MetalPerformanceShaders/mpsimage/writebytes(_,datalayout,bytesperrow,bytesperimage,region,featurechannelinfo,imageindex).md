# writeBytes(_:dataLayout:bytesPerRow:bytesPerImage:region:featureChannelInfo:imageIndex:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func writeBytes(_ dataBytes: UnsafeRawPointer, dataLayout: MPSDataLayout, bytesPerRow: Int, bytesPerImage: Int, region: MTLRegion, featureChannelInfo: MPSImageReadWriteParams, imageIndex: Int)
```

```objc
- (void) writeBytes:(const void *) dataBytes dataLayout:(MPSDataLayout) dataLayout bytesPerRow:(NSUInteger) bytesPerRow bytesPerImage:(NSUInteger) bytesPerImage region:(MTLRegion) region featureChannelInfo:(MPSImageReadWriteParams) featureChannelInfo imageIndex:(NSUInteger) imageIndex;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/writebytes(_:datalayout:bytesperrow:bytesperimage:region:featurechannelinfo:imageindex:))*