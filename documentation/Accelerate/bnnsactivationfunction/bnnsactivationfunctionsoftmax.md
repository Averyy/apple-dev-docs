# BNNSActivationFunctionSoftmax

**Framework**: Accelerate  
**Kind**: case  
**Role**: Enumeration Case

An activation function that returns the softmax function of its input.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```c
BNNSActivationFunctionSoftmax
```

#### Discussion

This constant defines an activation function that returns values using the following formula:

![General formula that describes mathematically the softmax activation function. s open bracket x sub i close bracket equals  the exponential of x sub i over summation from j equals one to n times the exponential of x sub j.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3401551@2x.png)

The softmax function transforms a vector of real numbers into a vector of probabilities. Each probability in the result is in the range 0…1, and the sum of the probabilities is 1.

The following code shows how to apply the softmax function to a vector that contains seven elements:

```swift
let inputs: [Float] = [3, 5, 1, 6, 2, 1, 4]
let count = inputs.count
var outputs = [Float](repeating: 0,
                      count: count)

var inDescription = BNNSVectorDescriptor(size: count,
                                         data_type: .float)
var outDescription = BNNSVectorDescriptor(size: count,
                                          data_type: .float)
var activation = BNNSActivation(function: .softmax)
var filterParameters = BNNSFilterParameters()

let activationLayer = BNNSFilterCreateVectorActivationLayer(&inDescription,
                                                            &outDescription,
                                                            &activation,
                                                            &filterParameters)

BNNSFilterApply(activationLayer, inputs, &outputs)
```

On return, the softmax function calculates the following values:

| Inputs | Outputs |
| --- | --- |
| `3.0` | `0.031415492` |
| `5.0` | `0.23213086` |
| `1.0` | `0.004251625` |
| `6.0` | `0.63099706` |
| `2.0` | `0.011557114` |
| `1.0` | `0.004251625` |
| `4.0` | `0.08539616` |

Changing the fourth element in `inputs` to 10 increases its probability to almost 1.0:

| Inputs | Outputs |
| --- | --- |
| `3.0` | `0.00090221845` |
| `5.0` | `0.0066665425` |
| `1.0` | `0.00012210199` |
| `10.0` | `0.98940265` |
| `2.0` | `0.00033190762` |
| `1.0` | `0.00012210199` |
| `4.0` | `0.002452484` |

## See Also

### Raw Values
- [var BNNSActivationFunctionCELU: BNNSActivationFunction](../bnnsactivationfunctioncelu.md)
  An activation function that evaluates the continuously differentiable exponential linear units (CELU) on its input.
- [BNNSActivationFunctionClamp](./bnnsactivationfunctionclamp.md)
  An activation function that returns its input clamped to the specified range.
- [var BNNSActivationFunctionClampedLeakyRectifiedLinear: BNNSActivationFunction](../bnnsactivationfunctionclampedleakyrectifiedlinear.md)
  An activation function that returns its input clamped to beta when that is greater than or equal to zero, otherwise it returns its input multiplied by alpha clamped to beta.
- [var BNNSActivationFunctionELU: BNNSActivationFunction](../bnnsactivationfunctionelu.md)
  An activation function that evaluates the exponential linear units (ELU) on its input.
- [var BNNSActivationFunctionErf: BNNSActivationFunction](../bnnsactivationfunctionerf.md)
- [var BNNSActivationFunctionGELU: BNNSActivationFunction](../bnnsactivationfunctiongelu.md)
- [var BNNSActivationFunctionGELUApproximation: BNNSActivationFunction](../bnnsactivationfunctiongeluapproximation.md)
  An activation function that evaluates the Gaussian error linear units (GELU) approximation on its input.
- [var BNNSActivationFunctionGELUApproximation2: BNNSActivationFunction](../bnnsactivationfunctiongeluapproximation2.md)
  An activation function that provides a fast evaluation of the Gaussian error linear units (GELU) approximation on its input.
- [var BNNSActivationFunctionGELUApproximationSigmoid: BNNSActivationFunction](../bnnsactivationfunctiongeluapproximationsigmoid.md)
- [var BNNSActivationFunctionGumbel: BNNSActivationFunction](../bnnsactivationfunctiongumbel.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [var BNNSActivationFunctionGumbelMax: BNNSActivationFunction](../bnnsactivationfunctiongumbelmax.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [var BNNSActivationFunctionHardShrink: BNNSActivationFunction](../bnnsactivationfunctionhardshrink.md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input.
- [var BNNSActivationFunctionHardSigmoid: BNNSActivationFunction](../bnnsactivationfunctionhardsigmoid.md)
  An activation function that returns the hard sigmoid function of its input.
- [var BNNSActivationFunctionHardSwish: BNNSActivationFunction](../bnnsactivationfunctionhardswish.md)
  An activation function that returns the hard swish function of its input.
- [BNNSActivationFunctionIntegerLinearSaturate](./bnnsactivationfunctionintegerlinearsaturate.md)
  An activation function that returns an arithmetic shift, preserving sign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctionsoftmax)*