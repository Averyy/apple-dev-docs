# copyDataFromDeviceMemory(toBytes:length:synchronizeWithDevice:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Copies tensor data from device memory to user-specified memory.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func copyDataFromDeviceMemory(toBytes bytes: UnsafeMutableRawPointer, length: Int, synchronizeWithDevice: Bool) -> Bool
```

```objc
- (BOOL) copyDataFromDeviceMemoryToBytes:(void *) bytes length:(NSUInteger) length synchronizeWithDevice:(BOOL) synchronizeWithDevice;
```

## Return Value

`true` if successful; otherwise, `false` if the framework failed to copy or synchronize.

## Discussion

When the device is a GPU, you may need to synchronize the device memory, that is, set `synchronizeWithDevice` to `true`. The framework ignores `synchronizeWithDevice` when the device is the CPU.

> ❗ **Important**:  Only call this method once the graph, with which you used this tensor, finishes execution. Otherwise the results in device memory may not be up to date. When the device is a GPU, you must set `synchronizeWithDevice` to `false` when you call this method in a completion handler. If you specified a tensor for the outputs of a graph using `addOutputs`, set `synchronizeWithDevice` to `false`.

## Parameters

- `bytes`: The data to copy.
- `length`: The number of bytes you specify for the framework to copy.
- `synchronizeWithDevice`: A Boolean that indicates whether you choose to synchronize device memory if the device is a GPU.

## See Also

### Managing Tensor Data
- [func synchronizeData() -> Bool](./synchronizedata%28%29.md)
  Synchronizes the data in host memory.
- [func synchronizeOptimizerData() -> Bool](./synchronizeoptimizerdata%28%29.md)
  Synchronizes the optimizer data in host memory.
- [func bindAndWriteData(MLCTensorData, to: MLCDevice) -> Bool](./bindandwritedata%28_,to%29.md)
  Associates the given data to the tensor, and if the device is a GPU, also copies the data to the device memory.
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?) -> Bool](./bindoptimizerdata%28_,devicedata%29.md)
  Associates the optimizer and device data buffers you specify to the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/copydatafromdevicememory(tobytes:length:synchronizewithdevice:))*