# init(descriptor:momentumScale:alpha:epsilon:isCentered:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an RMSProp optimizer with the descriptor, momentum scale, smoothing, epsilon, and option to compute the centered RMSProp that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 14.0+

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor, momentumScale: Float, alpha: Float, epsilon: Float, isCentered: Bool)
```

```objc
+ (instancetype) optimizerWithDescriptor:(MLCOptimizerDescriptor *) optimizerDescriptor momentumScale:(float) momentumScale alpha:(float) alpha epsilon:(float) epsilon isCentered:(BOOL) isCentered;
```

## Parameters

- `optimizerDescriptor`: An object you use to configure the optimizer.
- `momentumScale`: The momentum scale.
- `alpha`: The smoothing constant value.
- `epsilon`: The epsilon value you use to improve numerical stability.
- `isCentered`: A Boolean that indicates whether you compute the centered RMSProp.

## See Also

### Creating an RMSProp Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](./init%28descriptor%29.md)
  Creates an RMSProp optimizer with the descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer/init(descriptor:momentumscale:alpha:epsilon:iscentered:))*