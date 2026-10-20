# init(type:a:b:c:)

**Framework**: ML Compute  
**Kind**: init

Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(type activationType: MLCActivationType, a: Float, b: Float, c: Float)
```

## Parameters

- `activationType`: A type of activation function.
- `a`: Parameter a.
- `b`: Parameter b.
- `c`: Parameter c.

## See Also

- [convenience init?(type: MLCActivationType)](mlcactivationdescriptor/init(type:).md)
  Creates an activation descriptor with the activation type you specify.
- [convenience init?(type: MLCActivationType, a: Float)](mlcactivationdescriptor/init(type:a:).md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float)](mlcactivationdescriptor/init(type:a:b:).md)
  Creates an activation descriptor with the activation type and parameters a and b that you specify.
- [enum MLCActivationType](mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor/init(type:a:b:c:))*