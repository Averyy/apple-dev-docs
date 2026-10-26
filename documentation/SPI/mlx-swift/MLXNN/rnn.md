---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rnn"
framework: "mlx-swift/MLXNN"
---

# RNN

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

An Elman recurrent layer.

## Declaration

```swift
class RNN
```

#### Overview

See [`init(inputSize:hiddenSize:bias:nonLinearity:)`](./rnn/init%28inputsize,hiddensize,bias,nonlinearity%29.md)

## Topics

### Initializers
- [init(inputSize: Int, hiddenSize: Int, bias: Bool, nonLinearity: (MLXArray, StreamOrDevice) -> MLXArray)](./rnn/init%28inputsize,hiddensize,bias,nonlinearity%29.md)
  An Elman recurrent layer.
### Instance Properties
- [let bias: MLXArray?](./rnn/bias.md)
- [let hiddenSize: Int](./rnn/hiddensize.md)
- [let nonLinearity: (MLXArray, StreamOrDevice) -> MLXArray](./rnn/nonlinearity.md)
- [var whh: MLXArray](./rnn/whh.md)
- [var wxh: MLXArray](./rnn/wxh.md)
### Instance Methods
- [func callAsFunction(MLXArray, hidden: MLXArray?) -> MLXArray](./rnn/callasfunction%28_,hidden%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible

## See Also

### Recurrent
- [class GRU](./gru.md)
  A gated recurrent unit (GRU) RNN layer.
- [class LSTM](./lstm.md)
  An LSTM recurrent layer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rnn)*