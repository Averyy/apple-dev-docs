---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/lexicographicallyprecedes(_:by:)"
framework: "mlx-swift/MLX"
---

# lexicographicallyPrecedes(_:by:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.lexicographicallyPrecedes(_:by:)`.

## Declaration

```swift
func lexicographicallyPrecedes<OtherSequence>(_ other: OtherSequence, by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/lexicographicallyprecedes(_:by:))*