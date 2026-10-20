# bindOptimizerData(_:deviceData:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Associates the optimizer and device data buffers you specify to the tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func bindOptimizerData(_ data: [MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?) -> Bool
```

```objc
- (BOOL) bindOptimizerData:(NSArray<MLCTensorData *> *) data deviceData:(NSArray<MLCTensorOptimizerDeviceData *> *) deviceData;
```

#### Return Value

`true` if the framework successfully associated the data and device data with the tensor; otherwise, `false`.

## Parameters

- `data`: An array that contains the optimizer data to associate with the tensor.
- `deviceData`: An array that contains the optimizer device data to associate with the tensor.

## See Also

### Managing Tensor Data
- [func synchronizeData() -> Bool](./synchronizedata%28%29.md)
  Synchronizes the data in host memory.
- [func synchronizeOptimizerData() -> Bool](./synchronizeoptimizerdata%28%29.md)
  Synchronizes the optimizer data in host memory.
- [func copyDataFromDeviceMemory(toBytes: UnsafeMutableRawPointer, length: Int, synchronizeWithDevice: Bool) -> Bool](./copydatafromdevicememory%28tobytes,length,synchronizewithdevice%29.md)
  Copies tensor data from device memory to user-specified memory.
- [func bindAndWriteData(MLCTensorData, to: MLCDevice) -> Bool](./bindandwritedata%28_,to%29.md)
  Associates the given data to the tensor, and if the device is a GPU, also copies the data to the device memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/bindoptimizerdata(_:devicedata:))*