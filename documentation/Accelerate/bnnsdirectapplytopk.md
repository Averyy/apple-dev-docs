# BNNSDirectApplyTopK(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a top-k filter directly to an input.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSDirectApplyTopK(_ K: Int, _ axis: Int, _ batch_size: Int, _ input: UnsafePointer<BNNSNDArrayDescriptor>, _ input_batch_stride: Int, _ best_values: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ best_values_batch_stride: Int, _ best_indices: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ best_indices_batch_stride: Int, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

> ❗ **Important**:  In Swift, the input data type and best values data type must be `float`, and the best indices data type must be `int32`.

Use this function to find the maximum values and corresponding indices of a tensor along a specified axis.

For example, given the following 4 x 4 row-major matrix:

```swift
let source: [Float] = [1, 2, 3, 9,
                       1, 6, 7, 1,
                       9, 0, 1, 3,
                       4, 5, 8, 1]
```

The following code computes the top 2 elements of each column:

```swift
let n = 4
let k = 2

var bestIndices = [Int32](repeating: -1,
                          count: k * n)
var bestValues = [Float](repeating: -1,
                         count: k * n)

source.withUnsafeBufferPointer { srcPtr in
    bestIndices.withUnsafeMutableBufferPointer { indicesPtr in
        bestValues.withUnsafeMutableBufferPointer { valuesPtr in
            
            var srcDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                       layout: BNNSDataLayoutRowMajorMatrix,
                                                       size: (n, n, 0, 0, 0, 0, 0, 0),
                                                       stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                       data: UnsafeMutableRawPointer(mutating: srcPtr.baseAddress),
                                                       data_type: .float,
                                                       table_data: nil,
                                                       table_data_type: .float,
                                                       data_scale: 1,
                                                       data_bias: 0)
            
            var indicesDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                           layout: BNNSDataLayoutRowMajorMatrix,
                                                           size: (n, k, 0, 0, 0, 0, 0, 0),
                                                           stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                           data: indicesPtr.baseAddress,
                                                           data_type: .int32,
                                                           table_data: nil,
                                                           table_data_type: .int32,
                                                           data_scale: 1,
                                                           data_bias: 0)
            
            var valuesDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                          layout: BNNSDataLayoutRowMajorMatrix,
                                                          size: (n, k, 0, 0, 0, 0, 0, 0),
                                                          stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                          data: valuesPtr.baseAddress,
                                                          data_type: .float,
                                                          table_data: nil,
                                                          table_data_type: .float,
                                                          data_scale: 1,
                                                          data_bias: 0)
            
            BNNSDirectApplyTopK(k,
                                0,
                                1,
                                &srcDescriptor, n * n,
                                &valuesDescriptor, k * n,
                                &indicesDescriptor, k * n,
                                nil)
        }
    }
}
```

On return, `bestIndices` and `bestValues` contain the following values, where 9 is the top value in the first column at index 2:

```swift
                     |-- 1st --|     |-- 2nd --|
          bestValues [9, 6, 8, 9,    4, 5, 7, 3]
         bestIndices [2, 1, 3, 0,    3, 3, 1, 2]
```

## Parameters

- `K`: The number of entries the operation finds.
- `axis`: The axis along which the operation finds top-k entries.
- `batch_size`: Number of input-output pairs to process.
- `input`: The descriptor of the input.
- `input_batch_stride`: Increment, in values, between inputs.
- `best_values`: The descriptor of the k best values generated by the operation.
- `best_values_batch_stride`: Increment, in values, between best values tensors.
- `best_indices`: The descriptor of the indices of the k best values generated by the operation.
- `best_indices_batch_stride`: Increment, in values, between best indices tensors.
- `filter_params`: The filter runtime parameters.

## See Also

- [func BNNSDirectApplyInTopK(Int, Int, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsdirectapplyintopk(_:_:_:_:_:_:_:_:_:_:).md)
  Applies an in-top-k filter directly to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplytopk(_:_:_:_:_:_:_:_:_:_:))*