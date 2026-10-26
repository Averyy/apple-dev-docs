---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizationmode/affine"
framework: "mlx-swift/MLX"
---

# QuantizationMode.affine

**Framework**: mlx-swift/MLX  
**Kind**: case  
**Role**: Case

Affine (linear) quantization with scale and bias parameters.

## Declaration

```swift
case affine
```

#### Discussion

This is the standard quantization approach where values are quantized using:

```
quantized_value = round((value - bias) / scale)
dequantized_value = quantized_value * scale + bias
```

The `scale` and `bias` parameters are computed per group of elements (typically 32 or 64 elements) to minimize quantization error. This mode provides good compression with reasonable accuracy preservation for most neural network weights.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizationmode/affine)*