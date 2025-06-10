# MLCTensorData

**Framework**: ML Compute  
**Kind**: class

An encapsulation of the memory that tensor data uses.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCTensorData
```

#### Overview

> ❗ **Important**:  A tensor data instance doesn’t take ownership of the `bytes` pointer and therefore won’t free it upon deallocation.

## Topics

### Creating Tensor Data
- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](mlctensordata/init(bytesnocopy:length:).md)
  Creates a tensor data instance with the buffer of data and length of bytes you specify.
- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, deallocator: (UnsafeMutableRawPointer, Int) -> Void)](mlctensordata/init(bytesnocopy:length:deallocator:).md)
  Creates a tensor data instance with a data buffer, byte length, and custom deallocator closure you specify.
- [convenience init(immutableBytesNoCopy: UnsafeRawPointer, length: Int)](mlctensordata/init(immutablebytesnocopy:length:).md)
  Creates a tensor data instance with the buffer of immutable data and length of bytes you specify.
### Inspecting Tensor Data
- [var bytes: UnsafeMutableRawPointer](mlctensordata/bytes.md)
  A buffer that conains data.
- [var length: Int](mlctensordata/length.md)
  The number of bytes you choose to hold for this tensor data instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(descriptor: MLCTensorDescriptor)](mlctensor/init(descriptor:).md)
  Creates a tensor without data, using the descriptor you specify.
- [convenience init(descriptor: MLCTensorDescriptor, data: MLCTensorData)](mlctensor/init(descriptor:data:).md)
  Creates a tensor with the descriptor and data you specify.
- [convenience init(descriptor: MLCTensorDescriptor, fillWithData: NSNumber)](mlctensor/init(descriptor:fillwithdata:).md)
  Creates a tensor with the descriptor and scalar value you specify.
- [convenience init(descriptor: MLCTensorDescriptor, randomInitializerType: MLCRandomInitializerType)](mlctensor/init(descriptor:randominitializertype:).md)
  Creates a tensor with the descriptor and random initializer type you specify.
- [class MLCTensorDescriptor](mlctensordescriptor.md)
  A configuration object you use to create a tensor.
- [enum MLCDataType](mlcdatatype.md)
  A tensor data type.
- [enum MLCRandomInitializerType](mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata)*