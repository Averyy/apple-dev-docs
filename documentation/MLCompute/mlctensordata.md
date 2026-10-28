# MLCTensorData

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

An encapsulation of the memory that tensor data uses.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCTensorData
```

```objc
@interface MLCTensorData : NSObject
```

## Overview

> ❗ **Important**:  A tensor data instance doesn’t take ownership of the `bytes` pointer and therefore won’t free it upon deallocation.

## Topics

### Creating Tensor Data
- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](./mlctensordata/init%28bytesnocopy,length%29.md)
  Creates a tensor data instance with the buffer of data and length of bytes you specify.
- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, deallocator: (UnsafeMutableRawPointer, Int) -> Void)](./mlctensordata/init%28bytesnocopy,length,deallocator%29.md)
  Creates a tensor data instance with a data buffer, byte length, and custom deallocator closure you specify.
- [convenience init(immutableBytesNoCopy: UnsafeRawPointer, length: Int)](./mlctensordata/init%28immutablebytesnocopy,length%29.md)
  Creates a tensor data instance with the buffer of immutable data and length of bytes you specify.
### Inspecting Tensor Data
- [var bytes: UnsafeMutableRawPointer](./mlctensordata/bytes.md)
  A buffer that conains data.
- [var length: Int](./mlctensordata/length.md)
  The number of bytes you choose to hold for this tensor data instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Tensors with Descriptors
- [convenience init(descriptor: MLCTensorDescriptor)](./mlctensor/init%28descriptor%29.md)
  Creates a tensor without data, using the descriptor you specify.
- [convenience init(descriptor: MLCTensorDescriptor, data: MLCTensorData)](./mlctensor/init%28descriptor,data%29.md)
  Creates a tensor with the descriptor and data you specify.
- [convenience init(descriptor: MLCTensorDescriptor, fillWithData: NSNumber)](./mlctensor/init%28descriptor,fillwithdata%29.md)
  Creates a tensor with the descriptor and scalar value you specify.
- [convenience init(descriptor: MLCTensorDescriptor, randomInitializerType: MLCRandomInitializerType)](./mlctensor/init%28descriptor,randominitializertype%29.md)
  Creates a tensor with the descriptor and random initializer type you specify.
- [class MLCTensorDescriptor](./mlctensordescriptor.md)
  A configuration object you use to create a tensor.
- [enum MLCDataType](./mlcdatatype.md)
  A tensor data type.
- [enum MLCRandomInitializerType](./mlcrandominitializertype.md)
  An initializer type you use to create a tensor with random data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata)*