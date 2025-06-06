# adam(learningRate:beta1:beta2:epsilon:beta1Power:beta2Power:values:momentum:velocity:maximumVelocity:gradient:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates operations to apply Adam optimization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func adam(learningRate learningRateTensor: MPSGraphTensor, beta1 beta1Tensor: MPSGraphTensor, beta2 beta2Tensor: MPSGraphTensor, epsilon epsilonTensor: MPSGraphTensor, beta1Power beta1PowerTensor: MPSGraphTensor, beta2Power beta2PowerTensor: MPSGraphTensor, values valuesTensor: MPSGraphTensor, momentum momentumTensor: MPSGraphTensor, velocity velocityTensor: MPSGraphTensor, maximumVelocity maximumVelocityTensor: MPSGraphTensor?, gradient gradientTensor: MPSGraphTensor, name: String?) -> [MPSGraphTensor]
```

#### Return Value

If maximumVelocity is nil array of 3 tensors (update, newMomentum, newVelocity) else array of 4 tensors (update, newMomentum, newVelocity, newMaximumVelocity)

#### Discussion

The adam update ops are added current learning rate:

```md
lr[t] = learningRate * sqrt(1 - beta2^t) / (1 - beta1^t)
m[t] = beta1 * m[t-1] + (1 - beta1) * g
v[t] = beta2 * v[t-1] + (1 - beta2) * (g ^ 2)
maxVel[t] = max(maxVel[t-1], v[t])
variable = variable - lr[t] * m[t] / (sqrt(maxVel) + epsilon)
```

## Parameters

- `learningRateTensor`: Scalar tensor which indicates the learning rate to use with the optimizer
- `beta1Tensor`: beta1Tensor
- `beta2Tensor`: beta2Tensor
- `beta1PowerTensor`:   beta1 power tensor
- `beta2PowerTensor`:   beta2 power tensor
- `valuesTensor`: Values to update with optimization
- `momentumTensor`: Momentum tensor
- `velocityTensor`: Velocity tensor
- `maximumVelocityTensor`: Optional maximum velocity tensor
- `gradientTensor`: Partial gradient of the trainable parameters with respect to loss
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/adam(learningrate:beta1:beta2:epsilon:beta1power:beta2power:values:momentum:velocity:maximumvelocity:gradient:name:))*