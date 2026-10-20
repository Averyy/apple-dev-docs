---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/layers.html
---

# Layers

| [ALiBi](_autosummary/mlx.nn.ALiBi.md#mlx.nn.ALiBi)() | Implements Attention with Linear Biases (ALiBi). |
| --- | --- |
| [AllToShardedLinear](_autosummary/mlx.nn.AllToShardedLinear.md#mlx.nn.AllToShardedLinear)(input_dims, output_dims) | Each member of the group applies part of the affine transformation such that the result is sharded across the group. |
| [AvgPool1d](_autosummary/mlx.nn.AvgPool1d.md#mlx.nn.AvgPool1d)(kernel_size[, stride, padding]) | Applies 1-dimensional average pooling. |
| [AvgPool2d](_autosummary/mlx.nn.AvgPool2d.md#mlx.nn.AvgPool2d)(kernel_size[, stride, padding]) | Applies 2-dimensional average pooling. |
| [AvgPool3d](_autosummary/mlx.nn.AvgPool3d.md#mlx.nn.AvgPool3d)(kernel_size[, stride, padding]) | Applies 3-dimensional average pooling. |
| [BatchNorm](_autosummary/mlx.nn.BatchNorm.md#mlx.nn.BatchNorm)(num_features[, eps, momentum, ...]) | Applies Batch Normalization over a 2D, 3D or 4D input. |
| [Bilinear](_autosummary/mlx.nn.Bilinear.md#mlx.nn.Bilinear)(input1_dims, input2_dims, output_dims) | Applies a bilinear transformation to the inputs. |
| [CELU](_autosummary/mlx.nn.CELU.md#mlx.nn.CELU)([alpha]) | Applies the Continuously Differentiable Exponential Linear Unit. |
| [Conv1d](_autosummary/mlx.nn.Conv1d.md#mlx.nn.Conv1d)(in_channels, out_channels, kernel_size) | Applies a 1-dimensional convolution over the multi-channel input sequence. |
| [Conv2d](_autosummary/mlx.nn.Conv2d.md#mlx.nn.Conv2d)(in_channels, out_channels, kernel_size) | Applies a 2-dimensional convolution over the multi-channel input image. |
| [Conv3d](_autosummary/mlx.nn.Conv3d.md#mlx.nn.Conv3d)(in_channels, out_channels, kernel_size) | Applies a 3-dimensional convolution over the multi-channel input image. |
| [ConvTranspose1d](_autosummary/mlx.nn.ConvTranspose1d.md#mlx.nn.ConvTranspose1d)(in_channels, out_channels, ...) | Applies a 1-dimensional transposed convolution over the multi-channel input sequence. |
| [ConvTranspose2d](_autosummary/mlx.nn.ConvTranspose2d.md#mlx.nn.ConvTranspose2d)(in_channels, out_channels, ...) | Applies a 2-dimensional transposed convolution over the multi-channel input image. |
| [ConvTranspose3d](_autosummary/mlx.nn.ConvTranspose3d.md#mlx.nn.ConvTranspose3d)(in_channels, out_channels, ...) | Applies a 3-dimensional transposed convolution over the multi-channel input image. |
| [Dropout](_autosummary/mlx.nn.Dropout.md#mlx.nn.Dropout)([p]) | Randomly zero a portion of the elements during training. |
| [Dropout2d](_autosummary/mlx.nn.Dropout2d.md#mlx.nn.Dropout2d)([p]) | Apply 2D channel-wise dropout during training. |
| [Dropout3d](_autosummary/mlx.nn.Dropout3d.md#mlx.nn.Dropout3d)([p]) | Apply 3D channel-wise dropout during training. |
| [Embedding](_autosummary/mlx.nn.Embedding.md#mlx.nn.Embedding)(num_embeddings, dims) | Implements a simple lookup table that maps each input integer to a high-dimensional vector. |
| [ELU](_autosummary/mlx.nn.ELU.md#mlx.nn.ELU)([alpha]) | Applies the Exponential Linear Unit. |
| [GELU](_autosummary/mlx.nn.GELU.md#mlx.nn.GELU)([approx]) | Applies the Gaussian Error Linear Units. |
| [GLU](_autosummary/mlx.nn.GLU.md#mlx.nn.GLU)([axis]) | Applies the gated linear unit function. |
| [GroupNorm](_autosummary/mlx.nn.GroupNorm.md#mlx.nn.GroupNorm)(num_groups, dims[, eps, affine, ...]) | Applies Group Normalization [1] to the inputs. |
| [GRU](_autosummary/mlx.nn.GRU.md#mlx.nn.GRU)(input_size, hidden_size[, bias]) | A gated recurrent unit (GRU) RNN layer. |
| [HardShrink](_autosummary/mlx.nn.HardShrink.md#mlx.nn.HardShrink)([lambd]) | Applies the HardShrink function. |
| [HardTanh](_autosummary/mlx.nn.HardTanh.md#mlx.nn.HardTanh)() | Applies the HardTanh function. |
| [Hardswish](_autosummary/mlx.nn.Hardswish.md#mlx.nn.Hardswish)() | Applies the hardswish function, element-wise. |
| [Identity](_autosummary/mlx.nn.Identity.md#mlx.nn.Identity)(*args, **kwargs) | A placeholder identity operator that is argument-insensitive. |
| [InstanceNorm](_autosummary/mlx.nn.InstanceNorm.md#mlx.nn.InstanceNorm)(dims[, eps, affine]) | Applies instance normalization [1] on the inputs. |
| [LayerNorm](_autosummary/mlx.nn.LayerNorm.md#mlx.nn.LayerNorm)(dims[, eps, affine, bias]) | Applies layer normalization [1] on the inputs. |
| [LeakyReLU](_autosummary/mlx.nn.LeakyReLU.md#mlx.nn.LeakyReLU)([negative_slope]) | Applies the Leaky Rectified Linear Unit. |
| [Linear](_autosummary/mlx.nn.Linear.md#mlx.nn.Linear)(input_dims, output_dims[, bias]) | Applies an affine transformation to the input. |
| [LogSigmoid](_autosummary/mlx.nn.LogSigmoid.md#mlx.nn.LogSigmoid)() | Applies the Log Sigmoid function. |
| [LogSoftmax](_autosummary/mlx.nn.LogSoftmax.md#mlx.nn.LogSoftmax)() | Applies the Log Softmax function. |
| [LSTM](_autosummary/mlx.nn.LSTM.md#mlx.nn.LSTM)(input_size, hidden_size[, bias]) | An LSTM recurrent layer. |
| [MaxPool1d](_autosummary/mlx.nn.MaxPool1d.md#mlx.nn.MaxPool1d)(kernel_size[, stride, padding]) | Applies 1-dimensional max pooling. |
| [MaxPool2d](_autosummary/mlx.nn.MaxPool2d.md#mlx.nn.MaxPool2d)(kernel_size[, stride, padding]) | Applies 2-dimensional max pooling. |
| [MaxPool3d](_autosummary/mlx.nn.MaxPool3d.md#mlx.nn.MaxPool3d)(kernel_size[, stride, padding]) | Applies 3-dimensional max pooling. |
| [Mish](_autosummary/mlx.nn.Mish.md#mlx.nn.Mish)() | Applies the Mish function, element-wise. |
| [MultiHeadAttention](_autosummary/mlx.nn.MultiHeadAttention.md#mlx.nn.MultiHeadAttention)(dims, num_heads[, ...]) | Implements the scaled dot product attention with multiple heads. |
| [PReLU](_autosummary/mlx.nn.PReLU.md#mlx.nn.PReLU)([num_parameters, init]) | Applies the element-wise parametric ReLU. |
| [QQLinear](_autosummary/mlx.nn.QQLinear.md#mlx.nn.QQLinear)(input_dims, output_dims[, ...]) | Quantizes the input and applies an affine transformation using quantized weights. |
| [QuantizedAllToShardedLinear](_autosummary/mlx.nn.QuantizedAllToShardedLinear.md#mlx.nn.QuantizedAllToShardedLinear)(input_dims, ...) | Each member of the group applies part of the affine transformation with a quantized matrix such that the result is sharded across the group. |
| [QuantizedEmbedding](_autosummary/mlx.nn.QuantizedEmbedding.md#mlx.nn.QuantizedEmbedding)(num_embeddings, dims[, ...]) | The same as [Embedding](_autosummary/mlx.nn.Embedding.md#mlx.nn.Embedding) but with a quantized weight matrix. |
| [QuantizedLinear](_autosummary/mlx.nn.QuantizedLinear.md#mlx.nn.QuantizedLinear)(input_dims, output_dims[, ...]) | Applies an affine transformation to the input using a quantized weight matrix. |
| [QuantizedShardedToAllLinear](_autosummary/mlx.nn.QuantizedShardedToAllLinear.md#mlx.nn.QuantizedShardedToAllLinear)(input_dims, ...) | Each member of the group applies part of the affine transformation using the quantized matrix and then aggregates the results. |
| [RMSNorm](_autosummary/mlx.nn.RMSNorm.md#mlx.nn.RMSNorm)(dims[, eps]) | Applies Root Mean Square normalization [1] to the inputs. |
| [ReLU](_autosummary/mlx.nn.ReLU.md#mlx.nn.ReLU)() | Applies the Rectified Linear Unit. |
| [ReLU2](_autosummary/mlx.nn.ReLU2.md#mlx.nn.ReLU2)() | Applies the ReLU² activation function. |
| [ReLU6](_autosummary/mlx.nn.ReLU6.md#mlx.nn.ReLU6)() | Applies the Rectified Linear Unit 6. |
| [RNN](_autosummary/mlx.nn.RNN.md#mlx.nn.RNN)(input_size, hidden_size[, bias, ...]) | An Elman recurrent layer. |
| [RoPE](_autosummary/mlx.nn.RoPE.md#mlx.nn.RoPE)(dims[, traditional, base, scale]) | Implements the rotary positional encoding. |
| [SELU](_autosummary/mlx.nn.SELU.md#mlx.nn.SELU)() | Applies the Scaled Exponential Linear Unit. |
| [Sequential](_autosummary/mlx.nn.Sequential.md#mlx.nn.Sequential)(*modules) | A layer that calls the passed callables in order. |
| [ShardedToAllLinear](_autosummary/mlx.nn.ShardedToAllLinear.md#mlx.nn.ShardedToAllLinear)(input_dims, output_dims) | Each member of the group applies part of the affine transformation and then aggregates the results. |
| [Sigmoid](_autosummary/mlx.nn.Sigmoid.md#mlx.nn.Sigmoid)() | Applies the sigmoid function, element-wise. |
| [SiLU](_autosummary/mlx.nn.SiLU.md#mlx.nn.SiLU)() | Applies the Sigmoid Linear Unit. |
| [SinusoidalPositionalEncoding](_autosummary/mlx.nn.SinusoidalPositionalEncoding.md#mlx.nn.SinusoidalPositionalEncoding)(dims[, ...]) | Implements sinusoidal positional encoding. |
| [Softmin](_autosummary/mlx.nn.Softmin.md#mlx.nn.Softmin)() | Applies the Softmin function. |
| [Softshrink](_autosummary/mlx.nn.Softshrink.md#mlx.nn.Softshrink)([lambd]) | Applies the Softshrink function. |
| [Softsign](_autosummary/mlx.nn.Softsign.md#mlx.nn.Softsign)() | Applies the Softsign function. |
| [Softmax](_autosummary/mlx.nn.Softmax.md#mlx.nn.Softmax)() | Applies the Softmax function. |
| [Softplus](_autosummary/mlx.nn.Softplus.md#mlx.nn.Softplus)() | Applies the Softplus function. |
| [Step](_autosummary/mlx.nn.Step.md#mlx.nn.Step)([threshold]) | Applies the Step Activation Function. |
| [Tanh](_autosummary/mlx.nn.Tanh.md#mlx.nn.Tanh)() | Applies the hyperbolic tangent function. |
| [Transformer](_autosummary/mlx.nn.Transformer.md#mlx.nn.Transformer)(dims, num_heads, ...) | Implements a standard Transformer model. |
| [TransformerDecoder](_autosummary/mlx.nn.TransformerDecoder.md#mlx.nn.TransformerDecoder)(num_layers, dims, ...[, ...]) |  |
| [TransformerDecoderLayer](_autosummary/mlx.nn.TransformerDecoderLayer.md#mlx.nn.TransformerDecoderLayer)(dims, num_heads, ...) |  |
| [TransformerEncoder](_autosummary/mlx.nn.TransformerEncoder.md#mlx.nn.TransformerEncoder)(num_layers, dims, ...[, ...]) |  |
| [TransformerEncoderLayer](_autosummary/mlx.nn.TransformerEncoderLayer.md#mlx.nn.TransformerEncoderLayer)(dims, num_heads, ...) |  |
| [Upsample](_autosummary/mlx.nn.Upsample.md#mlx.nn.Upsample)(scale_factor[, mode, ...]) | Upsample the input signal spatially. |
