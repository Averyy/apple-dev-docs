# encode(to:sourceArrays:sourceGradient:gradientState:destinationArray:)

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
func encode(to cmdBuf: any MTLCommandBuffer, sourceArrays sources: [MPSNDArray], sourceGradient gradient: MPSNDArray, gradientState state: MPSState, destinationArray destination: MPSNDArray)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) cmdBuf sourceArrays:(NSArray<MPSNDArray *> *) sources sourceGradient:(MPSNDArray *) gradient gradientState:(MPSState *) state destinationArray:(MPSNDArray *) destination;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarygradientkernel/encode(to:sourcearrays:sourcegradient:gradientstate:destinationarray:))*