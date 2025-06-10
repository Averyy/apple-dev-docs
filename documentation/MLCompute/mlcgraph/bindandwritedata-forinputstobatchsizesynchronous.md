# bindAndWriteData(_:forInputs:to:batchSize:synchronous:)

**Framework**: ML Compute  
**Kind**: method

Associates the given data with the input tensors, and if the device is a GPU, also copies the data to the device memory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func bindAndWriteData(_ inputsData: [String : MLCTensorData], forInputs inputTensors: [String : MLCTensor], to device: MLCDevice, batchSize: Int, synchronous: Bool) -> Bool
```

#### Return Value

`true` if the data is successfully associated with input tensors, otherwise `false`.

#### Discussion

Use this method if you execute the forward, gradient, and optimizer updates independently. Write the inputs to device memory before the layer executes the forward pass. Similarly, write the inputs—typically the initial gradient tensor—to device memory before the layer executes the gradient pass.

Use asynchronous execution for better performance, except when testing or debugging.

> ❗ **Important**:  You must guarantee the lifetime of the underlying memory of each value of `inputsData` for the entirety of each corresponding input tensor’s lifetime.

## Parameters

- `inputsData`: An array that contains the input data to write to device memory.
- `inputTensors`: The list of tensors to perform writes on.
- `device`: The compute device.
- `batchSize`: The batch size.
- `synchronous`: A Boolean value that indicates whether to execute the copy to the device synchronously.

## See Also

- [func bindAndWriteData([String : MLCTensorData], forInputs: [String : MLCTensor], to: MLCDevice, synchronous: Bool) -> Bool](mlcgraph/bindandwritedata(_:forinputs:to:synchronous:).md)
  Associates the given data with the input tensors, and if the device is a GPU, also copies the data to the device memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/bindandwritedata(_:forinputs:to:batchsize:synchronous:))*