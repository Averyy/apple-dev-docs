# init(bytesNoCopy:length:deallocator:)

**Framework**: ML Compute  
**Kind**: init

Creates a tensor data instance with a data buffer, byte length, and custom deallocator closure you specify.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
convenience init(bytesNoCopy bytes: UnsafeMutableRawPointer, length: Int, deallocator: @escaping (UnsafeMutableRawPointer, Int) -> Void)
```

#### Return Value

A new `MLCTensorData` instance.

## Parameters

- `bytes`: A buffer that contains data.
- `length`: The number of bytes you want to reference from  . This number must not exceed the length of  .
- `deallocator`: A callback to invoke after the system deallocates the object instance.

## See Also

- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int)](mlctensordata/init(bytesnocopy:length:).md)
  Creates a tensor data instance with the buffer of data and length of bytes you specify.
- [convenience init(immutableBytesNoCopy: UnsafeRawPointer, length: Int)](mlctensordata/init(immutablebytesnocopy:length:).md)
  Creates a tensor data instance with the buffer of immutable data and length of bytes you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata/init(bytesnocopy:length:deallocator:))*