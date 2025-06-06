# init(splitSectionLengths:dimension:)

**Framework**: ML Compute  
**Kind**: init

Creates a split layer with the lengths of each split section and dimension you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(splitSectionLengths: [Int], dimension: Int)
```

## Parameters

- `splitSectionLengths`: An array that contains the lengths of each split section.
- `dimension`: The dimension or axis along which to split the tensor.

## See Also

- [convenience init(splitCount: Int, dimension: Int)](mlcsplitlayer/init(splitcount:dimension:).md)
  Creates a split layer with the number of splits and dimension you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsplitlayer/init(splitsectionlengths:dimension:))*