# applyStochasticGradientDescent(learningRate:variable:gradient:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

The Stochastic gradient descent performs a gradient descent `variable = variable - (learningRate * g)` where, `g` is gradient of error wrt variable this op directly writes to the variable

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func applyStochasticGradientDescent(learningRate learningRateTensor: MPSGraphTensor, variable: MPSGraphVariableOp, gradient gradientTensor: MPSGraphTensor, name: String?) -> MPSGraphOperation
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `learningRateTensor`: Scalar tensor which indicates the learning rate to use with the optimizer
- `variable`: Variable operation with trainable parameters
- `gradientTensor`: Partial gradient of the trainable parameters with respect to loss
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/applystochasticgradientdescent(learningrate:variable:gradient:name:))*