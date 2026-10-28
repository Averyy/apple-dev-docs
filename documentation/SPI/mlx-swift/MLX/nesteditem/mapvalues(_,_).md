---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/mapvalues(_:_:)"
framework: "mlx-swift/MLX"
---

# mapValues(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second `NestedItem`.

## Declaration

```swift
func mapValues<E2, R1, R2>(_ item: NestedItem<Key, E2>, _ transform: (Element, E2?) throws -> (R1, R2?)) rethrows -> (NestedItem<Key, R1>, NestedItem<Key, R2>)
```

## Discussion

This transforms both values simultaneously and produces two new `NestedItem` conceptually somewhat like `map(zip(i1, i2))`.

The structure of the second `NestedItem` should be identical to the first but these exceptions are allowed:

- `.none` will match any value, e.g. you can iterate an empty second item
- arrays do not need to be the same length – the receiver’s length is matched
- dictionaries do not need to have the same keys – the receivers keys are matched


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/mapvalues(_:_:))*