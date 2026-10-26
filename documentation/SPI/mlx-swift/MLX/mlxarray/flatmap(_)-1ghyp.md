---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/flatmap(_:)-1ghyp"
framework: "mlx-swift/MLX"
---

# flatMap(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.flatMap(_:)`.

**Availability**:
- Swift - Deprecated in 4.1 (renamed: compactMap(_:))

> **Deprecated**: Please use compactMap(_:) for the case where closure returns an optional value

## Declaration

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/flatmap(_:)-1ghyp)*