# MLCTensorOptimizerDeviceData

**Framework**: ML Compute  
**Kind**: class

An encapsulation of the device memory associated with a tensor that an optimizer uses.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCTensorOptimizerDeviceData
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [var optimizerData: [MLCTensorData]](mlctensor/optimizerdata.md)
  An array that contains optimizer buffers you specify when you create a tensor parameter.
- [var optimizerDeviceData: [MLCTensorOptimizerDeviceData]](mlctensor/optimizerdevicedata.md)
  An array that contains the device optimizer buffers you specify.
- [var hasValidNumerics: Bool](mlctensor/hasvalidnumerics.md)
  A Boolean that indicates whether a tensor contains NaN or INF values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensoroptimizerdevicedata)*