---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sinusoidalpositionalencoding/init(dimensions:minfrequency:maxfrequency:scale:cosinefirst:fullturns:)"
framework: "mlx-swift/MLXNN"
---

# init(dimensions:minFrequency:maxFrequency:scale:cosineFirst:fullTurns:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Initialize the layer.

## Declaration

```swift
init(dimensions: Int, minFrequency: Float = 0.0001, maxFrequency: Float = 1, scale: Float? = nil, cosineFirst: Bool = false, fullTurns: Bool = false)
```

## Parameters

- `dimensions`: Dimensionality of the resulting positional embeddings
- `minFrequency`: Minimum frequency expected
- `maxFrequency`: Maximum frequency expected
- `scale`: Multiplicative scale for the embeddings.  Default is `sqrt(2 / dimensions)`
- `cosineFirst`: If `true` embed using `[cos(x), sin(x)]` instead of the reverse
- `fullTurns`: If `true` multiply the frequencies with `2 * pi`


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sinusoidalpositionalencoding/init(dimensions:minfrequency:maxfrequency:scale:cosinefirst:fullturns:))*