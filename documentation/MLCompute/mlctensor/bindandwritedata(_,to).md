# bindAndWriteData(_:to:)

**Framework**: ML Compute  
**Kind**: method

Associates the given data to the tensor, and if the device is a GPU, also copies the data to the device memory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func bindAndWriteData(_ data: MLCTensorData, to device: MLCDevice) -> Bool
```

#### Return Value

`true` if the framework successfully associated the data with the tensor and copied it to the device; otherwise, `false`.

#### Discussion

The caller must guarantee the lifetime of the underlying memory of `data` for the lifetime of the tensor.

Only use this method to update device memory for tensors that are typically layer parameters, such as weights and bias for convolution layers, or beta and gamma for normalization layers. A typical use case might be implementing your own optimizer and needing to update the device memory data for these tensors.

For input tensors, use [`bindAndWriteData(_:forInputs:to:batchSize:synchronous:)`](mlcgraph/bindandwritedata(_:forinputs:to:batchsize:synchronous:).md).

## Parameters

- `data`: The data you want to associate with the tensor.
- `device`: The compute device.

## See Also

- [func synchronizeData() -> Bool](mlctensor/synchronizedata.md)
  Synchronizes the data in host memory.
- [func synchronizeOptimizerData() -> Bool](mlctensor/synchronizeoptimizerdata.md)
  Synchronizes the optimizer data in host memory.
- [func copyDataFromDeviceMemory(toBytes: UnsafeMutableRawPointer, length: Int, synchronizeWithDevice: Bool) -> Bool](mlctensor/copydatafromdevicememory(tobytes:length:synchronizewithdevice:).md)
  Copies tensor data from device memory to user-specified memory.
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?) -> Bool](mlctensor/bindoptimizerdata(_:devicedata:).md)
  Associates the optimizer and device data buffers you specify to the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/bindandwritedata(_:to:))*