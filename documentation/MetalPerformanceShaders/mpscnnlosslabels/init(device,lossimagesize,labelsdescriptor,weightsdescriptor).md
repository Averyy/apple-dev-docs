# init(device:lossImageSize:labelsDescriptor:weightsDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, lossImageSize: MTLSize, labelsDescriptor: MPSCNNLossDataDescriptor, weightsDescriptor: MPSCNNLossDataDescriptor?)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device lossImageSize:(MTLSize) lossImageSize labelsDescriptor:(MPSCNNLossDataDescriptor *) labelsDescriptor weightsDescriptor:(MPSCNNLossDataDescriptor *) weightsDescriptor;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlosslabels/init(device:lossimagesize:labelsdescriptor:weightsdescriptor:))*