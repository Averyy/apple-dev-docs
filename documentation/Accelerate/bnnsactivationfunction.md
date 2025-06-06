# BNNSActivationFunction

**Framework**: Accelerate  
**Kind**: struct

Constants that describe activation functions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSActivationFunction
```

## Topics

### Activation Functions
- [static var abs: BNNSActivationFunction](bnnsactivationfunction/abs.md)
  An activation function that returns the absolute value of its input.
- [static var clamp: BNNSActivationFunction](bnnsactivationfunction/clamp.md)
  An activation function that returns its input clamped to a specified range.
- [static var identity: BNNSActivationFunction](bnnsactivationfunction/identity.md)
  An activation function that returns its input.
- [static var integerLinearSaturate: BNNSActivationFunction](bnnsactivationfunction/integerlinearsaturate.md)
  An activation function that returns an arithmetic shift, preserving sign.
- [static var integerLinearSaturatePerChannel: BNNSActivationFunction](bnnsactivationfunction/integerlinearsaturateperchannel.md)
  An activation function that returns an arithmetic shift, preserving sign for each channel.
- [static var leakyRectifiedLinear: BNNSActivationFunction](bnnsactivationfunction/leakyrectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns its input multiplied by a specified value.
- [static var linear: BNNSActivationFunction](bnnsactivationfunction/linear.md)
  An activation function that returns its input multiplied by a specified value.
- [static var rectifiedLinear: BNNSActivationFunction](bnnsactivationfunction/rectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns zero.
- [static var scaledTanh: BNNSActivationFunction](bnnsactivationfunction/scaledtanh.md)
  An activation function that returns the scaled hyperbolic tangent of its input.
- [static var sigmoid: BNNSActivationFunction](bnnsactivationfunction/sigmoid.md)
  An activation function that returns the sigmoid function of its input.
- [static var softmax: BNNSActivationFunction](bnnsactivationfunction/softmax.md)
  An activation function that returns the softmax function of its input.
- [static var tanh: BNNSActivationFunction](bnnsactivationfunction/tanh.md)
  An activation function that returns the hyperbolic tangent of its input.
### Raw Values
- [init(UInt32)](bnnsactivationfunction/init(_:).md)
- [init(rawValue: UInt32)](bnnsactivationfunction/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsactivationfunction/rawvalue.md)
- [var BNNSActivationFunctionAbs: BNNSActivationFunction](bnnsactivationfunctionabs.md)
- [var BNNSActivationFunctionCELU: BNNSActivationFunction](bnnsactivationfunctioncelu.md)
  An activation function that evaluates the continuously differentiable exponential linear units (CELU) on its input.
- [var BNNSActivationFunctionClampedLeakyRectifiedLinear: BNNSActivationFunction](bnnsactivationfunctionclampedleakyrectifiedlinear.md)
  An activation function that returns its input clamped to beta when that is greater than or equal to zero, otherwise it returns its input multiplied by alpha clamped to beta.
- [var BNNSActivationFunctionELU: BNNSActivationFunction](bnnsactivationfunctionelu.md)
  An activation function that evaluates the exponential linear units (ELU) on its input.
- [var BNNSActivationFunctionErf: BNNSActivationFunction](bnnsactivationfunctionerf.md)
- [var BNNSActivationFunctionGELU: BNNSActivationFunction](bnnsactivationfunctiongelu.md)
- [var BNNSActivationFunctionGELUApproximation: BNNSActivationFunction](bnnsactivationfunctiongeluapproximation.md)
  An activation function that evaluates the Gaussian error linear units (GELU) approximation on its input.
- [var BNNSActivationFunctionGELUApproximation2: BNNSActivationFunction](bnnsactivationfunctiongeluapproximation2.md)
  An activation function that provides a fast evaluation of the Gaussian error linear units (GELU) approximation on its input.
- [var BNNSActivationFunctionGELUApproximationSigmoid: BNNSActivationFunction](bnnsactivationfunctiongeluapproximationsigmoid.md)
- [var BNNSActivationFunctionGumbel: BNNSActivationFunction](bnnsactivationfunctiongumbel.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [var BNNSActivationFunctionGumbelMax: BNNSActivationFunction](bnnsactivationfunctiongumbelmax.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [var BNNSActivationFunctionHardShrink: BNNSActivationFunction](bnnsactivationfunctionhardshrink.md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input.
- [var BNNSActivationFunctionHardSigmoid: BNNSActivationFunction](bnnsactivationfunctionhardsigmoid.md)
  An activation function that returns the hard sigmoid function of its input.
- [var BNNSActivationFunctionHardSwish: BNNSActivationFunction](bnnsactivationfunctionhardswish.md)
  An activation function that returns the hard swish function of its input.
- [var BNNSActivationFunctionIdentity: BNNSActivationFunction](bnnsactivationfunctionidentity.md)
- [var BNNSActivationFunctionLeakyRectifiedLinear: BNNSActivationFunction](bnnsactivationfunctionleakyrectifiedlinear.md)
- [var BNNSActivationFunctionLinearWithBias: BNNSActivationFunction](bnnsactivationfunctionlinearwithbias.md)
  An activation function that returns its input multiplied by a scale and added to a bias.
- [var BNNSActivationFunctionLogSigmoid: BNNSActivationFunction](bnnsactivationfunctionlogsigmoid.md)
  An activation function that returns the logarithm of the sigmoid function of its input.
- [var BNNSActivationFunctionLogSoftmax: BNNSActivationFunction](bnnsactivationfunctionlogsoftmax.md)
  An activation function that returns the logarithm of the softmax function of its input.
- [var BNNSActivationFunctionPReLUPerChannel: BNNSActivationFunction](bnnsactivationfunctionpreluperchannel.md)
  An activation function provides per-channel alpha values to Leaky Rectified Linear.
- [var BNNSActivationFunctionRectifiedLinear: BNNSActivationFunction](bnnsactivationfunctionrectifiedlinear.md)
- [var BNNSActivationFunctionReLU6: BNNSActivationFunction](bnnsactivationfunctionrelu6.md)
- [var BNNSActivationFunctionScaledTanh: BNNSActivationFunction](bnnsactivationfunctionscaledtanh.md)
- [var BNNSActivationFunctionSELU: BNNSActivationFunction](bnnsactivationfunctionselu.md)
  An activation function that evaluates the scaled exponential linear units (SELU) on its input.
- [var BNNSActivationFunctionSigmoid: BNNSActivationFunction](bnnsactivationfunctionsigmoid.md)
- [var BNNSActivationFunctionSiLU: BNNSActivationFunction](bnnsactivationfunctionsilu.md)
  An activation function that returns the sigmoid linear unit (SiLU) function of its input.
- [var BNNSActivationFunctionSoftplus: BNNSActivationFunction](bnnsactivationfunctionsoftplus.md)
  An activation function that returns the softplus function of its input.
- [var BNNSActivationFunctionSoftShrink: BNNSActivationFunction](bnnsactivationfunctionsoftshrink.md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input minus alpha.
- [var BNNSActivationFunctionSoftsign: BNNSActivationFunction](bnnsactivationfunctionsoftsign.md)
  An activation function that returns the softsign function of its input.
- [var BNNSActivationFunctionTanh: BNNSActivationFunction](bnnsactivationfunctiontanh.md)
- [var BNNSActivationFunctionTanhShrink: BNNSActivationFunction](bnnsactivationfunctiontanhshrink.md)
  An activation function that returns its input minus the hyperbolic tangent of its input.
- [var BNNSActivationFunctionThreshold: BNNSActivationFunction](bnnsactivationfunctionthreshold.md)
  An activation function that returns beta if its input is less than a specified threshold, otherwise it returns its input.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func BNNSFilterCreateVectorActivationLayer(UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSVectorDescriptor>, UnsafePointer<BNNSActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatevectoractivationlayer(_:_:_:_:).md)
- [class ActivationLayer](bnns/activationlayer.md)
  A layer object that wraps an activation filter and manages its deinitialization.
- [struct BNNSActivation](bnnsactivation.md)
  A set of parameters that describe common activation functions.
- [struct BNNSLayerParametersActivation](bnnslayerparametersactivation.md)
  A set of parameters that define an activation layer.
- [func BNNSFilterCreateLayerActivation(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayeractivation(_:_:).md)
  Returns a new activation layer.
- [func BNNSDirectApplyActivationBatch(UnsafePointer<BNNSLayerParametersActivation>, UnsafePointer<BNNSFilterParameters>?, Int, Int, Int) -> Int32](bnnsdirectapplyactivationbatch(_:_:_:_:_:).md)
  Applies an activation filter to a set of input objects, writing out the result to a set of output objects.
- [static func applyActivation(activation: BNNS.ActivationFunction, axes: [Int], input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:axes:input:output:batchsize:filterparameters:).md)
  Applies an activation function on the specified axes.
- [static func applyActivation(activation: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applyactivation(activation:input:output:batchsize:filterparameters:).md)
  Applies the specified activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction)*