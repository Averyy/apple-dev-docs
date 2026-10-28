---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/flattenedvalues()"
framework: "mlx-swift/MLX"
---

# flattenedValues()

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return a flattened representation of the structured contents as an array of values.

## Declaration

```swift
func flattenedValues() -> [Element]
```

## Discussion

This is typically called via [`flattenedValues()`](../nesteddictionary/flattenedvalues%28%29.md). Note that unlike [`flattened(prefix:)`](./flattened%28prefix%29.md) this cannot be reconstructed back into the original structure, but can be used with [`replacingValues(with:)`](../nesteddictionary/replacingvalues%28with%29.md) in a similar fashion.

### See Also

- [`flattened(prefix:)`](./flattened%28prefix%29.md)
- [`flattenedValues()`](../nesteddictionary/flattenedvalues%28%29.md)
- [`replacingValues(with:)`](../nesteddictionary/replacingvalues%28with%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/flattenedvalues())*