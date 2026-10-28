---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/randomstate"
framework: "mlx-swift/MLX"
---

# MLXRandom.RandomState

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

Random state factory.

## Declaration

```swift
class RandomState
```

## Overview

Note: although this type is thread-safe, the MLXArrays that it returns are not – do not evaluate these values or expressions that depend on them across multiple threads simultaneously.

### See Also

- [`globalState`](./globalstate.md)
- [`withRandomState(_:body:)`](../withrandomstate%28_,body%29-18ob4.md)

## Topics

### Initializers
- [init()](./randomstate/init%28%29.md)
  Initialize the RandomState with a seed based on the current time.
- [init(seed: UInt64)](./randomstate/init%28seed%29.md)
  Initialize the RandomState with the given seed value.
### Instance Methods
- [func asRandomKey() -> MLXArray](./randomstate/asrandomkey%28%29.md)
- [func innerState() -> [MLXArray]](./randomstate/innerstate%28%29.md)
- [func next() -> MLXArray](./randomstate/next%28%29.md)
  Split the current state and return a new Key.
- [func seed(UInt64)](./randomstate/seed%28_%29.md)
  Reset the random state.

## Relationships

### Conforms To
- [Evaluatable](../evaluatable.md)
- [RandomStateOrKey](../randomstateorkey.md)
- Swift.Sendable
- Swift.SendableMetatype
- [Updatable](../updatable.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/randomstate)*