# init(type:a:)

**Framework**: ML Compute  
**Kind**: init

Creates an activation descriptor with the activation type and parameter a that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(type activationType: MLCActivationType, a: Float)
```

#### Discussion

Use this initializer to create one of the following activation descriptors:

Activation type: [`MLCActivationType.celu`](mlcactivationtype/celu.md)

For common behavior, set `a` to `1.0`.

Activation type: [`MLCActivationType.hardShrink`](mlcactivationtype/hardshrink.md)

For common behavior, set `a` to `0.5`.

Activation type: [`MLCActivationType.elu`](mlcactivationtype/elu.md)

For common behavior, set `a` to `1.0`.

Activation type: [`MLCActivationType.relu`](mlcactivationtype/relu.md)

This is also referred to as Leaky ReLU. Some literature defines classical ReLU as `max(0, x)`. If you want this common behavior, set `a` to `0.0`.

Activation type: [`MLCActivationType.softShrink`](mlcactivationtype/softshrink.md)

For common behavior, set `a` to `0.5`.

## Parameters

- `activationType`: A type of activation function.
- `a`: Parameter a.

## See Also

- [convenience init?(type: MLCActivationType)](mlcactivationdescriptor/init(type:).md)
  Creates an activation descriptor with the activation type you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float)](mlcactivationdescriptor/init(type:a:b:).md)
  Creates an activation descriptor with the activation type and parameters a and b that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float, c: Float)](mlcactivationdescriptor/init(type:a:b:c:).md)
  Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.
- [enum MLCActivationType](mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor/init(type:a:))*