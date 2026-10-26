---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/reduce(_:_:)"
framework: "mlx-swift/MLX"
---

# reduce(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Reduces the contents of the NestedDictionary by visiting each value and applying the `reducer` function, accumulating the result.

## Declaration

```swift
func reduce<R>(_ initialValue: R, _ reducer: (R, Element) throws -> R) rethrows -> R
```

#### Discussion

Typically called via [`reduce(_:_:)`](../nesteddictionary/reduce%28_,_%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem/reduce(_:_:))*