# init(reductionType:dimensions:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a reduction layer using the reduction type and dimensions you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.0
- iPadOS 14.5+ - Deprecated in 17.0
- Mac Catalyst 14.5+ - Deprecated in 17.0
- macOS 11.3+ - Deprecated in 14.0
- tvOS 14.5+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init?(reductionType: MLCReductionType, dimensions: [Int])
```

## Parameters

- `reductionType`: The reduction type.
- `dimensions`: The dimensions to perform the reduction operation on.

## See Also

### Creating Reduction Layers
- [convenience init?(reductionType: MLCReductionType, dimension: Int)](./init%28reductiontype,dimension%29.md)
  Creates a reduction layer using the reduction type and dimension you specify.
- [enum MLCReductionType](../mlcreductiontype.md)
  Constants that describe a reduction operation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcreductionlayer/init(reductiontype:dimensions:))*