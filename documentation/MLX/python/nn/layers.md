---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/layers.html
---

# Layers

**

- [.rst](../../_sources/python/nn/layers.rst)
- **

.pdf

**

# Layers

 Table of contents 

# Layers

| ALiBi() |  |
| --- | --- |
| AvgPool1d(kernel_size[, stride, padding]) | Applies 1-dimensional average pooling. |
| AvgPool2d(kernel_size[, stride, padding]) | Applies 2-dimensional average pooling. |
| AvgPool3d(kernel_size[, stride, padding]) | Applies 3-dimensional average pooling. |
| BatchNorm(num_features[, eps, momentum, ...]) | Applies Batch Normalization over a 2D or 3D input. |
| CELU([alpha]) | Applies the Continuously Differentiable Exponential Linear Unit. |
| Conv1d(in_channels, out_channels, kernel_size) | Applies a 1-dimensional convolution over the multi-channel input sequence. |
| Conv2d(in_channels, out_channels, kernel_size) | Applies a 2-dimensional convolution over the multi-channel input image. |
| Conv3d(in_channels, out_channels, kernel_size) | Applies a 3-dimensional convolution over the multi-channel input image. |
| ConvTranspose1d(in_channels, out_channels, ...) | Applies a 1-dimensional transposed convolution over the multi-channel input sequence. |
| ConvTranspose2d(in_channels, out_channels, ...) | Applies a 2-dimensional transposed convolution over the multi-channel input image. |
| ConvTranspose3d(in_channels, out_channels, ...) | Applies a 3-dimensional transposed convolution over the multi-channel input image. |
| Dropout([p]) | Randomly zero a portion of the elements during training. |
| Dropout2d([p]) | Apply 2D channel-wise dropout during training. |
| Dropout3d([p]) | Apply 3D channel-wise dropout during training. |
| Embedding(num_embeddings, dims) | Implements a simple lookup table that maps each input integer to a high-dimensional vector. |
| ELU([alpha]) | Applies the Exponential Linear Unit. |
| GELU([approx]) | Applies the Gaussian Error Linear Units. |
| GLU([axis]) | Applies the gated linear unit function. |
| GroupNorm(num_groups, dims[, eps, affine, ...]) | Applies Group Normalization [1] to the inputs. |
| GRU(input_size, hidden_size[, bias]) | A gated recurrent unit (GRU) RNN layer. |
| HardShrink() | Applies the HardShrink function. |
| HardTanh() | Applies the HardTanh function. |
| Hardswish() | Applies the hardswish function, element-wise. |
| InstanceNorm(dims[, eps, affine]) | Applies instance normalization [1] on the inputs. |
| LayerNorm(dims[, eps, affine, bias]) | Applies layer normalization [1] on the inputs. |
| LeakyReLU([negative_slope]) | Applies the Leaky Rectified Linear Unit. |
| Linear(input_dims, output_dims[, bias]) | Applies an affine transformation to the input. |
| LogSigmoid() | Applies the Log Sigmoid function. |
| LogSoftmax() | Applies the Log Softmax function. |
| LSTM(input_size, hidden_size[, bias]) | An LSTM recurrent layer. |
| MaxPool1d(kernel_size[, stride, padding]) | Applies 1-dimensional max pooling. |
| MaxPool2d(kernel_size[, stride, padding]) | Applies 2-dimensional max pooling. |
| MaxPool3d(kernel_size[, stride, padding]) | Applies 3-dimensional max pooling. |
| Mish() | Applies the Mish function, element-wise. |
| MultiHeadAttention(dims, num_heads[, ...]) | Implements the scaled dot product attention with multiple heads. |
| PReLU([num_parameters, init]) | Applies the element-wise parametric ReLU. |
| QuantizedEmbedding(num_embeddings, dims[, ...]) | The same asEmbeddingbut with a  quantized weight matrix. |
| QuantizedLinear(input_dims, output_dims[, ...]) | Applies an affine transformation to the input using a quantized weight matrix. |
| RMSNorm(dims[, eps]) | Applies Root Mean Square normalization [1] to the inputs. |
| ReLU() | Applies the Rectified Linear Unit. |
| ReLU2() | Applies the ReLU² activation function. |
| ReLU6() | Applies the Rectified Linear Unit 6. |
| RNN(input_size, hidden_size[, bias, ...]) | An Elman recurrent layer. |
| RoPE(dims[, traditional, base, scale]) | Implements the rotary positional encoding. |
| SELU() | Applies the Scaled Exponential Linear Unit. |
| Sequential(*modules) | A layer that calls the passed callables in order. |
| Sigmoid() | Applies the sigmoid function, element-wise. |
| SiLU() | Applies the Sigmoid Linear Unit. |
| SinusoidalPositionalEncoding(dims[, ...]) | Implements sinusoidal positional encoding. |
| Softmin() | Applies the Softmin function. |
| Softshrink([lambd]) | Applies the Softshrink function. |
| Softsign() | Applies the Softsign function. |
| Softmax() | Applies the Softmax function. |
| Softplus() | Applies the Softplus function. |
| Step([threshold]) | Applies the Step Activation Function. |
| Tanh() | Applies the hyperbolic tangent function. |
| Transformer(dims, num_heads, ...) | Implements a standard Transformer model. |
| Upsample(scale_factor[, mode, align_corners]) | Upsample the input signal spatially. |
