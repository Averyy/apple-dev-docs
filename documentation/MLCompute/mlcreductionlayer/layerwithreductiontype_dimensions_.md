# layerWithReductionType:dimensions:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a reduction layer using the reduction type and dimensions you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) layerWithReductionType:(MLCReductionType) reductionType dimensions:(NSArray<NSNumber *> *) dimensions;
```

## Return Value

A new `MLCReductionLayer` instance.

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

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcreductionlayer/layerwithreductiontype:dimensions:)*