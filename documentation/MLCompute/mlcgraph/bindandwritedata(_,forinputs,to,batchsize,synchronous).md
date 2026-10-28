# bindAndWriteData(_:forInputs:to:batchSize:synchronous:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Associates the given data with the input tensors, and if the device is a GPU, also copies the data to the device memory.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func bindAndWriteData(_ inputsData: [String : MLCTensorData], forInputs inputTensors: [String : MLCTensor], to device: MLCDevice, batchSize: Int, synchronous: Bool) -> Bool
```

```objc
- (BOOL) bindAndWriteData:(NSDictionary<NSString *,MLCTensorData *> *) inputsData forInputs:(NSDictionary<NSString *,MLCTensor *> *) inputTensors toDevice:(MLCDevice *) device batchSize:(NSUInteger) batchSize synchronous:(BOOL) synchronous;
```

## Return Value

`true` if the data is successfully associated with input tensors, otherwise `false`.

## Discussion

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

### Associating Data with Input Tensors
- [func bindAndWriteData([String : MLCTensorData], forInputs: [String : MLCTensor], to: MLCDevice, synchronous: Bool) -> Bool](./bindandwritedata%28_,forinputs,to,synchronous%29.md)
  Associates the given data with the input tensors, and if the device is a GPU, also copies the data to the device memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraph/bindandwritedata(_:forinputs:to:batchsize:synchronous:))*