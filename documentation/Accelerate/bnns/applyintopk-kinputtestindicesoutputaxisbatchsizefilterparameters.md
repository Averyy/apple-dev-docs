# applyInTopK(k:input:testIndices:output:axis:batchSize:filterParameters:)

**Framework**: Accelerate  
**Kind**: method

Applies an in-top-k filter directly to an input.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func applyInTopK(k: Int, input: BNNSNDArrayDescriptor, testIndices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, batchSize: Int, filterParameters: BNNSFilterParameters? = nil) throws
```

#### Discussion

> ❗ **Important**:  The input data type must be `float`, the test indices data type must be `int32`, and the output data type must be `BNNSDataTypeBoolean`.

## Parameters

- `k`: The number of entries the operation finds.
- `input`: The descriptor of the input.
- `testIndices`: The descriptor of the test indices.
- `output`: The descriptor of the output.
- `axis`: The axis along which the operation finds top-k entries.
- `batchSize`: The number of input-output pairs to process.
- `filterParameters`: The filter runtime parameters.

## See Also

- [func BNNSDirectApplyInTopK(Int, Int, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsdirectapplyintopk(_:_:_:_:_:_:_:_:_:_:).md)
  Applies an in-top-k filter directly to an input.
- [static func applyTopK(k: Int, input: BNNSNDArrayDescriptor, bestValues: BNNSNDArrayDescriptor, bestIndices: BNNSNDArrayDescriptor, axis: Int, batchSize: Int, filterParameters: BNNSFilterParameters?) throws](bnns/applytopk(k:input:bestvalues:bestindices:axis:batchsize:filterparameters:).md)
  Applies a top-k filter directly to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/applyintopk(k:input:testindices:output:axis:batchsize:filterparameters:))*