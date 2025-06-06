# bindOptimizerData(_:deviceData:)

**Framework**: ML Compute  
**Kind**: method

Associates the optimizer and device data buffers you specify to the tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func bindOptimizerData(_ data: [MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?) -> Bool
```

#### Return Value

`true` if the framework successfully associated the data and device data with the tensor; otherwise, `false`.

## Parameters

- `data`: An array that contains the optimizer data to associate with the tensor.
- `deviceData`: An array that contains the optimizer device data to associate with the tensor.

## See Also

- [func synchronizeData() -> Bool](mlctensor/synchronizedata.md)
  Synchronizes the data in host memory.
- [func synchronizeOptimizerData() -> Bool](mlctensor/synchronizeoptimizerdata.md)
  Synchronizes the optimizer data in host memory.
- [func copyDataFromDeviceMemory(toBytes: UnsafeMutableRawPointer, length: Int, synchronizeWithDevice: Bool) -> Bool](mlctensor/copydatafromdevicememory(tobytes:length:synchronizewithdevice:).md)
  Copies tensor data from device memory to user-specified memory.
- [func bindAndWriteData(MLCTensorData, to: MLCDevice) -> Bool](mlctensor/bindandwritedata(_:to:).md)
  Associates the given data to the tensor, and if the device is a GPU, also copies the data to the device memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/bindoptimizerdata(_:devicedata:))*