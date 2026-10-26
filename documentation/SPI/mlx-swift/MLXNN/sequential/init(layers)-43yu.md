---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sequential/init(layers:)-43yu"
framework: "mlx-swift/MLXNN"
---

# init(layers:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

A convenient way to write code that builds a Sequential layer:

## Declaration

```swift
init(@SequentialBuilder layers: () -> [any UnaryLayer])
```

#### Discussion

```swift
// a nonsensical Sequential layer, but it demonstrates how
// to constructuct something with an interesting structure
let b = Bool.random()
let s = Sequential {
    Tanh()
    if b {
        Tanh()
    } else {
        Sigmoid()
    }
    for _ in 0 ..< 3 {
        Linear(10, 20)
    }
}
```

produces:

```swift
Sequential {
  layers: [
    Tanh,
    Sigmoid,
    Linear(inputDimensions=10, outputDimensions=20, bias=true),
    Linear(inputDimensions=10, outputDimensions=20, bias=true),
    Linear(inputDimensions=10, outputDimensions=20, bias=true)
  ],
}
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sequential/init(layers:)-43yu)*