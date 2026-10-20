# paddingMethod()

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func paddingMethod() -> MPSNNPaddingMethod
```

```objc
- (MPSNNPaddingMethod) paddingMethod;
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
- [func label() -> String](./label%28%29.md)
- [func inverse() -> Self?](./inverse%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnpadding/paddingmethod())*