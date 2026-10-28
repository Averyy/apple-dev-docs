---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/linspace(_:_:count:endpoint:dtype:stream:)-2b6eu"
framework: "mlx-swift/MLX"
---

# linspace(_:_:count:endpoint:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate `count` evenly spaced numbers over interval `[start, stop]`.

## Declaration

```swift
func linspace<T>(_ start: T, _ stop: T, count: Int = 50, endpoint: Bool = true, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray where T : HasDType, T : BinaryInteger
```

## Discussion

The result is floating point (`float32` by default), matching python’s `mx.linspace`, even for integer bounds: evenly spaced values between two integers are generally not integers.  Pass `dtype:` for anything else:

```swift
// [0, 0.5, 1] as float32 -- *not* [0, 0, 1] as int64
let r = MLXArray.linspace(0, 1, count: 3)

// opt in to an integer (truncating) result
let i = MLXArray.linspace(0, 10, count: 6, dtype: .int32)
```

### See Also

- [Initialization](./initialization.md)
- [`linspace(_:_:count:endpoint:dtype:stream:)`](./linspace%28_,_,count,endpoint,dtype,stream%29-2b6eu.md)

## Parameters

- `start`: Start value
- `stop`: Stop value
- `count`: Number of samples
- `endpoint`: If `true` then the endpoint is the last sample, if `false` it is a half-open interval
- `dtype`: Dtype of the result, `float32` if not specified
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/linspace(_:_:count:endpoint:dtype:stream:)-2b6eu)*