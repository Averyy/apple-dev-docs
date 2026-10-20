# elu(a:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates an instance of an ELU activation layer using the alpha value you specify for the ELU formation.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class func elu(a: Float) -> Self
```

```objc
+ (instancetype) eluLayerWithA:(float) a;
```

#### Return Value

A new `MLCActivationLayer` instance.

#### Discussion

The [`elu(a:)`](./elu%28a%29.md) factory type method creates an activation descriptor using [`init(type:a:)`](../mlcactivationdescriptor/init%28type,a%29.md), where `type =` [`MLCActivationType.elu`](../mlcactivationtype/elu.md) and `a = alpha`, and passes that descriptor to [`init(descriptor:)`](./init%28descriptor%29.md).

## Parameters

- `a`: The alpha value for the ELU formation.

## See Also

### Factory Methods
- [class func celu(a: Float) -> Self](./celu%28a%29.md)
  Creates an instance of a CELU activation layer using the alpha value you specify for the CELU formation.
- [class func clamp(min: Float, max: Float) -> Self](./clamp%28min,max%29.md)
  Creates an instance of a clamp activation layer using the minimum and maximum values you specify for the clamp formation.
- [class func hardShrink(a: Float) -> Self](./hardshrink%28a%29.md)
  Creates an instance of a hard shrink activation layer using the lambda value you specify for the hard shrink formation.
- [class func leakyReLU(negativeSlope: Float) -> Self](./leakyrelu%28negativeslope%29.md)
  Creates an instance of a leaky ReLU activation layer using the angle of the negative slope you specify.
- [class func linear(scale: Float, bias: Float) -> Self](./linear%28scale,bias%29.md)
  Creates an instance of a linear activation layer using the scale factor and bias value you specify.
- [class func relun(a: Float, b: Float) -> Self](./relun%28a,b%29.md)
  Creates an instance of a ReLUN activation layer using the alpha and beta values you specify.
- [class func softPlus(beta: Float) -> Self](./softplus%28beta%29.md)
  Creates an instance of a soft plus activation layer using the beta value you specify for the soft plus formation.
- [class func softShrink(a: Float) -> Self](./softshrink%28a%29.md)
  Creates an instance of a soft shrink activation layer using the lambda value you specify for the soft shrink formation.
- [class func threshold(Float, replacement: Float) -> Self](./threshold%28_,replacement%29.md)
  Creates an instance of a threshold activation layer using the threshold and replacement values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationlayer/elu(a:))*