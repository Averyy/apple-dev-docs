---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/gru"
framework: "mlx-swift/MLXNN"
---

# GRU

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

A gated recurrent unit (GRU) RNN layer.

## Declaration

```swift
class GRU
```

## Overview

See [`init(inputSize:hiddenSize:bias:)`](./gru/init%28inputsize,hiddensize,bias%29.md)

## Topics

### Initializers
- [init(inputSize: Int, hiddenSize: Int, bias: Bool)](./gru/init%28inputsize,hiddensize,bias%29.md)
  A gated recurrent unit (GRU) RNN layer.
### Instance Properties
- [let b: MLXArray?](./gru/b.md)
- [let bhn: MLXArray?](./gru/bhn.md)
- [let hiddenSize: Int](./gru/hiddensize.md)
- [var wh: MLXArray](./gru/wh.md)
- [var wx: MLXArray](./gru/wx.md)
### Instance Methods
- [func callAsFunction(MLXArray, hidden: MLXArray?) -> MLXArray](./gru/callasfunction%28_,hidden%29.md)

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
- [class LSTM](./lstm.md)
  An LSTM recurrent layer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/gru)*