# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an RMSProp optimizer with the descriptor you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 14.0+

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor)
```

```objc
+ (instancetype) optimizerWithDescriptor:(MLCOptimizerDescriptor *) optimizerDescriptor;
```

## Return Value

An RMSProp optimizer.

## Discussion

Sets [`momentumScale`](../mlcsgdoptimizer/momentumscale.md) to `0.0`, [`alpha`](./alpha.md) to `0.99`, [`epsilon`](./epsilon.md) to `1e-8` , and [`isCentered`](./iscentered.md) to `false` by default.

## Parameters

- `optimizerDescriptor`: An object you use to configure the optimizer.

## See Also

### Creating an RMSProp Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor, momentumScale: Float, alpha: Float, epsilon: Float, isCentered: Bool)](./init%28descriptor,momentumscale,alpha,epsilon,iscentered%29.md)
  Creates an RMSProp optimizer with the descriptor, momentum scale, smoothing, epsilon, and option to compute the centered RMSProp that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer/init(descriptor:))*