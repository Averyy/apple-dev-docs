# init(dimension:reductionType:)

**Framework**: ML Compute  
**Kind**: init

Creates a scatter layer with the dimension and reduction type you specify.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
convenience init?(dimension: Int, reductionType: MLCReductionType)
```

#### Discussion

> ❗ **Important**:  The reduction type can be either [`MLCReductionType.none`](mlcreductiontype/none.md) or [`MLCReductionType.sum`](mlcreductiontype/sum.md).

## Parameters

- `dimension`: The dimension to index.
- `reductionType`: The reduction type that applies to all values in a source tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcscatterlayer/init(dimension:reductiontype:))*