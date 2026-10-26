---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/compactmapvalues(_:)"
framework: "mlx-swift/MLX"
---

# compactMapValues(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Transform the values in the nested structure using the `transform()` function.

## Declaration

```swift
func compactMapValues<Result>(_ transform: (Element) throws -> Result?) rethrows -> NestedItem<Key, Result>
```

#### Discussion

This is typically called via [`compactMapValues(transform:)`](../nesteddictionary/compactmapvalues%28transform%29.md).

##### See Also

- [`compactMapValues(transform:)`](../nesteddictionary/compactmapvalues%28transform%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/compactmapvalues(_:))*