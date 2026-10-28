# init(dimension:reductionType:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a scatter layer with the dimension and reduction type you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(dimension: Int, reductionType: MLCReductionType)
```

```objc
+ (instancetype) layerWithDimension:(NSUInteger) dimension reductionType:(MLCReductionType) reductionType;
```

## Discussion

> ❗ **Important**:  The reduction type can be either [`MLCReductionType.none`](../mlcreductiontype/none.md) or [`MLCReductionType.sum`](../mlcreductiontype/sum.md).

## Parameters

- `dimension`: The dimension to index.
- `reductionType`: The reduction type that applies to all values in a source tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcscatterlayer/init(dimension:reductiontype:))*