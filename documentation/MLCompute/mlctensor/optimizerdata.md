# optimizerData

**Framework**: ML Compute  
**Kind**: property

An array that contains optimizer buffers you specify when you create a tensor parameter.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var optimizerData: [MLCTensorData] { get }
```

#### Discussion

These are the host-side momentum and velocity-optimizer buffers you can query and initialize.

## See Also

- [var tensorID: Int](mlctensor/tensorid.md)
  A number that uniquely identifies the tensor, which the framework assigns when it creates a tensor.
- [var descriptor: MLCTensorDescriptor](mlctensor/descriptor.md)
  The configuration object you use to create a tensor.
- [var data: Data?](mlctensor/data.md)
  The tensor data.
- [var label: String](mlctensor/label.md)
  A string that identifes this tensor.
- [var device: MLCDevice?](mlctensor/device.md)
  The device associated with this tensor.
- [var optimizerDeviceData: [MLCTensorOptimizerDeviceData]](mlctensor/optimizerdevicedata.md)
  An array that contains the device optimizer buffers you specify.
- [var hasValidNumerics: Bool](mlctensor/hasvalidnumerics.md)
  A Boolean that indicates whether a tensor contains NaN or INF values.
- [class MLCTensorOptimizerDeviceData](mlctensoroptimizerdevicedata.md)
  An encapsulation of the device memory associated with a tensor that an optimizer uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensor/optimizerdata)*