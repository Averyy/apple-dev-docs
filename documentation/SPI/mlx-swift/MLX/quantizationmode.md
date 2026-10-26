---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizationmode"
framework: "mlx-swift/MLX"
---

# QuantizationMode

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Quantization modes for weight compression in neural networks.

## Declaration

```swift
enum QuantizationMode
```

#### Overview

Quantization reduces the precision of model weights to decrease memory usage and potentially improve inference speed. Different modes use different strategies for mapping full-precision values to lower-precision representations.

## Topics

### Enumeration Cases
- [QuantizationMode.affine](./quantizationmode/affine.md)
  Affine (linear) quantization with scale and bias parameters.
- [QuantizationMode.mxfp4](./quantizationmode/mxfp4.md)
  MX (Microscaling) FP4 quantization format.
- [QuantizationMode.mxfp8](./quantizationmode/mxfp8.md)
  MX (Microscaling) FP8 quantization format.
- [QuantizationMode.nvfp4](./quantizationmode/nvfp4.md)
### Initializers
- [init?(rawValue: String)](./quantizationmode/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./quantizationmode/equatable-implementations.md)
- [RawRepresentable Implementations](./quantizationmode/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/quantizationmode)*