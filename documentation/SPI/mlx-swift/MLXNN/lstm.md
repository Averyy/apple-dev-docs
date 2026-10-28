---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/lstm"
framework: "mlx-swift/MLXNN"
---

# LSTM

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

An LSTM recurrent layer.

## Declaration

```swift
class LSTM
```

## Overview

See [`init(inputSize:hiddenSize:bias:)`](./lstm/init%28inputsize,hiddensize,bias%29.md)

## Topics

### Initializers
- [init(inputSize: Int, hiddenSize: Int, bias: Bool)](./lstm/init%28inputsize,hiddensize,bias%29.md)
  An LSTM recurrent layer.
### Instance Properties
- [let bias: MLXArray?](./lstm/bias.md)
- [let hiddenSize: Int](./lstm/hiddensize.md)
- [var wh: MLXArray](./lstm/wh.md)
- [var wx: MLXArray](./lstm/wx.md)
### Instance Methods
- [func callAsFunction(MLXArray, hidden: MLXArray?, cell: MLXArray?) -> (MLXArray, MLXArray)](./lstm/callasfunction%28_,hidden,cell%29.md)

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
- [class RNN](./rnn.md)
  An Elman recurrent layer.
- [class GRU](./gru.md)
  A gated recurrent unit (GRU) RNN layer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/lstm)*