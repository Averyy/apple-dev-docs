# encode(to:sourceArray:destinationArray:)

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
func encode(to cmdBuf: any MTLCommandBuffer, sourceArray: MPSNDArray, destinationArray destination: MPSNDArray)
```

```objc
- (void) encodeToCommandBuffer:(id<MTLCommandBuffer>) cmdBuf sourceArray:(MPSNDArray *) sourceArray destinationArray:(MPSNDArray *) destination;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayunarykernel/encode(to:sourcearray:destinationarray:))*