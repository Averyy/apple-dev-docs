# init(type:a:b:c:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(type activationType: MLCActivationType, a: Float, b: Float, c: Float)
```

```objc
+ (instancetype) descriptorWithType:(MLCActivationType) activationType a:(float) a b:(float) b c:(float) c;
```

## Parameters

- `activationType`: A type of activation function.
- `a`: Parameter a.
- `b`: Parameter b.
- `c`: Parameter c.

## See Also

### Creating Activation Descriptors
- [convenience init?(type: MLCActivationType)](./init%28type%29.md)
  Creates an activation descriptor with the activation type you specify.
- [convenience init?(type: MLCActivationType, a: Float)](./init%28type,a%29.md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float)](./init%28type,a,b%29.md)
  Creates an activation descriptor with the activation type and parameters a and b that you specify.
- [enum MLCActivationType](../mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor/init(type:a:b:c:))*