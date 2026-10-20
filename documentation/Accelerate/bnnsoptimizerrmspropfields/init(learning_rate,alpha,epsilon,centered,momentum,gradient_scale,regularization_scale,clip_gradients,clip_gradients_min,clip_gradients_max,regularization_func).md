# init(learning_rate:alpha:epsilon:centered:momentum:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:regularization_func:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new RMSProp optimizer fields structure from the specified parameters.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
init(learning_rate: Float, alpha: Float, epsilon: Float, centered: Bool, momentum: Float, gradient_scale: Float, regularization_scale: Float, clip_gradients: Bool, clip_gradients_min: Float, clip_gradients_max: Float, regularization_func: BNNSOptimizerRegularizationFunction)
```

## Parameters

- `learning_rate`: A value that specifies the learning rate.
- `alpha`: A constant that specifies smoothing, in the range 0 to 1.
- `epsilon`: A term that the optimizer adds to the denominator.
- `centered`: A Boolean value that specifies whether to use the centered variant.
- `momentum`: The rate of momentum decay.
- `gradient_scale`: A value that specifies the gradient scaling factor.
- `regularization_scale`: A value that specifies the regularization scaling factor.
- `clip_gradients`: A Boolean value that specifies whether to clip the gradient between minimum and maximum values.
- `clip_gradients_min`: The values for the minimum gradient.
- `clip_gradients_max`: The values for the maximum gradient.
- `regularization_func`: The variable that specifies the regularization function.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Returns a new RMSProp optimizer fields structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerrmspropfields/init(learning_rate:alpha:epsilon:centered:momentum:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:regularization_func:))*