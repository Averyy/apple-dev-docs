# init(learning_rate:momentum:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:nesterov:regularization_func:sgd_momentum_variant:)

**Framework**: Accelerate  
**Kind**: init

Returns a new SGD with momentum optimizer fields structure from the specified parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(learning_rate: Float, momentum: Float, gradient_scale: Float, regularization_scale: Float, clip_gradients: Bool, clip_gradients_min: Float, clip_gradients_max: Float, nesterov: Bool, regularization_func: BNNSOptimizerRegularizationFunction, sgd_momentum_variant: BNNSOptimizerSGDMomentumVariant)
```

## Parameters

- `learning_rate`: A value that specifies the learning rate.
- `momentum`: The rate of momentum decay.
- `gradient_scale`: A value that specifies the gradient scaling factor.
- `regularization_scale`: A value that specifies the regularization scaling factor.
- `clip_gradients`: A Boolean value that specifies whether to clip the gradient between minimum and maximum values.
- `clip_gradients_min`: The values for the minimum gradient.
- `clip_gradients_max`: The values for the maximum gradient.
- `nesterov`: A Boolean value that specifies whether to use Nesterov momentum update.
- `regularization_func`: The variable that specifies the regularization function.
- `sgd_momentum_variant`: The variable that specifies the momentum variant.

## See Also

- [init()](bnnsoptimizersgdmomentumfields/init.md)
  Returns a new SGD with momentum optimizer fields structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizersgdmomentumfields/init(learning_rate:momentum:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:nesterov:regularization_func:sgd_momentum_variant:))*