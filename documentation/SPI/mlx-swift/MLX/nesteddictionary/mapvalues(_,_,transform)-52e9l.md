---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/mapvalues(_:_:transform:)-52e9l"
framework: "mlx-swift/MLX"
---

# mapValues(_:_:transform:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second and third `NestedDictionary`.

## Declaration

```swift
func mapValues<E2, E3, R1, R2>(_ dictionary1: NestedDictionary<Key, E2>, _ dictionary2: NestedDictionary<Key, E3>, transform: (Element, E2?, E3?) -> (R1, R2?)) -> (NestedDictionary<Key, R1>, NestedDictionary<Key, R2>)
```

#### Discussion

This transforms all three values simultaneously and produces **two** new `NestedDictionary` conceptually somewhat like `map(zip(i1, i2, i3))`.

The structure of the second and third `NestedDictionary` should be identical to the first but these exceptions are allowed:

- `.none` will match any value, e.g. you can iterate an empty second item
- arrays do not need to be the same length – the receiver’s length is matched
- dictionaries do not need to have the same keys – the receivers keys are matched

##### See Also

- [`mapValues(_:_:_:)`](../nesteditem/mapvalues%28_,_,_%29.md)
- [`mapValues(_:transform:)`](./mapvalues%28_,transform%29-4ctis.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/mapvalues(_:_:transform:)-52e9l)*