# label()

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
optional func label() -> String
```

```objc
- (NSString *) label;
```

## See Also

### Instance Methods
- [func destinationImageDescriptor(forSourceImages: [MPSImage], sourceStates: [MPSState]?, for: MPSKernel, suggestedDescriptor: MPSImageDescriptor) -> MPSImageDescriptor](./destinationimagedescriptor%28forsourceimages,sourcestates,for,suggesteddescriptor%29.md)
- [class MPSImage](../mpsimage.md)
  A texture that may have more than four channels for use in convolutional neural networks.
- [class MPSState](../mpsstate.md)
  An opaque data container for large storage in MPS CNN filters.
- [class MPSKernel](../mpskernel.md)
  A standard interface for Metal Performance Shaders kernels.
- [class MPSImageDescriptor](../mpsimagedescriptor.md)
  A description of the attributes used to create an [`MPSImage`](../mpsimage.md).
- [func paddingMethod() -> MPSNNPaddingMethod](./paddingmethod%28%29.md)
- [func inverse() -> Self?](./inverse%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpadding/label())*