# init(device:momentumScale:useNesterovMomentum:optimizerDescriptor:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, momentumScale: Float, useNesterovMomentum: Bool, optimizerDescriptor: MPSNNOptimizerDescriptor)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device momentumScale:(float) momentumScale useNesterovMomentum:(BOOL) useNesterovMomentum optimizerDescriptor:(MPSNNOptimizerDescriptor *) optimizerDescriptor;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnoptimizerstochasticgradientdescent/init(device:momentumscale:usenesterovmomentum:optimizerdescriptor:))*