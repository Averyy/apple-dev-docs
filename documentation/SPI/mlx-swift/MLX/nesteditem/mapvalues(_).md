---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/mapvalues(_:)"
framework: "mlx-swift/MLX"
---

# mapValues(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Transform the values in the nested structure using the `transform()` function.

## Declaration

```swift
func mapValues<Result>(_ transform: (Element) throws -> Result) rethrows -> NestedItem<Key, Result>
```

## Discussion

This is typically called via [`mapValues(transform:)`](../nesteddictionary/mapvalues%28transform%29-1ehvq.md).

### See Also

- [`mapValues(transform:)`](../nesteddictionary/mapvalues%28transform%29-1ehvq.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/mapvalues(_:))*