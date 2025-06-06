# synchronizeOptimizerData()

**Framework**: ML Compute  
**Kind**: method

Synchronizes the optimizer data in host memory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func synchronizeOptimizerData() -> Bool
```

#### Return Value

`true` if synchronization is successful; otherwise, `false`.

#### Discussion

This method synchronizes the [`optimizerData`](mlctensor/optimizerdata.md) in host memory with latest contents in device memory.

Only call this method once the graph, with which you used this tensor, finishes execution; otherwise the results in device memory may not be up to date.

> ❗ **Important**:  Don’t call this method from a completion callback when the device is a GPU.

 Don’t call this method from a completion callback when the device is a GPU.

## See Also

- [func synchronizeData() -> Bool](mlctensor/synchronizedata.md)
  Synchronizes the data in host memory.
- [func copyDataFromDeviceMemory(toBytes: UnsafeMutableRawPointer, length: Int, synchronizeWithDevice: Bool) -> Bool](mlctensor/copydatafromdevicememory(tobytes:length:synchronizewithdevice:).md)
  Copies tensor data from device memory to user-specified memory.
- [func bindAndWriteData(MLCTensorData, to: MLCDevice) -> Bool](mlctensor/bindandwritedata(_:to:).md)
  Associates the given data to the tensor, and if the device is a GPU, also copies the data to the device memory.
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?) -> Bool](mlctensor/bindoptimizerdata(_:devicedata:).md)
  Associates the optimizer and device data buffers you specify to the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/synchronizeoptimizerdata())*