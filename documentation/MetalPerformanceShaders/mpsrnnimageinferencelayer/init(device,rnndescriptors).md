# init(device:rnnDescriptors:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, rnnDescriptors: [MPSRNNDescriptor])
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device rnnDescriptors:(NSArray<const MPSRNNDescriptor *> *) rnnDescriptors;
```

## See Also

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./init%28coder,device%29.md)
- [init(device: any MTLDevice, rnnDescriptor: MPSRNNDescriptor)](./init%28device,rnndescriptor%29.md)
- [class MPSRNNDescriptor](../mpsrnndescriptor.md)
  A description of a recursive neural network block or layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnimageinferencelayer/init(device:rnndescriptors:))*