# init(type:a:b:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an activation descriptor with the activation type and parameters a and b that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(type activationType: MLCActivationType, a: Float, b: Float)
```

```objc
+ (instancetype) descriptorWithType:(MLCActivationType) activationType a:(float) a b:(float) b;
```

#### Discussion

Use this initializer to create one of the following activation descriptors:

- **Hard Sigmoid**: `f(x) = clamp((x * a) + b, 0, 1)`

Activation type: [`MLCActivationType.hardSigmoid`](../mlcactivationtype/hardsigmoid.md)

For common behavior, set `a` to `0.2` and `b` to `0.5`.

- **Hyperbolic tangent (TanH)**: `f(x) = a * tanh(b * x)`

Activation type: [`MLCActivationType.tanh`](../mlcactivationtype/tanh.md)

For common behavior, set `a` to `1.0` and `b` to `1.0`.

- **Linear**: `f(x) = a * x + b`

Activation type: [`MLCActivationType.linear`](../mlcactivationtype/linear.md)

For common behavior, set `a` to `1.0` and `b` to `0.0`.

- **Parametric Soft Plus**: `f(x) = a * log(1 + e^(b * x))`

Activation type: [`MLCActivationType.softPlus`](../mlcactivationtype/softplus.md)

For common behavior, set `a` to `1.0` and `b` to `1.0`.

- **ReLUN**: `f(x) = min((x >= 0 ? x : a * x), b)`

Activation type: [`MLCActivationType.relun`](../mlcactivationtype/relun.md)

For common behavior, set `a` to `0.0` and `b` to `6.0`.

- **Threshold**: `f(x) = x`, if `x > a`, else `b`, where:

`a = threshold`

`b = replacement`

Activation type: [`MLCActivationType.threshold`](../mlcactivationtype/threshold.md)

## Parameters

- `activationType`: A type of activation function.
- `a`: Parameter a.
- `b`: Parameter b.

## See Also

### Creating Activation Descriptors
- [convenience init?(type: MLCActivationType)](./init%28type%29.md)
  Creates an activation descriptor with the activation type you specify.
- [convenience init?(type: MLCActivationType, a: Float)](./init%28type,a%29.md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float, c: Float)](./init%28type,a,b,c%29.md)
  Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.
- [enum MLCActivationType](../mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor/init(type:a:b:))*