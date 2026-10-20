# synchronizeData()

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Synchronizes the data in host memory.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func synchronizeData() -> Bool
```

```objc
- (BOOL) synchronizeData;
```

#### Return Value

`true` if synchronization is successful; otherwise, `false`.

#### Discussion

This method synchronizes the tensor’s [`data`](./data.md) in host memory with the latest contents in device memory.

Only call this method once the graph, with which you used this tensor, finishes execution; otherwise the results in device memory may not be up to date.

> ❗ **Important**:  Don’t call this method from a completion callback when the device is a GPU.

## See Also

### Managing Tensor Data
- [func synchronizeOptimizerData() -> Bool](./synchronizeoptimizerdata%28%29.md)
  Synchronizes the optimizer data in host memory.
- [func copyDataFromDeviceMemory(toBytes: UnsafeMutableRawPointer, length: Int, synchronizeWithDevice: Bool) -> Bool](./copydatafromdevicememory%28tobytes,length,synchronizewithdevice%29.md)
  Copies tensor data from device memory to user-specified memory.
- [func bindAndWriteData(MLCTensorData, to: MLCDevice) -> Bool](./bindandwritedata%28_,to%29.md)
  Associates the given data to the tensor, and if the device is a GPU, also copies the data to the device memory.
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?) -> Bool](./bindoptimizerdata%28_,devicedata%29.md)
  Associates the optimizer and device data buffers you specify to the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/synchronizedata())*