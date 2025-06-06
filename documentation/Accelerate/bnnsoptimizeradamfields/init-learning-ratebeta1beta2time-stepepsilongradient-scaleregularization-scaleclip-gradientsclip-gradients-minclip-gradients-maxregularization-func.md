# init(learning_rate:beta1:beta2:time_step:epsilon:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:regularization_func:)

**Framework**: Accelerate  
**Kind**: init

Returns a new Adam optimizer fields structure from the specified parameters.

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
init(learning_rate: Float, beta1: Float, beta2: Float, time_step: Float, epsilon: Float, gradient_scale: Float, regularization_scale: Float, clip_gradients: Bool, clip_gradients_min: Float, clip_gradients_max: Float, regularization_func: BNNSOptimizerRegularizationFunction)
```

## Parameters

- `learning_rate`: A value that specifies the learning rate.
- `beta1`: A value that specifies the first moment constant in the range 0 to 1.
- `beta2`: A value that specifies the second moment constant in the range 0 to 1.
- `time_step`: A value that’s at least 1 and represents the optimizer’s current time.
- `epsilon`: An addition for the division in the parameter update stage.
- `gradient_scale`: A value that specifies the gradient scaling factor.
- `regularization_scale`: A value that specifies the regularization scaling factor.
- `clip_gradients`: A Boolean value that specifies whether to clip the gradient between minimum and maximum values.
- `clip_gradients_min`: The values for the minimum gradient.
- `clip_gradients_max`: The values for the maximum gradient.
- `regularization_func`: The variable that specifies the regularization function.

## See Also

- [init()](bnnsoptimizeradamfields/init.md)
  Returns a new Adam optimizer fields structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizeradamfields/init(learning_rate:beta1:beta2:time_step:epsilon:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:regularization_func:))*