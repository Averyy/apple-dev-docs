---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/triu(_:k:stream:)"
framework: "mlx-swift/MLX"
---

# triu(_:k:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Zeros the array below the given diagonal.

## Declaration

```swift
func triu(_ array: MLXArray, k: Int = 0, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

### See Also

- [`tril(_:k:stream:)`](./tril%28_,k,stream%29.md)

## Parameters

- `array`: Input array
- `k`: The diagonal of the 2-D array
- `stream`: Stream or device to evaluate on

## See Also

### Factory
- [func zeros(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./zeros%28_,type,stream%29.md)
  Construct an array of zeros.
- [func zeros(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./zeros%28like,dtype,stream%29.md)
  Construct an array of zeros.
- [func ones(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./ones%28_,type,stream%29.md)
  Construct an array of ones.
- [func ones(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./ones%28like,dtype,stream%29.md)
  Construct an array of ones.
- [func eye(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./eye%28_,m,k,type,stream%29.md)
  Create an identity matrix or a general diagonal matrix.
- [func full(some Collection<Int>, values: some ScalarOrArray, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./full%28_,values,type,stream%29.md)
  Construct an array with the given value.
- [func full(some Collection<Int>, values: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./full%28_,values,stream%29.md)
  Construct an array with the given value.
- [func identity(Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./identity%28_,type,stream%29.md)
  Create a square identity matrix.
- [func linspace<T>(T, T, count: Int, endpoint: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./linspace%28_,_,count,endpoint,dtype,stream%29-2b6eu.md)
  Generate `count` evenly spaced numbers over interval `[start, stop]`.
- [func linspace<T>(T, T, count: Int, endpoint: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./linspace%28_,_,count,endpoint,dtype,stream%29-8k1d2.md)
  Generate `count` evenly spaced numbers over interval `[start, stop]`.
- [func repeated(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./repeated%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [func repeated(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./repeated%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [func `repeat`(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./repeat%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [func `repeat`(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./repeat%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [func tri(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./tri%28_,m,k,type,stream%29.md)
  An array with ones at and below the given diagonal and zeros elsewhere.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/triu(_:k:stream:))*