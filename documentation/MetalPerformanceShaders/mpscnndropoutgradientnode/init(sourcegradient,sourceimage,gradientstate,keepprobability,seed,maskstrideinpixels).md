# init(sourceGradient:sourceImage:gradientState:keepProbability:seed:maskStrideInPixels:)

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
init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)
```

```objc
- (instancetype) initWithSourceGradient:(MPSNNImageNode *) sourceGradient sourceImage:(MPSNNImageNode *) sourceImage gradientState:(MPSNNGradientStateNode *) gradientState keepProbability:(float) keepProbability seed:(NSUInteger) seed maskStrideInPixels:(MTLSize) maskStrideInPixels;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutgradientnode/init(sourcegradient:sourceimage:gradientstate:keepprobability:seed:maskstrideinpixels:))*