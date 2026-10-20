# optimizerDeviceData

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An array that contains the device optimizer buffers you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var optimizerDeviceData: [MLCTensorOptimizerDeviceData] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<MLCTensorOptimizerDeviceData *> * optimizerDeviceData;
```

#### Discussion

These are the host-side momentum and velocity-optimizer buffers you can query and initialize.

## See Also

### Inspecting Tensors
- [var tensorID: Int](./tensorid.md)
  A number that uniquely identifies the tensor, which the framework assigns when it creates a tensor.
- [var descriptor: MLCTensorDescriptor](./descriptor.md)
  The configuration object you use to create a tensor.
- [var data: Data?](./data.md)
  The tensor data.
- [var label: String](./label.md)
  A string that identifes this tensor.
- [var device: MLCDevice?](./device.md)
  The device associated with this tensor.
- [var optimizerData: [MLCTensorData]](./optimizerdata.md)
  An array that contains optimizer buffers you specify when you create a tensor parameter.
- [var hasValidNumerics: Bool](./hasvalidnumerics.md)
  A Boolean that indicates whether a tensor contains NaN or INF values.
- [class MLCTensorOptimizerDeviceData](../mlctensoroptimizerdevicedata.md)
  An encapsulation of the device memory associated with a tensor that an optimizer uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/optimizerdevicedata)*