# init(bytesNoCopy:length:)

**Framework**: ML Compute  
**Kind**: init

Creates a tensor data instance with the buffer of data and length of bytes you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(bytesNoCopy bytes: UnsafeMutableRawPointer, length: Int)
```

## Parameters

- `bytes`: A buffer that contains data.
- `length`: The number of bytes you choose to reference from  . This number must not exceed the length of  .

## See Also

- [convenience init(bytesNoCopy: UnsafeMutableRawPointer, length: Int, deallocator: (UnsafeMutableRawPointer, Int) -> Void)](mlctensordata/init(bytesnocopy:length:deallocator:).md)
  Creates a tensor data instance with a data buffer, byte length, and custom deallocator closure you specify.
- [convenience init(immutableBytesNoCopy: UnsafeRawPointer, length: Int)](mlctensordata/init(immutablebytesnocopy:length:).md)
  Creates a tensor data instance with the buffer of immutable data and length of bytes you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata/init(bytesnocopy:length:))*