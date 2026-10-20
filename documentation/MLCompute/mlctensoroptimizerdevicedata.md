# MLCTensorOptimizerDeviceData

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

An encapsulation of the device memory associated with a tensor that an optimizer uses.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCTensorOptimizerDeviceData
```

```objc
@interface MLCTensorOptimizerDeviceData : NSObject
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Inspecting Tensors
- [var tensorID: Int](./mlctensor/tensorid.md)
  A number that uniquely identifies the tensor, which the framework assigns when it creates a tensor.
- [var descriptor: MLCTensorDescriptor](./mlctensor/descriptor.md)
  The configuration object you use to create a tensor.
- [var data: Data?](./mlctensor/data.md)
  The tensor data.
- [var label: String](./mlctensor/label.md)
  A string that identifes this tensor.
- [var device: MLCDevice?](./mlctensor/device.md)
  The device associated with this tensor.
- [var optimizerData: [MLCTensorData]](./mlctensor/optimizerdata.md)
  An array that contains optimizer buffers you specify when you create a tensor parameter.
- [var optimizerDeviceData: [MLCTensorOptimizerDeviceData]](./mlctensor/optimizerdevicedata.md)
  An array that contains the device optimizer buffers you specify.
- [var hasValidNumerics: Bool](./mlctensor/hasvalidnumerics.md)
  A Boolean that indicates whether a tensor contains NaN or INF values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensoroptimizerdevicedata)*