---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/fromfp8(_:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# fromFP8(_:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Convert an E4M3 FP8 array to the given floating-point [`DType`](./dtype.md).

## Declaration

```swift
func fromFP8(_ array: MLXArray, dtype: DType = .bfloat16, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The input array is interpreted as raw FP8 bytes.

##### See Also

- [`toFP8(_:stream:)`](./tofp8%28_,stream%29.md)
- [Conversion](./conversion.md)

## Parameters

- `array`: Input array containing E4M3 FP8 values
- `dtype`: Data type of the output array
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/fromfp8(_:dtype:stream:))*