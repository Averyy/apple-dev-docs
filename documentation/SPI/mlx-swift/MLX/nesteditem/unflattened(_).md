---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/unflattened(_:)"
framework: "mlx-swift/MLX"
---

# unflattened(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Convert a flattened list of key/value tuples back into a `NestedItem` structure.

## Declaration

```swift
static func unflattened(_ tree: some Collection<(String, Element)>) -> NestedItem<Key, Element> where Key == String
```

#### Discussion

This is typically called via [`unflattened(_:)`](../nesteddictionary/unflattened%28_%29-4p8bn.md).

##### See Also

- [`flattened(prefix:)`](./flattened%28prefix%29.md)
- [`flattened(prefix:)`](../nesteddictionary/flattened%28prefix%29.md)
- [`unflattened(_:)`](../nesteddictionary/unflattened%28_%29-4p8bn.md)
- [`unflattened(_:)`](../nesteddictionary/unflattened%28_%29-4p8bn.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/unflattened(_:))*