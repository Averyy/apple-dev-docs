# init(coder:device:)

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
init?(coder aDecoder: NSCoder, device: any MTLDevice)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder device:(id<MTLDevice>) device;
```

## See Also

### Initializers
- [init(device: any MTLDevice, rnnDescriptor: MPSRNNDescriptor)](./init%28device,rnndescriptor%29.md)
- [init(device: any MTLDevice, rnnDescriptors: [MPSRNNDescriptor])](./init%28device,rnndescriptors%29.md)
- [class MPSRNNDescriptor](../mpsrnndescriptor.md)
  A description of a recursive neural network block or layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsrnnmatrixinferencelayer/init(coder:device:))*