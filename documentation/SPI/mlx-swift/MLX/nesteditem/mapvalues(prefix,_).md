---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/mapvalues(prefix:_:)"
framework: "mlx-swift/MLX"
---

# mapValues(prefix:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

A combination of [`mapValues(_:)`](./mapvalues%28_%29.md), [`flattened(prefix:)`](./flattened%28prefix%29.md) and [`unflattened(_:)`](./unflattened%28_%29.md).

## Declaration

```swift
func mapValues<Result>(prefix: String? = nil, _ transform: (String, Element) throws -> Result) rethrows -> NestedItem<Key, Result>
```

## Discussion

This transforms a nested structure into a new nested structure with the same shape but transformed values.  The `transform` function receives a dotted path and the value to transform.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/mapvalues(prefix:_:))*