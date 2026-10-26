---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/mapvalues(transform:)-4q1m3"
framework: "mlx-swift/MLX"
---

# mapValues(transform:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Transform the values in the nested structure using the `transform()` function.

## Declaration

```swift
func mapValues<Result>(transform: (String, Element) throws -> Result) rethrows -> NestedDictionary<Key, Result>
```

#### Discussion

This function receives both keys in dotted form and values.  This is roughly equivalent to:

```swift
let transformed = nd.flattened().map { key, value in (key, transformedValue) }
let result = NestedDictionary.unflattened(transformed)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/mapvalues(transform:)-4q1m3)*