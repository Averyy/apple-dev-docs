---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/sorted(using:)-5led6"
framework: "mlx-swift/MLX"
---

# sorted(using:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.sorted(using:)`.

**Availability**:
- iOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
func sorted<S, Comparator>(using comparators: S) -> [Self.Element] where S : Sequence, Comparator : SortComparator, Comparator == S.Element, Self.Element == Comparator.Compared
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary/sorted(using:)-5led6)*