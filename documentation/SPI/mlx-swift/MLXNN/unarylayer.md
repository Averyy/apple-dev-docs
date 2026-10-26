---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/unarylayer"
framework: "mlx-swift/MLXNN"
---

# UnaryLayer

**Framework**: mlx-swift/MLXNN  
**Kind**: protocol  
**Role**: Protocol

A `Layer` ([`Module`](./module.md) subclass) that can be evaluated as a *unary function*.

## Declaration

```swift
protocol UnaryLayer : Module
```

#### Overview

This provides [`callAsFunction(_:)`](./unarylayer/callasfunction%28_%29.md) with a single `MLXArray` input and a single `MLXArray` output.

##### See Also

- [Layers](./layers.md)
- [`Sequential`](./sequential.md)

## Topics

### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./unarylayer/callasfunction%28_%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforming Types
- [AllToShardedLinear](./alltoshardedlinear.md)
- [AvgPool1d](./avgpool1d.md)
- [AvgPool2d](./avgpool2d.md)
- [AvgPool3d](./avgpool3d.md)
- [BatchNorm](./batchnorm.md)
- [CELU](./celu.md)
- [Conv1d](./conv1d.md)
- [Conv2d](./conv2d.md)
- [Conv3d](./conv3d.md)
- [ConvTransposed1d](./convtransposed1d.md)
- [ConvTransposed2d](./convtransposed2d.md)
- [ConvTransposed3d](./convtransposed3d.md)
- [Dropout](./dropout.md)
- [Dropout2d](./dropout2d.md)
- [Dropout3d](./dropout3d.md)
- [ELU](./elu.md)
- [Embedding](./embedding.md)
- [GELU](./gelu.md)
- [GLU](./glu.md)
- [GroupNorm](./groupnorm.md)
- [HardShrink](./hardshrink.md)
- [HardSwish](./hardswish.md)
- [HardTanh](./hardtanh.md)
- [Identity](./identity.md)
- [InstanceNorm](./instancenorm.md)
- [LayerNorm](./layernorm.md)
- [LeakyReLU](./leakyrelu.md)
- [Linear](./linear.md)
- [LogSigmoid](./logsigmoid.md)
- [LogSoftmax](./logsoftmax.md)
- [MaxPool1d](./maxpool1d.md)
- [MaxPool2d](./maxpool2d.md)
- [MaxPool3d](./maxpool3d.md)
- [Mish](./mish.md)
- [PReLU](./prelu.md)
- [Pool](./pool.md)
- [QuantizedAllToShardedLinear](./quantizedalltoshardedlinear.md)
- [QuantizedEmbedding](./quantizedembedding.md)
- [QuantizedLinear](./quantizedlinear.md)
- [QuantizedShardedToAllLinear](./quantizedshardedtoalllinear.md)
- [RMSNorm](./rmsnorm.md)
- [ReLU](./relu.md)
- [ReLU6](./relu6.md)
- [ReLUSquared](./relusquared.md)
- [RoPE](./rope.md)
- [SELU](./selu.md)
- [Sequential](./sequential.md)
- [ShardedToAllLinear](./shardedtoalllinear.md)
- [SiLU](./silu.md)
- [Sigmoid](./sigmoid.md)
- [SinusoidalPositionalEncoding](./sinusoidalpositionalencoding.md)
- [Softmax](./softmax.md)
- [Softmin](./softmin.md)
- [Softplus](./softplus.md)
- [Softshrink](./softshrink.md)
- [Softsign](./softsign.md)
- [Step](./step.md)
- [Tanh](./tanh.md)
- [Upsample](./upsample.md)

## See Also

### Base Classes and Interfaces
- [class Module](./module.md)
  Base class for building neural networks with MLX.
- [protocol Quantizable](./quantizable.md)
  Protocol for layers that can be quantized
- [class ModuleInfo](./moduleinfo.md)
  ModuleInfo can provde information about child modules and act as an update point for [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md).
- [class ParameterInfo](./parameterinfo.md)
  ParameterInfo allows you to specify alternate keys for parameter propreties.
- [typealias ModuleParameters](./moduleparameters.md)
  `NestedDictionary` structure of `MLXArray`
- [typealias ModuleChildren](./modulechildren.md)
  `NestedDictionary` structure of `Module`
- [typealias ModuleItem](./moduleitem.md)
  Single item from [`items()`](./module/items%28%29.md)
- [typealias ModuleItems](./moduleitems.md)
  `NestedDictionary` structure of `ModuleValue` from [`items()`](./module/items%28%29.md)
- [enum ModuleValue](./modulevalue.md)
  A single value from [`Module`](./module.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/unarylayer)*