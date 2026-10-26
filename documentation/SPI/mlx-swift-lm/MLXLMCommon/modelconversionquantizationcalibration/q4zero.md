---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionquantizationcalibration/q4zero"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionQuantizationCalibration.q4Zero

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Reproduce the `Q4_0` grid: symmetric, 32-element groups, scaled by the signed element of largest magnitude.

## Declaration

```swift
case q4Zero
```

#### Discussion

Use this for checkpoints whose weights were already trained against that grid. Re-deriving a grid from such weights discards the alignment they were trained for; reproducing it keeps them on their intended lattice.

Requires 4 bits, a group size of 32, and `QuantizationMode.affine`. Supplying a conflicting value throws [`ModelConversionError.incompatibleCalibration(_:_:)`](../modelconversionerror/incompatiblecalibration%28_,_%29.md) rather than silently overriding it.

Only `Linear` layers are calibrated. Other quantizable layers are still quantized to the same 4-bit/group-32 affine grid, but derive it the standard way, because `QuantizedEmbedding` has no initializer accepting precomputed scales and biases. The stored format is identical either way, so this affects accuracy, not loadability.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionquantizationcalibration/q4zero)*