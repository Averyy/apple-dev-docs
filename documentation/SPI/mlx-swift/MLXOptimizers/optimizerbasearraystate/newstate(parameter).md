---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/optimizerbasearraystate/newstate(parameter:)"
framework: "mlx-swift/MLXOptimizers"
---

# newState(parameter:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: method  
**Role**: Instance Method

Subclasses must implement this to create a new `State` when needed.  This is called for each parameter in the model.

## Declaration

```swift
override func newState(parameter: MLXArray) -> MLXArray
```

#### Discussion

For example:

```swift
override func newState(parameter: MLXArray) -> MLXArray {
    MLXArray.zeros(like: gradient)
}
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/optimizerbasearraystate/newstate(parameter:))*