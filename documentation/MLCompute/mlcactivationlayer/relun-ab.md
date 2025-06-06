# relun(a:b:)

**Framework**: ML Compute  
**Kind**: method

Creates an instance of a ReLUN activation layer using the alpha and beta values you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class func relun(a: Float, b: Float) -> Self
```

#### Return Value

A new `MLCActivationLayer` instance.

#### Discussion

The [`relun(a:b:)`](mlcactivationlayer/relun(a:b:).md) factory type method creates an activation descriptor using [`init(type:a:b:)`](mlcactivationdescriptor/init(type:a:b:).md), where `type =` [`MLCActivationType.relun`](mlcactivationtype/relun.md), `a = alpha`, and `b = beta`, and passes that descriptor to [`init(descriptor:)`](mlcactivationlayer/init(descriptor:).md).

## Parameters

- `a`: The alpha value.
- `b`: The beta value.

## See Also

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
- [class func softPlus(beta: Float) -> Self](mlcactivationlayer/softplus(beta:).md)
  Creates an instance of a soft plus activation layer using the beta value you specify for the soft plus formation.
- [class func softShrink(a: Float) -> Self](mlcactivationlayer/softshrink(a:).md)
  Creates an instance of a soft shrink activation layer using the lambda value you specify for the soft shrink formation.
- [class func threshold(Float, replacement: Float) -> Self](mlcactivationlayer/threshold(_:replacement:).md)
  Creates an instance of a threshold activation layer using the threshold and replacement values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationlayer/relun(a:b:))*