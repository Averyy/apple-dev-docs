---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/graphdescription(_:namer:)"
framework: "mlx-swift/MLX"
---

# graphDescription(_:namer:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

A textual description of the compute graph that produces `outputs`.

## Declaration

```swift
func graphDescription(_ outputs: [MLXArray], namer: NodeNamer? = nil) -> String
```

#### Return Value

The description of the graph

#### Discussion

The arrays are not evaluated – this describes the graph as it currently stands.

##### See Also

- [`exportToDot(_:namer:)`](./exporttodot%28_,namer%29.md)
- [`NodeNamer`](./nodenamer.md)

## Parameters

- `outputs`: The outputs of the graph to describe
- `namer`: Optional namer providing readable names for arrays


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/graphdescription(_:namer:))*