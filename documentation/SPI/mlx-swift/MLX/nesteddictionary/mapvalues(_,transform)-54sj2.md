---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/mapvalues(_:transform:)-54sj2"
framework: "mlx-swift/MLX"
---

# mapValues(_:transform:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second `NestedDictionary`.

## Declaration

```swift
func mapValues<E2, R1, R2>(_ dictionary1: NestedDictionary<Key, E2>, transform: (Element, E2?) throws -> (R1, R2?)) rethrows -> (NestedDictionary<Key, R1>, NestedDictionary<Key, R2>)
```

## Discussion

This transforms both values simultaneously and produces two new `NestedDictionary` conceptually somewhat like `map(zip(i1, i2))`.

The structure of the second `NestedDictionary` should be identical to the first but these exceptions are allowed:

- `.none` will match any value, e.g. you can iterate an empty second item
- arrays do not need to be the same length – the receiver’s length is matched
- dictionaries do not need to have the same keys – the receivers keys are matched

### See Also

- [`mapValues(_:_:)`](../nesteditem/mapvalues%28_,_%29.md)
- [`mapValues(_:_:transform:)`](./mapvalues%28_,_,transform%29-52e9l.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/mapvalues(_:transform:)-54sj2)*