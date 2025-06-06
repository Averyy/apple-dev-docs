# init(type:a:b:)

**Framework**: ML Compute  
**Kind**: init

Creates an activation descriptor with the activation type and parameters a and b that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(type activationType: MLCActivationType, a: Float, b: Float)
```

#### Discussion

Use this initializer to create one of the following activation descriptors:

Activation type: [`MLCActivationType.hardSigmoid`](mlcactivationtype/hardsigmoid.md)

For common behavior, set `a` to `0.2` and `b` to `0.5`.

Activation type: [`MLCActivationType.tanh`](mlcactivationtype/tanh.md)

For common behavior, set `a` to `1.0` and `b` to `1.0`.

Activation type: [`MLCActivationType.linear`](mlcactivationtype/linear.md)

For common behavior, set `a` to `1.0` and `b` to `0.0`.

Activation type: [`MLCActivationType.softPlus`](mlcactivationtype/softplus.md)

For common behavior, set `a` to `1.0` and `b` to `1.0`.

Activation type: [`MLCActivationType.relun`](mlcactivationtype/relun.md)

For common behavior, set `a` to `0.0` and `b` to `6.0`.

`a = threshold`

`b = replacement`

Activation type: [`MLCActivationType.threshold`](mlcactivationtype/threshold.md)

## Parameters

- `activationType`: A type of activation function.
- `a`: Parameter a.
- `b`: Parameter b.

## See Also

- [convenience init?(type: MLCActivationType)](mlcactivationdescriptor/init(type:).md)
  Creates an activation descriptor with the activation type you specify.
- [convenience init?(type: MLCActivationType, a: Float)](mlcactivationdescriptor/init(type:a:).md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float, c: Float)](mlcactivationdescriptor/init(type:a:b:c:).md)
  Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.
- [enum MLCActivationType](mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor/init(type:a:b:))*