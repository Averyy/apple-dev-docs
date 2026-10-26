# init(splitCount:dimension:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a split layer with the number of splits and dimension you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(splitCount: Int, dimension: Int)
```

```objc
+ (instancetype) layerWithSplitCount:(NSUInteger) splitCount dimension:(NSUInteger) dimension;
```

## Parameters

- `splitCount`: The number of splits.
- `dimension`: The dimension or axis along which to split the tensor.

## See Also

### Creating Split Layers
- [convenience init(splitSectionLengths: [Int], dimension: Int)](./init%28splitsectionlengths,dimension%29.md)
  Creates a split layer with the lengths of each split section and dimension you specify.
- [+ layerWithSplitSectionLengths:dimension:](./layerwithsplitsectionlengths_dimension_.md)
  Creates a split layer with the lengths of each split section and dimension you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsplitlayer/init(splitcount:dimension:))*