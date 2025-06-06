# Preconfigured Activation Layers

**Framework**: ML Compute

Obtain a preconfigured activation layer with common behavior.

#### Overview

Use a factory to receive a preconfigured activation layer for various activation types.

## Topics

### Factory Methods
- [class func celu(a: Float) -> Self](mlcactivationlayer/celu(a:).md)
  Creates an instance of a CELU activation layer using the alpha value you specify for the CELU formation.
- [class func clamp(min: Float, max: Float) -> Self](mlcactivationlayer/clamp(min:max:).md)
  Creates an instance of a clamp activation layer using the minimum and maximum values you specify for the clamp formation.
- [class func elu(a: Float) -> Self](mlcactivationlayer/elu(a:).md)
  Creates an instance of an ELU activation layer using the alpha value you specify for the ELU formation.
- [class func hardShrink(a: Float) -> Self](mlcactivationlayer/hardshrink(a:).md)
  Creates an instance of a hard shrink activation layer using the lambda value you specify for the hard shrink formation.
- [class func leakyReLU(negativeSlope: Float) -> Self](mlcactivationlayer/leakyrelu(negativeslope:).md)
  Creates an instance of a leaky ReLU activation layer using the angle of the negative slope you specify.
- [class func linear(scale: Float, bias: Float) -> Self](mlcactivationlayer/linear(scale:bias:).md)
  Creates an instance of a linear activation layer using the scale factor and bias value you specify.
- [class func relun(a: Float, b: Float) -> Self](mlcactivationlayer/relun(a:b:).md)
  Creates an instance of a ReLUN activation layer using the alpha and beta values you specify.
- [class func softPlus(beta: Float) -> Self](mlcactivationlayer/softplus(beta:).md)
  Creates an instance of a soft plus activation layer using the beta value you specify for the soft plus formation.
- [class func softShrink(a: Float) -> Self](mlcactivationlayer/softshrink(a:).md)
  Creates an instance of a soft shrink activation layer using the lambda value you specify for the soft shrink formation.
- [class func threshold(Float, replacement: Float) -> Self](mlcactivationlayer/threshold(_:replacement:).md)
  Creates an instance of a threshold activation layer using the threshold and replacement values you specify.
### Factory Properties
- [class var absolute: MLCActivationLayer](mlcactivationlayer/absolute.md)
  Creates an instance of an absolute activation layer.
- [class var celu: MLCActivationLayer](mlcactivationlayer/celu.md)
  Creates an instance of a CELU activation layer.
- [class var elu: MLCActivationLayer](mlcactivationlayer/elu.md)
  Creates an instance of a parametric ELU activation layer.
- [class var gelu: MLCActivationLayer](mlcactivationlayer/gelu.md)
  Creates an instance of a GELU activation layer.
- [class var hardShrink: MLCActivationLayer](mlcactivationlayer/hardshrink.md)
  Creates an instance of a hard shrink activation layer.
- [class var hardSigmoid: MLCActivationLayer](mlcactivationlayer/hardsigmoid.md)
  Creates an instance of a hard sigmoid activation layer.
- [class var hardSwish: MLCActivationLayer](mlcactivationlayer/hardswish.md)
  Creates an instance of a hard swish activation layer.
- [class var leakyReLU: MLCActivationLayer](mlcactivationlayer/leakyrelu.md)
  Creates an instance of a leaky ReLU activation layer.
- [class var logSigmoid: MLCActivationLayer](mlcactivationlayer/logsigmoid.md)
  Creates an instance of a log sigmoid activation layer.
- [class var relu: MLCActivationLayer](mlcactivationlayer/relu.md)
  Creates an instance of a ReLU activation layer.
- [class var relu6: MLCActivationLayer](mlcactivationlayer/relu6.md)
  Creates an instance of a ReLU6 activation layer.
- [class var selu: MLCActivationLayer](mlcactivationlayer/selu.md)
  Creates an instance of a SELU activation layer.
- [class var sigmoid: MLCActivationLayer](mlcactivationlayer/sigmoid.md)
  Creates an instance of a sigmoid activation layer.
- [class var softPlus: MLCActivationLayer](mlcactivationlayer/softplus.md)
  Creates an instance of a parametric soft plus activation layer.
- [class var softShrink: MLCActivationLayer](mlcactivationlayer/softshrink.md)
  Creates an instance of a soft shrink activation layer.
- [class var softSign: MLCActivationLayer](mlcactivationlayer/softsign.md)
  Creates an instance of a parametric soft sign activation layer.
- [class var tanh: MLCActivationLayer](mlcactivationlayer/tanh.md)
  Creates an instance of a hyperbolic tangent activation layer.
- [class var tanhShrink: MLCActivationLayer](mlcactivationlayer/tanhshrink.md)
  Creates an instance of a tanh shrink activation layer.

## See Also

- [convenience init(descriptor: MLCActivationDescriptor)](mlcactivationlayer/init(descriptor:).md)
  Creates an activation layer with the descriptor you specify.
- [class MLCActivationDescriptor](mlcactivationdescriptor.md)
  A configuration object you use to create an activation layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/preconfigured-activation-layers)*