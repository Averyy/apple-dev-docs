# init(reductionType:dimension:)

**Framework**: ML Compute  
**Kind**: init

Creates a reduction layer using the reduction type and dimension you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(reductionType: MLCReductionType, dimension: Int)
```

#### Return Value

A new [`MLCReductionLayer`](mlcreductionlayer.md) instance.

## Parameters

- `reductionType`: The reduction type.
- `dimension`: The dimension to perform the reduction operation on.

## See Also

- [convenience init?(reductionType: MLCReductionType, dimensions: [Int])](mlcreductionlayer/init(reductiontype:dimensions:).md)
  Creates a reduction layer using the reduction type and dimensions you specify.
- [enum MLCReductionType](mlcreductiontype.md)
  Constants that describe a reduction operation type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcreductionlayer/init(reductiontype:dimension:))*