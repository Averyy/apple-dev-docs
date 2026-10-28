# specializationStrategy

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

Optimization strategy for the model specialization.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```objc
@property (nonatomic, assign, readwrite) MLSpecializationStrategy specializationStrategy;
```

## Discussion

Core ML segments the model’s compute graph and optimizes each segment for the target compute device. This process can affect the model loading time and the prediction latency.

Use this option to tailor the specialization strategy for your application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mloptimizationhints-c.class/specializationstrategy)*