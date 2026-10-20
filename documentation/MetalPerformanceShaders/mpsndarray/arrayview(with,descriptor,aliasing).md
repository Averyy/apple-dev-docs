# arrayView(with:descriptor:aliasing:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func arrayView(with cmdBuf: any MTLCommandBuffer, descriptor: MPSNDArrayDescriptor, aliasing: MPSAliasingStrategy) -> MPSNDArray?
```

```objc
- (MPSNDArray *) arrayViewWithCommandBuffer:(id<MTLCommandBuffer>) cmdBuf descriptor:(MPSNDArrayDescriptor *) descriptor aliasing:(MPSAliasingStrategy) aliasing;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarray/arrayview(with:descriptor:aliasing:))*