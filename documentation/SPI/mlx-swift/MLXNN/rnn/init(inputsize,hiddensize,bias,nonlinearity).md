---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rnn/init(inputsize:hiddensize:bias:nonlinearity:)"
framework: "mlx-swift/MLXNN"
---

# init(inputSize:hiddenSize:bias:nonLinearity:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

An Elman recurrent layer.

## Declaration

```swift
init(inputSize: Int, hiddenSize: Int, bias: Bool = true, nonLinearity: @escaping (MLXArray, StreamOrDevice) -> MLXArray = tanh)
```

#### Discussion

The input is a sequence of shape `NLD` or `LD` where:

- `N` is the optional batch dimension
- `L` is the sequence length
- `D` is the input’s feature dimension

The hidden state `h` has shape `NH` or `H`, depending on whether the input is batched or not. Returns the hidden state at each time step, of shape `NLH` or `LH`.

## Parameters

- `inputSize`: Dimension of the input, `D`
- `hiddenSize`: Dimension of the hidden state, `H`
- `bias`: If `true` use a bias
- `nonLinearity`: Non-Linearity to use


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rnn/init(inputsize:hiddensize:bias:nonlinearity:))*