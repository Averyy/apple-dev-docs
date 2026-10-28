# bindAndWriteData(_:to:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Associates the given data to the tensor, and if the device is a GPU, also copies the data to the device memory.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func bindAndWriteData(_ data: MLCTensorData, to device: MLCDevice) -> Bool
```

```objc
- (BOOL) bindAndWriteData:(MLCTensorData *) data toDevice:(MLCDevice *) device;
```

## Return Value

`true` if the framework successfully associated the data with the tensor and copied it to the device; otherwise, `false`.

## Discussion

The caller must guarantee the lifetime of the underlying memory of `data` for the lifetime of the tensor.

Only use this method to update device memory for tensors that are typically layer parameters, such as weights and bias for convolution layers, or beta and gamma for normalization layers. A typical use case might be implementing your own optimizer and needing to update the device memory data for these tensors.

For input tensors, use [`bindAndWriteData(_:forInputs:to:batchSize:synchronous:)`](../mlcgraph/bindandwritedata%28_,forinputs,to,batchsize,synchronous%29.md).

## Parameters

- `data`: The data you want to associate with the tensor.
- `device`: The compute device.

## See Also

### Managing Tensor Data
- [func synchronizeData() -> Bool](./synchronizedata%28%29.md)
  Synchronizes the data in host memory.
- [func synchronizeOptimizerData() -> Bool](./synchronizeoptimizerdata%28%29.md)
  Synchronizes the optimizer data in host memory.
- [func copyDataFromDeviceMemory(toBytes: UnsafeMutableRawPointer, length: Int, synchronizeWithDevice: Bool) -> Bool](./copydatafromdevicememory%28tobytes,length,synchronizewithdevice%29.md)
  Copies tensor data from device memory to user-specified memory.
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?) -> Bool](./bindoptimizerdata%28_,devicedata%29.md)
  Associates the optimizer and device data buffers you specify to the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/bindandwritedata(_:to:))*