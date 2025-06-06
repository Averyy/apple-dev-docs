# init(type:)

**Framework**: ML Compute  
**Kind**: init

Creates an activation descriptor with the activation type you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(type activationType: MLCActivationType)
```

#### Discussion

Use this initializer to create one of the following activation descriptors:

Activation type: [`MLCActivationType.absolute`](mlcactivationtype/absolute.md)

Activation type: [`MLCActivationType.gelu`](mlcactivationtype/gelu.md)

`f(x) = x, if x >= +3`

`f(x) = x * (x + 3)/6`

Activation type: [`MLCActivationType.hardSwish`](mlcactivationtype/hardswish.md)

Activation type: [`MLCActivationType.none`](mlcactivationtype/none.md)

Activation type: [`MLCActivationType.logSigmoid`](mlcactivationtype/logsigmoid.md)

Activation type: [`MLCActivationType.softSign`](mlcactivationtype/softsign.md)

`α = 1.6732632423543772848170429916717`

`scale = 1.0507009873554804934193349852946`

Activation type: [`MLCActivationType.selu`](mlcactivationtype/selu.md)

Activation type: [`MLCActivationType.sigmoid`](mlcactivationtype/sigmoid.md)

Activation type: [`MLCActivationType.tanhShrink`](mlcactivationtype/tanhshrink.md)

## Parameters

- `activationType`: A type of activation function.

## See Also

- [convenience init?(type: MLCActivationType, a: Float)](mlcactivationdescriptor/init(type:a:).md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float)](mlcactivationdescriptor/init(type:a:b:).md)
  Creates an activation descriptor with the activation type and parameters a and b that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float, c: Float)](mlcactivationdescriptor/init(type:a:b:c:).md)
  Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.
- [enum MLCActivationType](mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor/init(type:))*