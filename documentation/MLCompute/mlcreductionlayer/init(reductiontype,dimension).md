# init(reductionType:dimension:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a reduction layer using the reduction type and dimension you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(reductionType: MLCReductionType, dimension: Int)
```

```objc
+ (instancetype) layerWithReductionType:(MLCReductionType) reductionType dimension:(NSUInteger) dimension;
```

#### Return Value

A new [`MLCReductionLayer`](../mlcreductionlayer.md) instance.

## Parameters

- `reductionType`: The reduction type.
- `dimension`: The dimension to perform the reduction operation on.

## See Also

### Creating Reduction Layers
- [convenience init?(reductionType: MLCReductionType, dimensions: [Int])](./init%28reductiontype,dimensions%29.md)
  Creates a reduction layer using the reduction type and dimensions you specify.
- [enum MLCReductionType](../mlcreductiontype.md)
  Constants that describe a reduction operation type.
- [+ layerWithReductionType:dimensions:](./layerwithreductiontype_dimensions_.md)
  Creates a reduction layer using the reduction type and dimensions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcreductionlayer/init(reductiontype:dimension:))*