# leakyReLU(negativeSlope:)

**Framework**: ML Compute  
**Kind**: method

Creates an instance of a leaky ReLU activation layer using the angle of the negative slope you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class func leakyReLU(negativeSlope: Float) -> Self
```

#### Return Value

A new `MLCActivationLayer` instance.

#### Discussion

The [`leakyReLU(negativeSlope:)`](mlcactivationlayer/leakyrelu(negativeslope:).md) factory type method creates an activation descriptor using [`init(type:a:)`](mlcactivationdescriptor/init(type:a:).md), where `type =` [`MLCActivationType.relu`](mlcactivationtype/relu.md) and `a = negativeSlope`, and passes that descriptor to [`init(descriptor:)`](mlcactivationlayer/init(descriptor:).md).

## Parameters

- `negativeSlope`: The angle of the negative slope.

## See Also

- [class func celu(a: Float) -> Self](mlcactivationlayer/celu(a:).md)
  Creates an instance of a CELU activation layer using the alpha value you specify for the CELU formation.
- [class func clamp(min: Float, max: Float) -> Self](mlcactivationlayer/clamp(min:max:).md)
  Creates an instance of a clamp activation layer using the minimum and maximum values you specify for the clamp formation.
- [class func elu(a: Float) -> Self](mlcactivationlayer/elu(a:).md)
  Creates an instance of an ELU activation layer using the alpha value you specify for the ELU formation.
- [class func hardShrink(a: Float) -> Self](mlcactivationlayer/hardshrink(a:).md)
  Creates an instance of a hard shrink activation layer using the lambda value you specify for the hard shrink formation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationlayer/leakyrelu(negativeslope:))*