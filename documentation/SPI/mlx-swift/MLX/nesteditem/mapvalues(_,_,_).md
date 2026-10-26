---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/mapvalues(_:_:_:)"
framework: "mlx-swift/MLX"
---

# mapValues(_:_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second and third `NestedItem`.

## Declaration

```swift
func mapValues<E2, E3, R1, R2, R3>(_ item1: NestedItem<Key, E2>, _ item2: NestedItem<Key, E3>, _ transform: (Element, E2?, E3?) throws -> (R1, R2?, R3?)) rethrows -> (NestedItem<Key, R1>, NestedItem<Key, R2>, NestedItem<Key, R3>)
```

#### Discussion

This transforms all three values simultaneously and produces three new `NestedItem` conceptually somewhat like `map(zip(i1, i2, i3))`.

The structure of the second and third `NestedItem` should be identical to the first but these exceptions are allowed:

- `.none` will match any value, e.g. you can iterate an empty second item
- arrays do not need to be the same length – the receiver’s length is matched
- dictionaries do not need to have the same keys – the receivers keys are matched


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/mapvalues(_:_:_:))*