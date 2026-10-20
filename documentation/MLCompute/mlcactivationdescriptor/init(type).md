# init(type:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an activation descriptor with the activation type you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(type activationType: MLCActivationType)
```

```objc
+ (instancetype) descriptorWithType:(MLCActivationType) activationType;
```

#### Discussion

Use this initializer to create one of the following activation descriptors:

- **Absolute**: `f(x) = fabs(x)`

Activation type: [`MLCActivationType.absolute`](../mlcactivationtype/absolute.md)

- **GELU**: `f(x) = x * CDF(x)`

Activation type: [`MLCActivationType.gelu`](../mlcactivationtype/gelu.md)

- **Hard Swish**: `f(x) = 0, if x <= -3`

`f(x) = x, if x >= +3`

`f(x) = x * (x + 3)/6`

Activation type: [`MLCActivationType.hardSwish`](../mlcactivationtype/hardswish.md)

- **Identity**: `f(x) = x`

Activation type: [`MLCActivationType.none`](../mlcactivationtype/none.md)

- **LogSigmoid**: `f(x) = log(1 / (1 + exp(-x)))`

Activation type: [`MLCActivationType.logSigmoid`](../mlcactivationtype/logsigmoid.md)

- **Parametric Soft Sign**: `f(x) = x / (1 + abs(x))`

Activation type: [`MLCActivationType.softSign`](../mlcactivationtype/softsign.md)

- **SELU**: `f(x) = scale * (max(0, x) + min(0, α * (exp(x)−1)))`, where:

`α = 1.6732632423543772848170429916717`

`scale = 1.0507009873554804934193349852946`

Activation type: [`MLCActivationType.selu`](../mlcactivationtype/selu.md)

- **Sigmoid**: `f(x) = 1 / (1 + e⁻ˣ)`

Activation type: [`MLCActivationType.sigmoid`](../mlcactivationtype/sigmoid.md)

- **TanhShrink**: `f(x) = x - tanh(x)`

Activation type: [`MLCActivationType.tanhShrink`](../mlcactivationtype/tanhshrink.md)

## Parameters

- `activationType`: A type of activation function.

## See Also

### Creating Activation Descriptors
- [convenience init?(type: MLCActivationType, a: Float)](./init%28type,a%29.md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float)](./init%28type,a,b%29.md)
  Creates an activation descriptor with the activation type and parameters a and b that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float, c: Float)](./init%28type,a,b,c%29.md)
  Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.
- [enum MLCActivationType](../mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor/init(type:))*