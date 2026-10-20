# init(splitSectionLengths:dimension:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a split layer with the lengths of each split section and dimension you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init(splitSectionLengths: [Int], dimension: Int)
```

## Parameters

- `splitSectionLengths`: An array that contains the lengths of each split section.
- `dimension`: The dimension or axis along which to split the tensor.

## See Also

### Creating Split Layers
- [convenience init(splitCount: Int, dimension: Int)](./init%28splitcount,dimension%29.md)
  Creates a split layer with the number of splits and dimension you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsplitlayer/init(splitsectionlengths:dimension:))*