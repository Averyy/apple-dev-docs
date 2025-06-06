# init(learning_rate:alpha:epsilon:centered:momentum:gradient_scale:regularization_scale:regularization_func:clipping_func:clip_gradients_min:clip_gradients_max:clip_gradients_max_norm:clip_gradients_use_norm:)

**Framework**: Accelerate  
**Kind**: init

Returns a new RMSProp optimizer fields structure from the specified parameters.

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
init(learning_rate: Float, alpha: Float, epsilon: Float, centered: Bool, momentum: Float, gradient_scale: Float, regularization_scale: Float, regularization_func: BNNSOptimizerRegularizationFunction, clipping_func: BNNSOptimizerClippingFunction, clip_gradients_min: Float, clip_gradients_max: Float, clip_gradients_max_norm: Float, clip_gradients_use_norm: Float)
```

## Parameters

- `learning_rate`: A value that specifies the learning rate.
- `alpha`: A constant that specifies smoothing, in the range 0 to 1.
- `epsilon`: A term that the optimizer adds to the denominator.
- `centered`: A Boolean value that specifies whether to use the centered variant.
- `momentum`: The rate of momentum decay.
- `gradient_scale`: A value that specifies the gradient scaling factor.
- `regularization_scale`: A value that specifies the regularization scaling factor.
- `regularization_func`: The variable that specifies the regularization function.
- `clipping_func`: The clipping function.
- `clip_gradients_min`: The minimum clipping value for clipping by value.
- `clip_gradients_max`: The maximum clipping value for clipping by value.
- `clip_gradients_max_norm`: The maximum Euclidean norm for clipping by norm and clipping by global norm.
- `clip_gradients_use_norm`: An optional value for a known Euclidean norm for clipping by global norm. Set to   to specify that the function computes the norm.

## See Also

- [struct BNNSOptimizerClippingFunction](bnnsoptimizerclippingfunction.md)
  Constants that describe clipping functions.
- [init()](bnnsoptimizerrmspropwithclippingfields/init.md)
  Returns a new RMSProp optimizer fields structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerrmspropwithclippingfields/init(learning_rate:alpha:epsilon:centered:momentum:gradient_scale:regularization_scale:regularization_func:clipping_func:clip_gradients_min:clip_gradients_max:clip_gradients_max_norm:clip_gradients_use_norm:))*