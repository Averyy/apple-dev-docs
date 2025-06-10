# argSort(axis:sortOrder:)

**Framework**: Accelerate  
**Kind**: method

Adds an argsort operation to the current graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func argSort(axis: Int, sortOrder: BNNSGraph.Builder.SortOrder) -> BNNSGraph.Builder.Tensor<Int32>
```

#### Discussion

This function returns the indices into `self`ordered by the corresponding values.

For example, if `self` contains the values `[1, 4, 2, 3]`, the ascending indices are `[0, 2, 3, 1]`.

## Parameters

- `axis`: The axis over which the operation performs the sort.
- `sortOrder`: The sort order, either ascending or descending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/argsort(axis:sortorder:))*