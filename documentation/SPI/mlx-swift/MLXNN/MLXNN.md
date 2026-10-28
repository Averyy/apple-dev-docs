---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn"
framework: "mlx-swift/MLXNN"
---

# MLXNN

**Framework**: mlx-swift/MLXNN  
**Kind**: module  
**Role**: Framework

Neural Networks support for MLX

## Mentions

- [Creating Modules](./custom-layers.md)

## Overview

Writing arbitrarily complex neural networks in MLX can be done using only `MLXArray` and `valueAndGrad()`. However, this requires the user to write again and again the same simple neural network operations as well as handle all the parameter state and initialization manually and explicitly.

The `MLXNN` package solves this problem by providing an intuitive way of composing neural network layers, initializing their parameters, freezing them for finetuning and more.

## Modules

The workhorse of any neural network library is the [`Module`](./module.md) class. In MLX the [`Module`](./module.md) class is a container of `MLXArray` or [`Module`](./module.md) instances. Its main function is to provide a way to recursively access and update its parameters and those of its submodules.

- [`Module`](./module.md)
- [Creating Modules](./custom-layers.md)

### Parameters

A parameter of a module is any member of type `MLXArray` (its name should not start with `_`). It can be nested in other [`Module`](./module.md) instances or `Array` and `Dictionary`.

[`parameters()`](./module/parameters%28%29.md) can be used to extract a `NestedDictionary` ([`ModuleParameters`](./moduleparameters.md)) with all the parameters of a module and its submodules.

A Module can also keep track of “frozen” parameters. See the [`freeze(recursive:keys:strict:)`](./module/freeze%28recursive,keys,strict%29.md) method for more details. [`valueAndGrad(model:_:)`](./valueandgrad%28model,_%29-12a2c.md) the gradients returned will be with respect to these trainable parameters.

### Training

See [Training a Model](./training.md)

## Other MLX Packages

- [MLX](../MLX/MLX.md)
- [MLXOptimizers](../MLXOptimizers/MLXOptimizers.md)
- [Python mlx](https://ml-explore.github.io/mlx/build/html/index.html)

## Topics

### Articles
- [Creating Modules](./custom-layers.md)
  Creating custom modules using `MLXNN`.
- [Training a Model](./training.md)
  A model training loop.
### Base Classes and Interfaces
- [class Module](./module.md)
  Base class for building neural networks with MLX.
- [protocol UnaryLayer](./unarylayer.md)
  A `Layer` ([`Module`](./module.md) subclass) that can be evaluated as a *unary function*.
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
### Unary Layers
- [class AvgPool1d](./avgpool1d.md)
  Applies 1-dimensional average pooling.
- [class AvgPool2d](./avgpool2d.md)
  Applies 2-dimensional average pooling.
- [class Conv1d](./conv1d.md)
  Applies a 1-dimensional convolution over the multi-channel input sequence.
- [class Conv2d](./conv2d.md)
  Applies a 2-dimensional convolution over the multi-channel input image.
- [class Dropout](./dropout.md)
  Randomly zero a portion of the elements during training.
- [class Dropout2d](./dropout2d.md)
  Apply 2D channel-wise dropout during training.
- [class Dropout3d](./dropout3d.md)
  Apply 3D channel-wise dropout during training.
- [class Embedding](./embedding.md)
  Implements a simple lookup table that maps each input integer to a high-dimensional vector.
- [class Identity](./identity.md)
  A placeholder identity operator that is argument-insensitive.
- [class Linear](./linear.md)
  Applies an affine transformation to the input.
- [class MaxPool1d](./maxpool1d.md)
  Applies 1-dimensional max pooling.
- [class MaxPool2d](./maxpool2d.md)
  Applies 2-dimensional max pooling.
- [class QuantizedLinear](./quantizedlinear.md)
  Applies an affine transformation to the input using a quantized weight matrix.
- [class RoPE](./rope.md)
  Implements the rotary positional encoding.
- [class RMSNorm](./rmsnorm.md)
  Applies Root Mean Square normalization [1] to the inputs.
- [class Sequential](./sequential.md)
  A layer that calls the passed [`UnaryLayer`](./unarylayer.md) in order.
### Sampling
- [class Upsample](./upsample.md)
  Upsample the input signal spatially.
### Recurrent
- [class RNN](./rnn.md)
  An Elman recurrent layer.
- [class GRU](./gru.md)
  A gated recurrent unit (GRU) RNN layer.
- [class LSTM](./lstm.md)
  An LSTM recurrent layer.
### Other Layers
- [class Bilinear](./bilinear.md)
  Applies a bilinear transformation to the inputs.
- [class MultiHeadAttention](./multiheadattention.md)
  Implements the scaled dot product attention with multiple heads.
### Activation Free Functions
- [func celu(MLXArray, alpha: Float) -> MLXArray](./celu%28_,alpha%29.md)
  Applies the Continuously Differentiable Exponential Linear Unit.
- [func elu(MLXArray, alpha: Float) -> MLXArray](./elu%28_,alpha%29.md)
  Applies the Exponential Linear Unit.
- [func gelu(MLXArray) -> MLXArray](./gelu%28_%29.md)
  Applies the Gaussian Error Linear Units function.
- [func geluApproximate(MLXArray) -> MLXArray](./geluapproximate%28_%29.md)
  An approximation to Gaussian Error Linear Unit.
- [func geluFastApproximate(MLXArray) -> MLXArray](./gelufastapproximate%28_%29.md)
  A fast approximation to Gaussian Error Linear Unit.
- [func glu(MLXArray, axis: Int) -> MLXArray](./glu%28_,axis%29.md)
  Applies the gated linear unit function.
- [func hardSwish(MLXArray) -> MLXArray](./hardswish%28_%29.md)
  Applies the hardswish function, element-wise
- [func leakyRelu(MLXArray, negativeSlope: Float) -> MLXArray](./leakyrelu%28_,negativeslope%29.md)
  Applies the Leaky Rectified Linear Unit.
- [func logSigmoid(MLXArray) -> MLXArray](./logsigmoid%28_%29.md)
  Applies the Log Sigmoid function.
- [func logSoftmax(MLXArray, axis: Int) -> MLXArray](./logsoftmax%28_,axis%29.md)
  Applies the Log Softmax function.
- [func mish(MLXArray) -> MLXArray](./mish%28_%29.md)
  Applies the Mish function, element-wise.
- [func prelu(MLXArray, alpha: MLXArray) -> MLXArray](./prelu%28_,alpha%29.md)
  Applies the element-wise parametric ReLU.
- [func relu(MLXArray) -> MLXArray](./relu%28_%29.md)
  Applies the Rectified Linear Unit.
- [func relu6(MLXArray) -> MLXArray](./relu6%28_%29.md)
  Applies the Rectified Linear Unit 6.
- [func reluSquared(MLXArray) -> MLXArray](./relusquared%28_%29.md)
  Applies the squared Rectified Linear Unit.
- [func selu(MLXArray) -> MLXArray](./selu%28_%29.md)
  Applies the Scaled Exponential Linear Unit.
- [func silu(MLXArray) -> MLXArray](./silu%28_%29.md)
  Applies the Sigmoid Linear Unit. Also known as Swish.
- [func sigmoid(MLXArray) -> MLXArray](./sigmoid%28_%29.md)
  Applies the element-wise logistic sigmoid.
- [func softplus(MLXArray) -> MLXArray](./softplus%28_%29.md)
  Applies the Softplus function.
- [func softsign(MLXArray) -> MLXArray](./softsign%28_%29.md)
  Applies the Softsign function.
- [func step(MLXArray, threshold: Float) -> MLXArray](./step%28_,threshold%29.md)
  Applies the Step Activation Function.
### Activation Modules
- [class CELU](./celu.md)
  Applies the Continuously Differentiable Exponential Linear Unit.
- [class GELU](./gelu.md)
  Applies the Gaussian Error Linear Units function.
- [class GLU](./glu.md)
  Applies the gated linear unit function.
- [class HardSwish](./hardswish.md)
  Applies the hardswish function, element-wise
- [class LeakyReLU](./leakyrelu.md)
  Applies the Leaky Rectified Linear Unit.
- [class LogSigmoid](./logsigmoid.md)
  Applies the Log Sigmoid function.
- [class LogSoftmax](./logsoftmax.md)
  Applies the Log Softmax function.
- [class Mish](./mish.md)
  Applies the Mish function, element-wise.
- [class PReLU](./prelu.md)
  Applies the element-wise parametric ReLU.
- [class ReLU](./relu.md)
  Applies the Rectified Linear Unit.
- [class ReLU6](./relu6.md)
  Applies the Rectified Linear Unit 6.
- [class ReLUSquared](./relusquared.md)
  Applies the squared Rectified Linear Unit.
- [class SELU](./selu.md)
  Applies the Scaled Exponential Linear Unit.
- [class SiLU](./silu.md)
  Applies the Sigmoid Linear Unit. Also known as Swish.
- [class Sigmoid](./sigmoid.md)
  Applies the element-wise logistic sigmoid.
- [class Softmax](./softmax.md)
  Applies the Softmax function.
- [class Softplus](./softplus.md)
  Applies the Softplus function.
- [class Softsign](./softsign.md)
  Applies the Softsign function.
- [class Step](./step.md)
  Applies the Step Activation Function.
- [class Tanh](./tanh.md)
  Applies the hyperbolic tangent function
### Loss Functions
- [func binaryCrossEntropy(logits: MLXArray, targets: MLXArray, weights: MLXArray?, withLogits: Bool, reduction: LossReduction) -> MLXArray](./binarycrossentropy%28logits,targets,weights,withlogits,reduction%29.md)
  Computes the binary cross entropy loss.
- [func cosineSimilarityLoss(x1: MLXArray, x2: MLXArray, axis: Int, eps: Float, reduction: LossReduction) -> MLXArray](./cosinesimilarityloss%28x1,x2,axis,eps,reduction%29.md)
  Computes the cosine similarity between the two inputs.
- [func crossEntropy(logits: MLXArray, targets: MLXArray, weights: MLXArray?, axis: Int, labelSmoothing: Float, reduction: LossReduction) -> MLXArray](./crossentropy%28logits,targets,weights,axis,labelsmoothing,reduction%29.md)
  Computes the cross entropy loss.
- [func hingeLoss(inputs: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./hingeloss%28inputs,targets,reduction%29.md)
  Computes the hinge loss between inputs and targets.
- [func huberLoss(inputs: MLXArray, targets: MLXArray, delta: Float, reduction: LossReduction) -> MLXArray](./huberloss%28inputs,targets,delta,reduction%29.md)
  Computes the Huber loss between inputs and targets.
- [func klDivLoss(inputs: MLXArray, targets: MLXArray, axis: Int, reduction: LossReduction) -> MLXArray](./kldivloss%28inputs,targets,axis,reduction%29.md)
  Computes the Kullback-Leibler divergence loss.
- [func l1Loss(predictions: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./l1loss%28predictions,targets,reduction%29.md)
  Computes the L1 loss
- [func logCoshLoss(inputs: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./logcoshloss%28inputs,targets,reduction%29.md)
  Computes the log cosh loss between inputs and targets.
- [func mseLoss(predictions: MLXArray, targets: MLXArray, reduction: LossReduction) -> MLXArray](./mseloss%28predictions,targets,reduction%29.md)
  Computes the mean squared error loss.
- [func nllLoss(inputs: MLXArray, targets: MLXArray, axis: Int, reduction: LossReduction) -> MLXArray](./nllloss%28inputs,targets,axis,reduction%29.md)
  Computes the negative log likelihood loss.
- [func smoothL1Loss(predictions: MLXArray, targets: MLXArray, beta: Float, reduction: LossReduction) -> MLXArray](./smoothl1loss%28predictions,targets,beta,reduction%29.md)
  Computes the smooth L1 loss.
- [func tripletLoss(anchors: MLXArray, positives: MLXArray, negatives: MLXArray, axis: Int, p: Int, margin: Float, eps: Float, reduction: LossReduction) -> MLXArray](./tripletloss%28anchors,positives,negatives,axis,p,margin,eps,reduction%29.md)
  Computes the triplet loss for a set of anchor, positive, and negative samples. Margin is represented with alpha in the math section.
### Normalization Layers
- [class InstanceNorm](./instancenorm.md)
  Applies instance normalization [1] on the inputs.
- [class LayerNorm](./layernorm.md)
  Applies layer normalization [1] on the inputs.
- [class RMSNorm](./rmsnorm.md)
  Applies Root Mean Square normalization [1] to the inputs.
- [class GroupNorm](./groupnorm.md)
  Applies Group Normalization [1] on the inputs.
- [class BatchNorm](./batchnorm.md)
  Applies batch normalization [1] on the inputs.
### Positional Encoding Layers
- [class RoPE](./rope.md)
  Implements the rotary positional encoding.
- [class SinusoidalPositionalEncoding](./sinusoidalpositionalencoding.md)
  Implements sinusoidal positional encoding.
- [class ALiBi](./alibi.md)
### Transformer Layers
- [class MultiHeadAttention](./multiheadattention.md)
  Implements the scaled dot product attention with multiple heads.
- [class Transformer](./transformer.md)
  Implements a standard Transformer model.
### Value and Grad
- [func valueAndGrad<Model>(model: Model, (Model, MLXArray, MLXArray) -> MLXArray) -> (Model, MLXArray, MLXArray) -> (MLXArray, ModuleParameters)](./valueandgrad%28model,_%29-12a2c.md)
  Transform the passed function `f(Model, MLXArray, MLXArray)` to a function that computes the gradients of `f` with regard to the model’s trainable parameters and also its value.
- [func valueAndGrad<Model>(model: Model, (Model, [MLXArray]) -> [MLXArray]) -> (Model, [MLXArray]) -> ([MLXArray], ModuleParameters)](./valueandgrad%28model,_%29-548r7.md)
  Variant of `valueAndGrad(model:_:)` that can be used to pass an arbitrary number of `MLXArray` to a loss function.
- [func valueAndGrad<Model, Arguments>(model: Model, (Model, Arguments) -> [MLXArray]) -> (Model, Arguments) -> ([MLXArray], ModuleParameters)](./valueandgrad%28model,_%29-45dg5.md)
  Variant of `valueAndGrad(model:_:)` that can be used to pass an arbitrary parameters to a loss function.
### Articles
- [Activation Functions and Layers](./activations.md)
  Built-in activation functions and layers.
- [Layers](./layers.md)
  Built-in layers.
- [Loss Functions](./losses.md)
  Built-in loss functions
- [Normalization](./normalization.md)
  Built-in normalization layers
- [Positional Encoding](./positional-encoding.md)
  Built-in layers for positional encoding.
- [Transformer](./transformers.md)
  Built-in transformer layers
### Classes
- [class AllToShardedLinear](./alltoshardedlinear.md)
  Each member of the group applies part of the affine transformation so that the result is sharded across the group.
- [class AvgPool3d](./avgpool3d.md)
  Applies 3-dimensional average pooling.
- [class MaxPool3d](./maxpool3d.md)
  Applies 3-dimensional max pooling.
- [class Pool](./pool.md)
  Abstract pooling layer.
- [class QuantizedAllToShardedLinear](./quantizedalltoshardedlinear.md)
  The quantized flavor of [`AllToShardedLinear`](./alltoshardedlinear.md).
- [class QuantizedEmbedding](./quantizedembedding.md)
  The same as [`Embedding`](./embedding.md) but with a quantized weight matrix.
- [class QuantizedShardedToAllLinear](./quantizedshardedtoalllinear.md)
  The quantized flavor of [`ShardedToAllLinear`](./shardedtoalllinear.md).
- [class ShardedToAllLinear](./shardedtoalllinear.md)
  Each member of the group applies part of the affine transformation and the results are then aggregated.
### Protocols
- [protocol ArrayOffsetLayer](./arrayoffsetlayer.md)
  A layer ([`Module`](./module.md) subclass) that can be evaluated with an input array and a per-example position offset.
- [protocol OffsetLayer](./offsetlayer.md)
  A `Layer`  ([`Module`](./module.md) subclass) that can be evaluated with an array and offset.
- [protocol Quantized](./quantized.md)
  Protocol for layers that are quantized.
### Structures
- [struct SequentialBuilder](./sequentialbuilder.md)
  A way to build [`Sequential`](./sequential.md).
### Functions
- [func averageGradients(ModuleParameters, group: MLXDistributed.Group?, allReduceSize: Int, stream: StreamOrDevice) throws -> ModuleParameters](./averagegradients%28_,group,allreducesize,stream%29.md)
  Average the gradients across the processes in the group.
- [func clipGradNormSharded(gradients: ModuleParameters, maxNorm: Float, group: MLXDistributed.Group?, stream: StreamOrDevice) throws -> (ModuleParameters, MLXArray)](./clipgradnormsharded%28gradients,maxnorm,group,stream%29.md)
  Clip the global norm of gradients that are sharded across a group.
- [func quantize(model: Module, filter: (String, Module) -> (groupSize: Int, bits: Int, mode: QuantizationMode)?, apply: (Module, Int, Int, QuantizationMode) -> Module?)](./quantize%28model,filter,apply%29-3yqd1.md)
  Quantize the sub-modules of a module according to a filter.
- [func quantize(model: Module, filter: (String, Module) -> (groupSize: Int, bits: Int)?, apply: (Module, Int, Int) -> Module?)](./quantize%28model,filter,apply%29-9dc23.md)
- [func quantize(model: Module, groupSize: Int, bits: Int, filter: (String, Module) -> Bool, apply: (Module, Int, Int) -> Module?)](./quantize%28model,groupsize,bits,filter,apply%29.md)
- [func quantize(model: Module, groupSize: Int, bits: Int, mode: QuantizationMode, filter: (String, Module) -> Bool, apply: (Module, Int, Int, QuantizationMode) -> Module?)](./quantize%28model,groupsize,bits,mode,filter,apply%29.md)
  Quantize the sub-modules of a module according to a filter.
- [func quantizeSingle(layer: Module, groupSize: Int, bits: Int, mode: QuantizationMode) -> (any Quantized)?](./quantizesingle%28layer,groupsize,bits,mode%29.md)
  Quantize any [`Quantizable`](./quantizable.md) layer that is not already quantized.
- [func shardInPlace(Module, predicate: (String, MLXArray) -> (axis: Int, segments: Segments)?, group: MLXDistributed.Group?) throws](./shardinplace%28_,predicate,group%29.md)
  Shard a module in place, choosing how each parameter is split.
- [func shardInPlace(Module, sharding: ShardingType, segments: Segments, group: MLXDistributed.Group?) throws](./shardinplace%28_,sharding,segments,group%29.md)
  Shard a module in place by replacing its parameters with sharded ones.
- [func shardLinear(Linear, sharding: ShardingType, segments: Segments, group: MLXDistributed.Group?) throws -> Linear](./shardlinear%28_,sharding,segments,group%29.md)
  Create a new linear layer with sharded parameters that also performs the distributed communication, either in the forward or the backward pass.
- [func sumGradients(group: MLXDistributed.Group) -> (MLXArray) -> MLXArray](./sumgradients%28group%29.md)
  Returns a function that is the identity in the forward pass and sums the gradients across the group in the backward pass.
### Type Aliases
- [typealias ShardingPredicate](./shardingpredicate.md)
  The sharding axis and segments for a parameter, or `nil` to leave it alone.
### Enumerations
- [enum LossReduction](./lossreduction.md)
  Different types of loss reductions
- [enum Segments](./segments.md)
  Describes how an unsharded weight is composed.
- [enum ShardingError](./shardingerror.md)
  A layer cannot be sharded across a group.
- [enum ShardingType](./shardingtype.md)
  How a linear layer is sharded across a group.
- [enum UpdateError](./updateerror.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn)*