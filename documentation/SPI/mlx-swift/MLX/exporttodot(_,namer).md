---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/exporttodot(_:namer:)"
framework: "mlx-swift/MLX"
---

# exportToDot(_:namer:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

A [GraphViz](https://graphviz.org) `DOT` representation of the compute graph that produces `outputs`.

## Declaration

```swift
func exportToDot(_ outputs: [MLXArray], namer: NodeNamer? = nil) -> String
```

#### Return Value

The graph in `DOT` format

#### Discussion

The arrays are not evaluated – this describes the graph as it currently stands.

```swift
let x = MLXArray([1, 2, 3])
let dot = exportToDot([x * 2 + 1])
try dot.write(to: url, atomically: true, encoding: .utf8)
```

##### See Also

- [`graphDescription(_:namer:)`](./graphdescription%28_,namer%29.md)
- [`NodeNamer`](./nodenamer.md)

## Parameters

- `outputs`: The outputs of the graph to describe
- `namer`: Optional namer providing readable names for arrays


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/exporttodot(_:namer:))*