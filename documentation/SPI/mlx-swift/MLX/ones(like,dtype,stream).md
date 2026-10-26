---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/ones(like:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# ones(like:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Construct an array of ones.

## Declaration

```swift
func ones(like array: MLXArray, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Example:

```swift
let array = MLXArray(0 ..< 12, [4, 3])
let r = MLXArray.ones(like: array)
```

##### See Also

- [Initialization](./initialization.md)
- [`ones(_:type:stream:)`](./ones%28_,type,stream%29.md)
- [`zeros(_:type:stream:)`](./zeros%28_,type,stream%29.md)

## Parameters

- `array`: Array to copy shape and dtype from
- `dtype`: Optional type to produce the result in, otherwise use array’s dtype
- `stream`: Stream or device to evaluate on

## See Also

### Factory
- [func zeros(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./zeros%28_,type,stream%29.md)
  Construct an array of zeros.
- [func zeros(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./zeros%28like,dtype,stream%29.md)
  Construct an array of zeros.
- [func ones(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./ones%28_,type,stream%29.md)
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
- [func tril(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./tril%28_,k,stream%29.md)
  Zeros the array above the given diagonal.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/ones(like:dtype:stream:))*